# coding: utf-8

"""
    Networks API

    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.<br> <br> <span class='pnap-api-knowledge-base-link'> Helpful knowledge base articles are available for  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>multi-private backend networks</a> and <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-15' target='_blank'>public networks</a>. </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b> 

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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Error(BaseModel):
    """
    Error
    """ # noqa: E501
    message: StrictStr = Field(description="The description detailing the cause of the error code.")
    validation_errors: Optional[List[StrictStr]] = Field(default=None, description="Validation errors, if any.", alias="validationErrors")
    __properties: ClassVar[List[str]] = ["message", "validationErrors"]

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
        """Create an instance of Error from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "message",
                "validation_errors",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Error from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "validationErrors": obj.get("validationErrors")
        })
        return _obj


