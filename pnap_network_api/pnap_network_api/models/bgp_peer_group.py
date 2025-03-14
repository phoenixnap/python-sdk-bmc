# coding: utf-8

"""
    Networks API

    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.<br> <br> <span class='pnap-api-knowledge-base-link'> Helpful knowledge base articles are available for  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>multi-private backend networks</a>,  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-15' target='_blank'>public networks</a> and <a href='https://phoenixnap.com/kb/border-gateway-protocol-bmc' target='_blank'>border gateway protocol peer groups</a>. </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b> 

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
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from pnap_network_api.models.asn_details import AsnDetails
from pnap_network_api.models.bgp_ipv4_prefix import BgpIPv4Prefix
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class BgpPeerGroup(BaseModel):
    """
    The Border Gateway Protocol (BGP) Peer Group.
    """ # noqa: E501
    id: StrictStr = Field(description="The unique identifier of the BGP Peer Group.")
    status: StrictStr = Field(description="The BGP Peer Group status. Can have one of the following values: `PENDING`, `ON_HOLD`, `BUSY`, `READY`, `ERROR`, `PENDING_DELETION` and `DELETING`.")
    location: StrictStr = Field(description="The BGP Peer Group location. Can have one of the following values: `PHX`, `ASH`, `SGP`, `NLD`, `CHI`, `SEA` and `AUS`.")
    ipv4_prefixes: List[BgpIPv4Prefix] = Field(description="The List of the BGP Peer Group IPv4 prefixes.", alias="ipv4Prefixes")
    target_asn_details: AsnDetails = Field(alias="targetAsnDetails")
    active_asn_details: Optional[AsnDetails] = Field(default=None, alias="activeAsnDetails")
    password: Annotated[str, Field(min_length=8, strict=True, max_length=32)] = Field(description="The BGP Peer Group password.")
    advertised_routes: StrictStr = Field(description="The Advertised routes for the BGP Peer Group. Can have one of the following values: `DEFAULT` and `NONE`.", alias="advertisedRoutes")
    rpki_roa_origin_asn: StrictInt = Field(description="The RPKI ROA Origin ASN of the BGP Peer Group based on location.", alias="rpkiRoaOriginAsn")
    e_bgp_multi_hop: StrictInt = Field(description="The eBGP Multi-hop of the BGP Peer Group.", alias="eBgpMultiHop")
    peering_loopbacks_v4: List[Annotated[str, Field(strict=True)]] = Field(description="The IPv4 Peering Loopback addresses of the BGP Peer Group. Valid IP formats are IPv4 addresses.", alias="peeringLoopbacksV4")
    keep_alive_timer_seconds: StrictInt = Field(description="The Keep Alive Timer in seconds of the BGP Peer Group.", alias="keepAliveTimerSeconds")
    hold_timer_seconds: StrictInt = Field(description="The Hold Timer in seconds of the BGP Peer Group.", alias="holdTimerSeconds")
    created_on: Optional[StrictStr] = Field(default=None, description="Date and time of creation.", alias="createdOn")
    last_updated_on: Optional[StrictStr] = Field(default=None, description="Date and time of last update.", alias="lastUpdatedOn")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "location", "ipv4Prefixes", "targetAsnDetails", "activeAsnDetails", "password", "advertisedRoutes", "rpkiRoaOriginAsn", "eBgpMultiHop", "peeringLoopbacksV4", "keepAliveTimerSeconds", "holdTimerSeconds", "createdOn", "lastUpdatedOn"]

    @field_validator('password')
    def password_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z0-9!@#$%^&*()\-|\[\]{}=;:<>,.]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9!@#$%^&*()\-|\[\]{}=;:<>,.]+$/")
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
        """Create an instance of BgpPeerGroup from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in ipv4_prefixes (list)
        _items = []
        if self.ipv4_prefixes:
            for _item in self.ipv4_prefixes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ipv4Prefixes'] = _items
        # override the default output from pydantic by calling `to_dict()` of target_asn_details
        if self.target_asn_details:
            _dict['targetAsnDetails'] = self.target_asn_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of active_asn_details
        if self.active_asn_details:
            _dict['activeAsnDetails'] = self.active_asn_details.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of BgpPeerGroup from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "location": obj.get("location"),
            "ipv4Prefixes": [BgpIPv4Prefix.from_dict(_item) for _item in obj.get("ipv4Prefixes")] if obj.get("ipv4Prefixes") is not None else None,
            "targetAsnDetails": AsnDetails.from_dict(obj.get("targetAsnDetails")) if obj.get("targetAsnDetails") is not None else None,
            "activeAsnDetails": AsnDetails.from_dict(obj.get("activeAsnDetails")) if obj.get("activeAsnDetails") is not None else None,
            "password": obj.get("password"),
            "advertisedRoutes": obj.get("advertisedRoutes"),
            "rpkiRoaOriginAsn": obj.get("rpkiRoaOriginAsn"),
            "eBgpMultiHop": obj.get("eBgpMultiHop"),
            "peeringLoopbacksV4": obj.get("peeringLoopbacksV4"),
            "keepAliveTimerSeconds": obj.get("keepAliveTimerSeconds"),
            "holdTimerSeconds": obj.get("holdTimerSeconds"),
            "createdOn": obj.get("createdOn"),
            "lastUpdatedOn": obj.get("lastUpdatedOn")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


