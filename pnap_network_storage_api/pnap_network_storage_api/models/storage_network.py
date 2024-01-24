# coding: utf-8

"""
    Network Storage API

    Create, list, edit, and delete storage networks with the Network Storage API. Use storage networks to expand storage capacity on a private network. <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bare-metal-cloud-storage' target='_blank'>here</a> </span> <br> <b>All URLs are relative to (https://api.phoenixnap.com/network-storage/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from pnap_network_storage_api.models.status import Status
from pnap_network_storage_api.models.volume import Volume
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class StorageNetwork(BaseModel):
    """
    Storage network.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Storage network ID.")
    name: Optional[StrictStr] = Field(default=None, description="Storage network friendly name.")
    description: Optional[StrictStr] = Field(default=None, description="Storage network description.")
    status: Optional[Status] = None
    location: Optional[StrictStr] = Field(default=None, description="Location of storage network. Currently this field should be set to `PHX` or `ASH`.")
    network_id: Optional[StrictStr] = Field(default=None, description="Id of network the storage belongs to.", alias="networkId")
    ips: Optional[List[StrictStr]] = Field(default=None, description="IP of the storage network.")
    created_on: Optional[datetime] = Field(default=None, description="Date and time when this storage network was created.", alias="createdOn")
    delete_requested_on: Optional[datetime] = Field(default=None, description="Date and time of the initial request for storage network deletion.", alias="deleteRequestedOn")
    volumes: Optional[List[Volume]] = Field(default=None, description="Volume for a storage network.")
    __properties: ClassVar[List[str]] = ["id", "name", "description", "status", "location", "networkId", "ips", "createdOn", "deleteRequestedOn", "volumes"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StorageNetwork from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in volumes (list)
        _items = []
        if self.volumes:
            for _item in self.volumes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['volumes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of StorageNetwork from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "location": obj.get("location"),
            "networkId": obj.get("networkId"),
            "ips": obj.get("ips"),
            "createdOn": obj.get("createdOn"),
            "deleteRequestedOn": obj.get("deleteRequestedOn"),
            "volumes": [Volume.from_dict(_item) for _item in obj.get("volumes")] if obj.get("volumes") is not None else None
        })
        return _obj

