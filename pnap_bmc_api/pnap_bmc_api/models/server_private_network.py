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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ServerPrivateNetwork(BaseModel):
    """
    Private network details of bare metal server.
    """ # noqa: E501
    id: StrictStr = Field(description="The network identifier.")
    ips: Optional[Annotated[List[StrictStr], Field(max_length=256)]] = Field(default=None, description="IPs to configure/configured on the server.<br> Valid IP formats are single IPv4 addresses or IPv4 ranges. IPs must be within the network's range. Should be null or empty list if DHCP is true. <br> If field is undefined and DHCP is false, next available IP in network will be automatically allocated.<br> If the network contains a membership of type 'storage', the first twelve IPs are already reserved by BMC and not usable.<br> Setting the `force` query parameter to `true` allows you to:<ul> <li> Assign no specific IP addresses by designating an empty array of IPs. Note that at least one IP is required for the gateway address to be selected from this network. <li> Assign one or more IP addresses which are already configured on other resource(s) in network. <li> Assign IP addresses which are considered as reserved in network.</ul>")
    dhcp: Optional[StrictBool] = Field(default=False, description="Determines whether DHCP is enabled for this server. Should be false if any IPs are provided. Not supported for Proxmox OS.")
    status_description: Optional[StrictStr] = Field(default=None, description="(Read-only) The status of the network.", alias="statusDescription")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "ips", "dhcp", "statusDescription"]

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
        """Create an instance of ServerPrivateNetwork from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "status_description",
                "additional_properties",
            },
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ServerPrivateNetwork from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ips": obj.get("ips"),
            "dhcp": obj.get("dhcp") if obj.get("dhcp") is not None else False,
            "statusDescription": obj.get("statusDescription")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


