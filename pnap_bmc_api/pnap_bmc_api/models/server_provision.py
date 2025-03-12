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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from pnap_bmc_api.models.network_configuration import NetworkConfiguration
from pnap_bmc_api.models.os_configuration import OsConfiguration
from pnap_bmc_api.models.storage_configuration import StorageConfiguration
from pnap_bmc_api.models.tag_assignment_request import TagAssignmentRequest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServerProvision(BaseModel):
    """
    Provision bare metal server.
    """ # noqa: E501
    hostname: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(description="Hostname of server.")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Description of server.")
    os: StrictStr = Field(description="The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `ubuntu/jammy+pytorch`, `ubuntu/noble`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `windows/srv2022std`, `windows/srv2022dc`, `esxi/esxi70`, `esxi/esxi80`, `almalinux/almalinux8`, `almalinux/almalinux9`, `rockylinux/rockylinux8`, `rockylinux/rockylinux9`, `virtuozzo/virtuozzo7`, `oraclelinux/oraclelinux9`, `debian/bullseye`, `debian/bookworm`, `proxmox/bullseye`, `proxmox/proxmox8`, `netris/controller`, `netris/softgate_1g`, `netris/softgate_10g` or `netris/softgate_25g`.")
    install_default_ssh_keys: Optional[StrictBool] = Field(default=True, description="Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request.", alias="installDefaultSshKeys")
    ssh_keys: Optional[List[StrictStr]] = Field(default=None, description="A list of SSH keys that will be installed on the server.", alias="sshKeys")
    ssh_key_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request.", alias="sshKeyIds")
    network_type: Optional[StrictStr] = Field(default='PUBLIC_AND_PRIVATE', description="The type of network configuration for this server.<br> Currently this field should be set to `PUBLIC_AND_PRIVATE`, `PRIVATE_ONLY`, `PUBLIC_ONLY` or `USER_DEFINED`.<br> Setting the `force` query parameter to `true` allows you to configure network configuration type as `NONE`.", alias="networkType")
    os_configuration: Optional[OsConfiguration] = Field(default=None, alias="osConfiguration")
    tags: Optional[List[TagAssignmentRequest]] = Field(default=None, description="Tags to set to the server. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview).")
    network_configuration: Optional[NetworkConfiguration] = Field(default=None, alias="networkConfiguration")
    storage_configuration: Optional[StorageConfiguration] = Field(default=None, alias="storageConfiguration")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["hostname", "description", "os", "installDefaultSshKeys", "sshKeys", "sshKeyIds", "networkType", "osConfiguration", "tags", "networkConfiguration", "storageConfiguration"]

    @field_validator('hostname')
    def hostname_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?=.*[a-zA-Z])([a-zA-Z0-9().-])+$", value):
            raise ValueError(r"must validate the regular expression /^(?=.*[a-zA-Z])([a-zA-Z0-9().-])+$/")
        return value

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
        """Create an instance of ServerProvision from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of os_configuration
        if self.os_configuration:
            _dict['osConfiguration'] = self.os_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of network_configuration
        if self.network_configuration:
            _dict['networkConfiguration'] = self.network_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_configuration
        if self.storage_configuration:
            _dict['storageConfiguration'] = self.storage_configuration.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServerProvision from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostname": obj.get("hostname"),
            "description": obj.get("description"),
            "os": obj.get("os"),
            "installDefaultSshKeys": obj.get("installDefaultSshKeys") if obj.get("installDefaultSshKeys") is not None else True,
            "sshKeys": obj.get("sshKeys"),
            "sshKeyIds": obj.get("sshKeyIds"),
            "networkType": obj.get("networkType") if obj.get("networkType") is not None else 'PUBLIC_AND_PRIVATE',
            "osConfiguration": OsConfiguration.from_dict(obj.get("osConfiguration")) if obj.get("osConfiguration") is not None else None,
            "tags": [TagAssignmentRequest.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "networkConfiguration": NetworkConfiguration.from_dict(obj.get("networkConfiguration")) if obj.get("networkConfiguration") is not None else None,
            "storageConfiguration": StorageConfiguration.from_dict(obj.get("storageConfiguration")) if obj.get("storageConfiguration") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


