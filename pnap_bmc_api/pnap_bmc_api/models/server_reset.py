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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from pnap_bmc_api.models.os_configuration_map import OsConfigurationMap
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServerReset(BaseModel):
    """
    Reset bare metal server.
    """ # noqa: E501
    install_default_ssh_keys: Optional[StrictBool] = Field(default=True, description="Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request.", alias="installDefaultSshKeys")
    ssh_keys: Optional[List[StrictStr]] = Field(default=None, description="A list of SSH keys that will be installed on the server.", alias="sshKeys")
    ssh_key_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request.", alias="sshKeyIds")
    os_configuration: Optional[OsConfigurationMap] = Field(default=None, alias="osConfiguration")
    __properties: ClassVar[List[str]] = ["installDefaultSshKeys", "sshKeys", "sshKeyIds", "osConfiguration"]

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
        """Create an instance of ServerReset from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of os_configuration
        if self.os_configuration:
            _dict['osConfiguration'] = self.os_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServerReset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "installDefaultSshKeys": obj.get("installDefaultSshKeys") if obj.get("installDefaultSshKeys") is not None else True,
            "sshKeys": obj.get("sshKeys"),
            "sshKeyIds": obj.get("sshKeyIds"),
            "osConfiguration": OsConfigurationMap.from_dict(obj.get("osConfiguration")) if obj.get("osConfiguration") is not None else None
        })
        return _obj


