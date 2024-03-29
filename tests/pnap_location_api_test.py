import unittest
import xmlrunner
from dateutil.parser import parse
import pnap_location_api
from pnap_location_api.api import locations_api
from pnap_location_api.models.location_enum import LocationEnum
from pnap_location_api.models.product_category_enum import ProductCategoryEnum
from test_utils import TestUtils


class TestLocationApi(unittest.TestCase):
    configuration = pnap_location_api.Configuration(host = "127.0.0.1:1080/location-api/v1")
    api_client = pnap_location_api.ApiClient(configuration)

    def verify_called_once(self, expectation_id):
        # Result retrieved from server's verification
        # Verifying expectation matched exactly once.
        verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

        # Asserts a successful result.
        self.assertEqual(202, verifyResult.status_code)

    def test_get_locations(self):
        # Setting up expectation
        request, response = TestUtils.generate_payloads_from('locationapi/locations_get')
        expectation_id = TestUtils.setup_expectation(request, response, 1)

        # Creating new instance
        api_instance = locations_api.LocationsApi(self.api_client)
        opts = TestUtils.generate_query_params(request)

        # Changing values to be enums
        opts['location'] = LocationEnum(opts['location'])
        opts['product_category'] = ProductCategoryEnum(opts['productCategory'])
        del opts['productCategory']

        result = api_instance.get_locations(**opts)

        self.assertEqual(response['body'][0], result[0].to_dict())

        self.verify_called_once(expectation_id)

    def tearDown(self):
        TestUtils.reset_expectations()
        self.api_client.close()

if __name__ == '__main__':
    TestUtils.reset_mockserver()
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False)