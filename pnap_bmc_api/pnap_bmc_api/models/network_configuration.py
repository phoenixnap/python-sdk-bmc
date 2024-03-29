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
from pnap_bmc_api.models.ip_blocks_configuration import IpBlocksConfiguration
from pnap_bmc_api.models.private_network_configuration import PrivateNetworkConfiguration
from pnap_bmc_api.models.public_network_configuration import PublicNetworkConfiguration
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NetworkConfiguration(BaseModel):
    """
    Entire network details of bare metal server.
    """ # noqa: E501
    gateway_address: Optional[StrictStr] = Field(default=None, description="The address of the gateway assigned / to assign to the server.<br> When used as part of request body, IP address has to be part of a private/public network or an IP block assigned to this server.<br> Gateway address also has to be assigned on an already deployed resource unless the address matches the BMC gateway address in a public network/IP block or the `force` query parameter is true.", alias="gatewayAddress")
    private_network_configuration: Optional[PrivateNetworkConfiguration] = Field(default=None, alias="privateNetworkConfiguration")
    ip_blocks_configuration: Optional[IpBlocksConfiguration] = Field(default=None, alias="ipBlocksConfiguration")
    public_network_configuration: Optional[PublicNetworkConfiguration] = Field(default=None, alias="publicNetworkConfiguration")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["gatewayAddress", "privateNetworkConfiguration", "ipBlocksConfiguration", "publicNetworkConfiguration"]

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
        """Create an instance of NetworkConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of private_network_configuration
        if self.private_network_configuration:
            _dict['privateNetworkConfiguration'] = self.private_network_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ip_blocks_configuration
        if self.ip_blocks_configuration:
            _dict['ipBlocksConfiguration'] = self.ip_blocks_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_network_configuration
        if self.public_network_configuration:
            _dict['publicNetworkConfiguration'] = self.public_network_configuration.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NetworkConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "gatewayAddress": obj.get("gatewayAddress"),
            "privateNetworkConfiguration": PrivateNetworkConfiguration.from_dict(obj.get("privateNetworkConfiguration")) if obj.get("privateNetworkConfiguration") is not None else None,
            "ipBlocksConfiguration": IpBlocksConfiguration.from_dict(obj.get("ipBlocksConfiguration")) if obj.get("ipBlocksConfiguration") is not None else None,
            "publicNetworkConfiguration": PublicNetworkConfiguration.from_dict(obj.get("publicNetworkConfiguration")) if obj.get("publicNetworkConfiguration") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


