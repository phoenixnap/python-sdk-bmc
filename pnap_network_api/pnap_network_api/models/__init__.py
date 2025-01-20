# coding: utf-8

# flake8: noqa
"""
    Networks API

    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.<br> <br> <span class='pnap-api-knowledge-base-link'> Helpful knowledge base articles are available for  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>multi-private backend networks</a>,  <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-15' target='_blank'>public networks</a> and <a href='https://phoenixnap.com/kb/border-gateway-protocol-bmc' target='_blank'>border gateway protocol peer groups</a>. </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from pnap_network_api.models.asn_details import AsnDetails
from pnap_network_api.models.bgp_ipv4_prefix import BgpIPv4Prefix
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
from pnap_network_api.models.bgp_peer_group_create import BgpPeerGroupCreate
from pnap_network_api.models.bgp_peer_group_patch import BgpPeerGroupPatch
from pnap_network_api.models.error import Error
from pnap_network_api.models.network_membership import NetworkMembership
from pnap_network_api.models.private_network import PrivateNetwork
from pnap_network_api.models.private_network_create import PrivateNetworkCreate
from pnap_network_api.models.private_network_modify import PrivateNetworkModify
from pnap_network_api.models.private_network_server import PrivateNetworkServer
from pnap_network_api.models.public_network import PublicNetwork
from pnap_network_api.models.public_network_create import PublicNetworkCreate
from pnap_network_api.models.public_network_ip_block import PublicNetworkIpBlock
from pnap_network_api.models.public_network_ip_block_create import PublicNetworkIpBlockCreate
from pnap_network_api.models.public_network_modify import PublicNetworkModify
