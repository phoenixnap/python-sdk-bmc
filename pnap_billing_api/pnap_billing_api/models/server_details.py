# coding: utf-8

"""
    Billing API

    Automate your infrastructure billing with the Bare Metal Cloud Billing API. Reserve your server instances to ensure guaranteed resource availability for 12, 24, and 36 months. Retrieve your server’s rated usage for a given period and enable or disable auto-renewals.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/phoenixnap-bare-metal-cloud-billing-models' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/billing/v1/)</b> 

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServerDetails(BaseModel):
    """
    Details of the server associated with this rated usage record.
    """ # noqa: E501
    id: StrictStr = Field(description="The server identifier as returned by the BMC API.")
    hostname: StrictStr = Field(description="The server hostname.")
    __properties: ClassVar[List[str]] = ["id", "hostname"]

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
        """Create an instance of ServerDetails from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServerDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "hostname": obj.get("hostname")
        })
        return _obj


