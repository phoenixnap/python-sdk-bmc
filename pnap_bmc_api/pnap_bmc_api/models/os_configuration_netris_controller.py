# coding: utf-8

"""
    Bare Metal Cloud API

    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API.  Deprovision servers, get or edit SSH key details, assign public IPs, assign servers to networks and a lot more.  Manage your infrastructure more efficiently using just a few simple API calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)</b> 

    The version of the OpenAPI document: 0.1
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

class OsConfigurationNetrisController(BaseModel):
    """
    Netris Controller configuration properties. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/netris-bare-metal-cloud#deploy-netris-controller' target='_blank'>here</a>.
    """ # noqa: E501
    host_os: Optional[StrictStr] = Field(default=None, description="(Read-only) Host OS on which the Netris Controller is installed.", alias="hostOs")
    netris_web_console_url: Optional[StrictStr] = Field(default=None, description="(Read-only) The URL for the Netris Controller web console. It will only be returned in response to provisioning a server.", alias="netrisWebConsoleUrl")
    netris_user_password: Optional[StrictStr] = Field(default=None, description="(Read-only) Auto-generated password set for user 'netris' in the web console.<br>  The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference.", alias="netrisUserPassword")
    __properties: ClassVar[List[str]] = ["hostOs", "netrisWebConsoleUrl", "netrisUserPassword"]

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
        """Create an instance of OsConfigurationNetrisController from a JSON string"""
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
        """Create an instance of OsConfigurationNetrisController from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostOs": obj.get("hostOs"),
            "netrisWebConsoleUrl": obj.get("netrisWebConsoleUrl"),
            "netrisUserPassword": obj.get("netrisUserPassword")
        })
        return _obj


