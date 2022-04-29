# flake8: noqa

"""
    Networks API

    Create, list, edit and delete public/private networks with the Network API. Use public networks to place multiple  servers on the same network or VLAN. Assign new servers with IP addresses from the same CIDR range. Use private  networks to avoid unnecessary egress data charges. Model your networks according to your business needs.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


# import ApiClient
from pnap_network_api.api_client import ApiClient

# import Configuration
from pnap_network_api.configuration import Configuration

# import exceptions
from pnap_network_api.exceptions import OpenApiException
from pnap_network_api.exceptions import ApiAttributeError
from pnap_network_api.exceptions import ApiTypeError
from pnap_network_api.exceptions import ApiValueError
from pnap_network_api.exceptions import ApiKeyError
from pnap_network_api.exceptions import ApiException
from pnap_network_api.version import VERSION


__version__ = VERSION