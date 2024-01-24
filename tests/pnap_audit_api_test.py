import unittest
import xmlrunner
from dateutil.parser import parse
from pnap_audit_api.pnap_audit_api.api.events_api import EventsApi
from pnap_audit_api.pnap_audit_api.model_utils import model_to_dict

from test_utils import TestUtils

import pnap_audit_api.pnap_audit_api

class  TestAuditApi(unittest.TestCase):
  configuration = pnap_audit_api.pnap_audit_api.Configuration(host = "127.0.0.1:1080/audit/v1")
  api_client = pnap_audit_api.pnap_audit_api.ApiClient(configuration)


  def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)

  def test_get_events_all_query_params(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('auditapi/events_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = EventsApi.EventsApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    # Changing key from `_from` to 'from'
    opts['_from'] = opts.pop('from')
    opts['limit'] = int(opts['limit'])
    
    result = api_instance.events_get(**opts)

    # Parsing time for comparison
    response['body'][0]['timestamp'] = parse(response['body'][0]['timestamp'])

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

  def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
  TestUtils.reset_mockserver()
  unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    failfast=False, buffer=False, catchbreak=False)