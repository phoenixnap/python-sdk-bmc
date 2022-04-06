"""
    Bare Metal Cloud API

    Create, power off, power on, reset, reboot, or shut down your server with the Bare Metal Cloud API. Deprovision servers, get or edit SSH key details, and a lot more. Manage your infrastructure more efficiently using just a few simple api calls.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/how-to-deploy-bare-metal-cloud-server' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/bmc/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 0.1
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pnap_bmc_api
from pnap_bmc_api.model.server_patch import ServerPatch


class TestServerPatch(unittest.TestCase):
    """ServerPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testServerPatch(self):
        """Test ServerPatch"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ServerPatch()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
