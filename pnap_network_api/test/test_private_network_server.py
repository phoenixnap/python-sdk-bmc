"""
    Networks API

    Use the Networks API to create, list, edit, and delete private networks to best fit your business needs. Private networks allow your servers to communicate without connecting to the public internet, avoiding unnecessary egress data charges.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#multi-private-backend-network-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/networks/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pnap_network_api
from pnap_network_api.model.private_network_server import PrivateNetworkServer


class TestPrivateNetworkServer(unittest.TestCase):
    """PrivateNetworkServer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrivateNetworkServer(self):
        """Test PrivateNetworkServer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PrivateNetworkServer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
