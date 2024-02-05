import unittest
import xmlrunner
from test_utils import TestUtils
from dateutil.parser import parse

import pnap_invoicing_api
from pnap_invoicing_api.models.paginated_invoices import PaginatedInvoices
from pnap_invoicing_api.models.invoice import Invoice

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
        opts['sent_on_from'] = opts.pop('sentOnFrom')
        opts['sent_on_to'] = opts.pop('sentOnTo')
        opts['sort_direction'] = opts.pop('sortDirection')
        opts['sort_field'] = opts.pop('sortField')

        result = api_instance.invoices_get(**opts)

        result_dict = PaginatedInvoices.from_dict(result)
        response_dict = PaginatedInvoices.from_dict(response['body'])

        self.assertEqual(response_dict, result_dict)

        self.verify_called_once(expectation_id)

    def test_get_invoice_by_id(self):
		# Setting up expectation
        request, response = TestUtils.generate_payloads_from('invoicing/invoices_get_by_id')
        expectation_id = TestUtils.setup_expectation(request, response, 1)
        api_instance = pnap_invoicing_api.InvoicesApi(self.api_client)

        invoice_id = TestUtils.extract_id_from(request, "id")

        result = api_instance.invoices_invoice_id_get(invoice_id)

        result_dict = Invoice.from_dict(result)
        response_dict = Invoice.from_dict(response['body'])

        self.assertEqual(response_dict, result_dict)

        self.verify_called_once(expectation_id)

    def test_invoices_invoice_id_pay_post(self):
		# Setting up expectation
        request, response = TestUtils.generate_payloads_from('invoicing/invoices_pay_post')
        expectation_id = TestUtils.setup_expectation(request, response, 1)
        api_instance = pnap_invoicing_api.InvoicesApi(self.api_client)

        invoice_id = TestUtils.extract_id_from(request, "id")

        result = api_instance.invoices_invoice_id_pay_post(invoice_id)

        self.assertEqual(result, response['body'])

        self.verify_called_once(expectation_id)

    def test_invoices_igenerate_pdf_post(self):
		# Setting up expectation
        request, response = TestUtils.generate_payloads_from('invoicing/invoices_generate_pdf_post')
        expectation_id = TestUtils.setup_expectation(request, response, 1)
        api_instance = pnap_invoicing_api.InvoicesApi(self.api_client)

        invoice_id = TestUtils.extract_id_from(request, "id")

        result = api_instance.invoices_invoice_id_generate_pdf_post(invoice_id)

        self.verify_called_once(expectation_id)

if __name__ == '__main__':
	TestUtils.reset_mockserver()
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		failfast=False, buffer=False, catchbreak=False)