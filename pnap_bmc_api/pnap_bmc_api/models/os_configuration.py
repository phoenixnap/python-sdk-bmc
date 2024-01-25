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
from typing_extensions import Annotated
from pnap_bmc_api.models.os_configuration_cloud_init import OsConfigurationCloudInit
from pnap_bmc_api.models.os_configuration_netris_controller import OsConfigurationNetrisController
from pnap_bmc_api.models.os_configuration_netris_softgate import OsConfigurationNetrisSoftgate
from pnap_bmc_api.models.os_configuration_windows import OsConfigurationWindows
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class OsConfiguration(BaseModel):
    """
    OS specific configuration properties.
    """ # noqa: E501
    netris_controller: Optional[OsConfigurationNetrisController] = Field(default=None, alias="netrisController")
    netris_softgate: Optional[OsConfigurationNetrisSoftgate] = Field(default=None, alias="netrisSoftgate")
    windows: Optional[OsConfigurationWindows] = None
    root_password: Optional[StrictStr] = Field(default=None, description="(Read-only) Auto-generated password set for user 'root' on an ESXi or Proxmox server.<br>  The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference.", alias="rootPassword")
    management_ui_url: Optional[StrictStr] = Field(default=None, description="(Read-only) The URL of the management UI which will only be returned in response to provisioning a server.", alias="managementUiUrl")
    management_access_allowed_ips: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="List of IPs allowed to access the Management UI. Supported in single IP, CIDR and range format. When undefined, Management UI is disabled. This will only be returned in response to provisioning a server.", alias="managementAccessAllowedIps")
    install_os_to_ram: Optional[StrictBool] = Field(default=False, description="If true, OS will be installed to and booted from the server's RAM. On restart RAM OS will be lost and the server will not be reachable unless a custom bootable OS has been deployed. Follow the <a href='https://phoenixnap.com/kb/bmc-custom-os' target='_blank'>instructions</a> on how to install custom OS on BMC. Only supported for ubuntu/focal and ubuntu/jammy.", alias="installOsToRam")
    cloud_init: Optional[OsConfigurationCloudInit] = Field(default=None, alias="cloudInit")
    __properties: ClassVar[List[str]] = ["netrisController", "netrisSoftgate", "windows", "rootPassword", "managementUiUrl", "managementAccessAllowedIps", "installOsToRam", "cloudInit"]

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
        """Create an instance of OsConfiguration from a JSON string"""
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
                "root_password",
                "management_ui_url",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of netris_controller
        if self.netris_controller:
            _dict['netrisController'] = self.netris_controller.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netris_softgate
        if self.netris_softgate:
            _dict['netrisSoftgate'] = self.netris_softgate.to_dict()
        # override the default output from pydantic by calling `to_dict()` of windows
        if self.windows:
            _dict['windows'] = self.windows.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_init
        if self.cloud_init:
            _dict['cloudInit'] = self.cloud_init.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of OsConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "netrisController": OsConfigurationNetrisController.from_dict(obj.get("netrisController")) if obj.get("netrisController") is not None else None,
            "netrisSoftgate": OsConfigurationNetrisSoftgate.from_dict(obj.get("netrisSoftgate")) if obj.get("netrisSoftgate") is not None else None,
            "windows": OsConfigurationWindows.from_dict(obj.get("windows")) if obj.get("windows") is not None else None,
            "rootPassword": obj.get("rootPassword"),
            "managementUiUrl": obj.get("managementUiUrl"),
            "managementAccessAllowedIps": obj.get("managementAccessAllowedIps"),
            "installOsToRam": obj.get("installOsToRam") if obj.get("installOsToRam") is not None else False,
            "cloudInit": OsConfigurationCloudInit.from_dict(obj.get("cloudInit")) if obj.get("cloudInit") is not None else None
        })
        return _obj

