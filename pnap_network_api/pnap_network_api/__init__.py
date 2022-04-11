# flake8: noqa

"""
    Networks API

    Use the Networks API to create, list, edit, and delete private networks to best fit your business needs. Private networks allow your servers to communicate without connecting to the public internet, avoiding unnecessary egress data charges.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b>   # noqa: E501

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