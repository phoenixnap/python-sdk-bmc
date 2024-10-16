# coding: utf-8

"""
    IP Addresses API

    Public IP blocks are a set of contiguous IPs that allow you to access your servers or networks from the internet. Use the IP Addresses API to request and delete IP blocks.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/public-ip-management#bmc-public-ip-allocations-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/ips/v1/)</b> 

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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from pnap_ip_api.models.tag_assignment import TagAssignment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IpBlock(BaseModel):
    """
    IP Block Details.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="IP Block identifier.")
    location: Optional[StrictStr] = Field(default=None, description="IP Block location ID. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.")
    cidr_block_size: Optional[StrictStr] = Field(default=None, description="CIDR IP Block Size. Currently this field should be set to either `/31`, `/30`, `/29`, `/28`, `/27`, `/26`, `/25`, `/24`, `/23` or `/22`.", alias="cidrBlockSize")
    cidr: Optional[StrictStr] = Field(default=None, description="The IP Block in CIDR notation.")
    ip_version: Optional[StrictStr] = Field(default=None, description="The IP Version of the block.", alias="ipVersion")
    status: Optional[StrictStr] = Field(default=None, description="The status of the IP Block. Can have one of the following values: `creating` , `assigning` , `error assigning` , `assigned` , `unassigning` , `error unassigning` or `unassigned`.")
    assigned_resource_id: Optional[StrictStr] = Field(default=None, description="ID of the resource assigned to the IP Block.", alias="assignedResourceId")
    assigned_resource_type: Optional[StrictStr] = Field(default=None, description="Type of the resource assigned to the IP Block.", alias="assignedResourceType")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="The description of the IP Block.")
    tags: Optional[List[TagAssignment]] = Field(default=None, description="The tags assigned if any.")
    is_bring_your_own: Optional[StrictBool] = Field(default=None, description="True if the IP block is a `bring your own` block.", alias="isBringYourOwn")
    created_on: Optional[datetime] = Field(default=None, description="Date and time when the IP block was created.", alias="createdOn")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "location", "cidrBlockSize", "cidr", "ipVersion", "status", "assignedResourceId", "assignedResourceType", "description", "tags", "isBringYourOwn", "createdOn"]

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
        """Create an instance of IpBlock from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "additional_properties",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of IpBlock from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "location": obj.get("location"),
            "cidrBlockSize": obj.get("cidrBlockSize"),
            "cidr": obj.get("cidr"),
            "ipVersion": obj.get("ipVersion"),
            "status": obj.get("status"),
            "assignedResourceId": obj.get("assignedResourceId"),
            "assignedResourceType": obj.get("assignedResourceType"),
            "description": obj.get("description"),
            "tags": [TagAssignment.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "isBringYourOwn": obj.get("isBringYourOwn"),
            "createdOn": obj.get("createdOn")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


