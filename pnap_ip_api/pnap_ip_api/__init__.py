# coding: utf-8

# flake8: noqa

"""
    IP Addresses API

    Public IP blocks are a set of contiguous IPs that allow you to access your servers or networks from the internet. Use the IP Addresses API to request and delete IP blocks.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/public-ip-management#bmc-public-ip-allocations-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/ips/v1/)</b> 

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "2.0.2"

# import apis into sdk package
from pnap_ip_api.api.ip_blocks_api import IPBlocksApi

# import ApiClient
from pnap_ip_api.api_response import ApiResponse
from pnap_ip_api.api_client import ApiClient
from pnap_ip_api.configuration import Configuration
from pnap_ip_api.exceptions import OpenApiException
from pnap_ip_api.exceptions import ApiTypeError
from pnap_ip_api.exceptions import ApiValueError
from pnap_ip_api.exceptions import ApiKeyError
from pnap_ip_api.exceptions import ApiAttributeError
from pnap_ip_api.exceptions import ApiException

# import models into sdk package
from pnap_ip_api.models.delete_ip_block_result import DeleteIpBlockResult
from pnap_ip_api.models.error import Error
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.models.ip_block_create import IpBlockCreate
from pnap_ip_api.models.ip_block_patch import IpBlockPatch
from pnap_ip_api.models.tag_assignment import TagAssignment
from pnap_ip_api.models.tag_assignment_request import TagAssignmentRequest
