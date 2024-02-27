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

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from pnap_bmc_api.models.network_configuration import NetworkConfiguration
from pnap_bmc_api.models.os_configuration import OsConfiguration
from pnap_bmc_api.models.storage_configuration import StorageConfiguration
from pnap_bmc_api.models.tag_assignment import TagAssignment
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Server(BaseModel):
    """
    Bare metal server.
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the server.")
    status: StrictStr = Field(description="The status of the server. Can have one of the following values: `creating` , `powered-on` , `powered-off` , `rebooting` , `resetting` , `deleting` , `reserved` , `error` or `reinstating`.")
    hostname: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(description="Hostname of server.")
    description: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Description of server.")
    os: Optional[StrictStr] = Field(default=None, description="The server’s OS ID used when the server was created. Currently this field should be set to either `ubuntu/bionic`, `ubuntu/focal`, `ubuntu/jammy`, `centos/centos7`, `centos/centos8`, `windows/srv2019std`, `windows/srv2019dc`, `windows/srv2022std`, `windows/srv2022dc`, `esxi/esxi70`, `esxi/esxi80`, `almalinux/almalinux8`, `rockylinux/rockylinux8`, `almalinux/almalinux9`, `rockylinux/rockylinux9`, `debian/bullseye`, `debian/bookworm`, `proxmox/bullseye`, `proxmox/proxmox8`, `netris/controller`, `netris/softgate_1g`, `netris/softgate_10g` or `netris/softgate_25g`.")
    type: StrictStr = Field(description="Server type ID. Cannot be changed once a server is created. Currently this field should be set to either `s0.d1.small`, `s0.d1.medium`, `s1.c1.small`, `s1.c1.medium`, `s1.c2.medium`, `s1.c2.large`, `s1.e1.small`, `s1.e1.medium`, `s1.e1.large`, `s2.c1.small`, `s2.c1.medium`, `s2.c1.large`, `s2.c2.small`, `s2.c2.medium`, `s2.c2.large`, `d1.c1.small`, `d1.c2.small`, `d1.c3.small`, `d1.c4.small`, `d1.c1.medium`, `d1.c2.medium`, `d1.c3.medium`, `d1.c4.medium`, `d1.c1.large`, `d1.c2.large`, `d1.c3.large`, `d1.c4.large`, `d1.m1.medium`, `d1.m2.medium`, `d1.m3.medium`, `d1.m4.medium`, `d2.c1.medium`, `d2.c2.medium`, `d2.c3.medium`, `d2.c4.medium`, `d2.c5.medium`, `d2.c1.large`, `d2.c2.large`, `d2.c3.large`, `d2.c4.large`, `d2.c5.large`, `d2.m1.xlarge`, `d2.m2.xxlarge`, `d2.m3.xlarge`, `d2.m4.xlarge`, `d2.m5.xlarge`, `d2.c4.db1.pliops1`, `d3.m4.xlarge`, `d3.m5.xlarge`, `d3.m6.xlarge`, `a1.c5.large`, `d3.s5.xlarge`, `d3.m4.xxlarge`, `d3.m5.xxlarge`,  `d3.m6.xxlarge`, `s3.c3.medium`, `s3.c3.large`, `d3.c4.medium`, `d3.c5.medium` or `d3.c6.medium`.")
    location: StrictStr = Field(description="Server location ID. Cannot be changed once a server is created. Currently this field should be set to `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` or `AUS`.")
    cpu: StrictStr = Field(description="A description of the machine CPU.")
    cpu_count: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of CPUs available in the system.", alias="cpuCount")
    cores_per_cpu: Annotated[int, Field(strict=True, ge=1)] = Field(description="The number of physical cores present on each CPU.", alias="coresPerCpu")
    cpu_frequency: Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]] = Field(description="The CPU frequency in GHz.", alias="cpuFrequency")
    ram: StrictStr = Field(description="A description of the machine RAM.")
    storage: StrictStr = Field(description="A description of the machine storage.")
    private_ip_addresses: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="Private IP addresses assigned to server.", alias="privateIpAddresses")
    public_ip_addresses: Optional[Annotated[List[StrictStr], Field(min_length=0)]] = Field(default=None, description="Public IP addresses assigned to server.", alias="publicIpAddresses")
    reservation_id: Optional[StrictStr] = Field(default=None, description="The reservation reference id if any.", alias="reservationId")
    pricing_model: StrictStr = Field(description="The pricing model this server is being billed. Currently this field should be set to `HOURLY`, `ONE_MONTH_RESERVATION`, `TWELVE_MONTHS_RESERVATION`, `TWENTY_FOUR_MONTHS_RESERVATION` or `THIRTY_SIX_MONTHS_RESERVATION`.", alias="pricingModel")
    password: Optional[StrictStr] = Field(default=None, description="Auto-generated password set for user `Admin` on Windows server, user `root` on ESXi servers, user `root` on Proxmox server and user `netris` on Netris servers.<br> The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference.")
    network_type: Optional[StrictStr] = Field(default='PUBLIC_AND_PRIVATE', description="The type of network configuration for this server. Currently this field should be set to `PUBLIC_AND_PRIVATE`, `PRIVATE_ONLY`, `PUBLIC_ONLY` or `NONE`.", alias="networkType")
    cluster_id: Optional[StrictStr] = Field(default=None, description="The cluster reference id if any.", alias="clusterId")
    tags: Optional[List[TagAssignment]] = Field(default=None, description="The tags assigned if any.")
    provisioned_on: Optional[datetime] = Field(default=None, description="Date and time when server was provisioned.", alias="provisionedOn")
    os_configuration: Optional[OsConfiguration] = Field(default=None, alias="osConfiguration")
    network_configuration: NetworkConfiguration = Field(alias="networkConfiguration")
    storage_configuration: StorageConfiguration = Field(alias="storageConfiguration")
    superseded_by: Optional[StrictStr] = Field(default=None, description="Unique identifier of the server to which the reservation has been transferred.", alias="supersededBy")
    supersedes: Optional[StrictStr] = Field(default=None, description="Unique identifier of the server from which the reservation has been transferred.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "hostname", "description", "os", "type", "location", "cpu", "cpuCount", "coresPerCpu", "cpuFrequency", "ram", "storage", "privateIpAddresses", "publicIpAddresses", "reservationId", "pricingModel", "password", "networkType", "clusterId", "tags", "provisionedOn", "osConfiguration", "networkConfiguration", "storageConfiguration", "supersededBy", "supersedes"]

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
        """Create an instance of Server from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of os_configuration
        if self.os_configuration:
            _dict['osConfiguration'] = self.os_configuration.to_dict()
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
        """Create an instance of Server from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "hostname": obj.get("hostname"),
            "description": obj.get("description"),
            "os": obj.get("os"),
            "type": obj.get("type"),
            "location": obj.get("location"),
            "cpu": obj.get("cpu"),
            "cpuCount": obj.get("cpuCount"),
            "coresPerCpu": obj.get("coresPerCpu"),
            "cpuFrequency": obj.get("cpuFrequency"),
            "ram": obj.get("ram"),
            "storage": obj.get("storage"),
            "privateIpAddresses": obj.get("privateIpAddresses"),
            "publicIpAddresses": obj.get("publicIpAddresses"),
            "reservationId": obj.get("reservationId"),
            "pricingModel": obj.get("pricingModel") if obj.get("pricingModel") is not None else 'HOURLY',
            "password": obj.get("password"),
            "networkType": obj.get("networkType") if obj.get("networkType") is not None else 'PUBLIC_AND_PRIVATE',
            "clusterId": obj.get("clusterId"),
            "tags": [TagAssignment.from_dict(_item) for _item in obj.get("tags")] if obj.get("tags") is not None else None,
            "provisionedOn": obj.get("provisionedOn"),
            "osConfiguration": OsConfiguration.from_dict(obj.get("osConfiguration")) if obj.get("osConfiguration") is not None else None,
            "networkConfiguration": NetworkConfiguration.from_dict(obj.get("networkConfiguration")) if obj.get("networkConfiguration") is not None else None,
            "storageConfiguration": StorageConfiguration.from_dict(obj.get("storageConfiguration")) if obj.get("storageConfiguration") is not None else None,
            "supersededBy": obj.get("supersededBy"),
            "supersedes": obj.get("supersedes")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


