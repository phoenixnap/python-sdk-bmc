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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from pnap_ip_api.models.tag_assignment_request import TagAssignmentRequest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class IpBlockCreate(BaseModel):
    """
    IP Block Request.
    """ # noqa: E501
    location: StrictStr = Field(description="IP Block location ID. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.")
    cidr_block_size: StrictStr = Field(description="CIDR IP Block Size. V4 supported sizes: [`/31`, `/30`, `/29` or `/28`]. V6 supported sizes: [`/64`]. For a larger Block Size contact support.", alias="cidrBlockSize")
    ip_version: Optional[StrictStr] = Field(default='V4', description="IP Version. This field should be set to `V4` or `V6`", alias="ipVersion")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="The description of the IP Block.")
    tags: Optional[List[TagAssignmentRequest]] = Field(default=None, description="Tags to set to the ip-block. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview).")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["location", "cidrBlockSize", "ipVersion", "description", "tags"]

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
        """Create an instance of IpBlockCreate from a JSON string"""
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
        """Create an instance of IpBlockCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location": obj.get("location"),
            "cidrBlockSize": obj.get("cidrBlockSize"),
            "ipVersion": obj.get("ipVersion") if obj.get("ipVersion") is not None else 'V4',
            "description": obj.get("description"),
            "tags": [TagAssignmentRequest.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


