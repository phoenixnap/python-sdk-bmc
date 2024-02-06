import unittest

import xmlrunner
import pnap_audit_api
from test_utils import TestUtils
from pnap_audit_api.api import events_api
from dateutil.parser import parse

class  TestMisc(unittest.TestCase):
  configuration = pnap_audit_api.Configuration(host = "127.0.0.1:1080/audit/v1")
  api_client = pnap_audit_api.ApiClient(configuration)

def test_get_events_all_additional_properties(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('auditapi/events_get_additional_properties')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = events_api.EventsApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    # Changing key from `_from` to 'from'
    opts['var_from'] = opts.pop('from')
    opts['limit'] = int(opts['limit'])
    
    result = api_instance.events_get(**opts)
    print(result)

    # Parsing time for comparison
    response['body'][0]['timestamp'] = parse(response['body'][0]['timestamp'])

    self.assertEqual(response['body'][0], result[0].to_dict())

    self.verify_called_once(expectation_id)

if __name__ == '__main__':
  unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    failfast=False, buffer=False, catchbreak=False)