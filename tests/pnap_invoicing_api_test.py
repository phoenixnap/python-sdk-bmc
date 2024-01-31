import unittest
import xmlrunner
from test_utils import TestUtils
from dateutil.parser import parse

import pnap_invoicing_api

class TestInvoicingApi(unittest.TestCase):
    configuration = pnap_invoicing_api.Configuration(host = "127.0.0.1:1080/invoicing/v1")
    api_client = pnap_invoicing_api.ApiClient(configuration)

    def verify_called_once(self, expectation_id):
        # Result retrieved from server's verification
        # Verifying expectation matched exactly once.
        verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

        # Asserts a successful result.
        self.assertEqual(202, verifyResult.status_code)

    def tearDown(self):
        TestUtils.reset_expectations()
        self.api_client.close()

    def test_get_invoices(self):
        # Setting up expectation
        request, response = TestUtils.generate_payloads_from('invoicing/invoices_get')

        expectation_id = TestUtils.setup_expectation(request, response, 1)

        api_instance = pnap_invoicing_api.InvoicesApi(self.api_client)

        opts = TestUtils.generate_query_params(request)

        opts['limit'] = int(opts['limit'])
        opts['offset'] = int(opts['offset'])

        print(response)

        result = api_instance.invoices_get(**opts)

        # response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])
        # response['body'][0]['volumes'][0]['createdOn'] = parse(response['body'][0]['volumes'][0]['createdOn'])

        # self.assertEqual(response['body'][0], result[0].to_dict())

        # self.verify_called_once(expectation_id)

if __name__ == '__main__':
	TestUtils.reset_mockserver()
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		failfast=False, buffer=False, catchbreak=False)