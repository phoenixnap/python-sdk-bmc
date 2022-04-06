"""
    Audit Log API

    The Audit Logs API lets you read audit log entries and track API calls or activities in the Bare Metal Cloud Portal.<br> <br> <span class='pnap-api-knowledge-base-link'> Knowledge base articles to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#audit-log-api' target='_blank'>here</a> </span><br> <br> <b>All URLs are relative to (https://api.phoenixnap.com/audit/v1/)</b>   # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: support@phoenixnap.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pnap_audit_api
from pnap_audit_api.model.api_action_all_of import ApiActionAllOf
from pnap_audit_api.model.event import Event
from pnap_audit_api.model.request import Request
from pnap_audit_api.model.response import Response
from pnap_audit_api.model.user_info import UserInfo
globals()['ApiActionAllOf'] = ApiActionAllOf
globals()['Event'] = Event
globals()['Request'] = Request
globals()['Response'] = Response
globals()['UserInfo'] = UserInfo
from pnap_audit_api.model.api_action import ApiAction


class TestApiAction(unittest.TestCase):
    """ApiAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApiAction(self):
        """Test ApiAction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApiAction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
