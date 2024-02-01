import unittest
from dateutil.parser import parse
import xmlrunner

import pnap_payments_api
from pnap_payments_api.models.transaction import Transaction
from test_utils import TestUtils

class TestLocationApi(unittest.TestCase):
    configuration = pnap_payments_api.Configuration(host = "127.0.0.1:1080/payments/v1")
    api_client = pnap_payments_api.ApiClient(configuration)

    def verify_called_once(self, expectation_id):
        # Result retrieved from server's verification
        # Verifying expectation matched exactly once.
        verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

        # Asserts a successful result.
        self.assertEqual(202, verifyResult.status_code)

    def tearDown(self):
        TestUtils.reset_expectations()
        self.api_client.close()

    def test_get_transactions(self):
        # Setting up expectation
        request, response = TestUtils.generate_payloads_from('paymentsapi/transactions_get')
        expectation_id = TestUtils.setup_expectation(request, response, 1)

        # Creating new instance
        api_instance = pnap_payments_api.TransactionsApi(self.api_client)
        opts = TestUtils.generate_query_params(request)

        opts['limit'] = int(opts['limit'])
        opts['offset'] = int(opts['offset'])
        opts['sort_direction'] = opts.pop('sortDirection')
        opts['sort_field'] = opts.pop('sortField')
        opts['var_from'] = opts.pop('from')

        result = api_instance.transactions_get(**opts)

        response['body']['results'][0]['date'] = parse(response['body']['results'][0]['date'])

        self.assertEqual(response['body'], result.to_dict())

        self.verify_called_once(expectation_id)

    def test_get_transaction_by_id(self):
		# Setting up expectation
        request, response = TestUtils.generate_payloads_from('paymentsapi/transactions_get_by_id')
        expectation_id = TestUtils.setup_expectation(request, response, 1)
        api_instance = pnap_payments_api.TransactionsApi(self.api_client)

        transaction_id = TestUtils.extract_id_from(request, "id")

        result = api_instance.transaction_id_get(transaction_id)

        result_dict = Transaction.from_dict(result)
        response_dict = Transaction.from_dict(response['body'])

        self.assertEqual(response_dict, result_dict)

        self.verify_called_once(expectation_id)

if __name__ == '__main__':
	TestUtils.reset_mockserver()
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		failfast=False, buffer=False, catchbreak=False)