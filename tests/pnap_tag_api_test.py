import unittest
import xmlrunner

from test_utils import TestUtils

import pnap_tag_api
from pnap_tag_api.api import tags_api
from pnap_tag_api.model.tag_create import TagCreate
from pnap_tag_api.model.tag_update import TagUpdate
from pnap_tag_api.model_utils import model_to_dict

class TestTagApi(unittest.TestCase):
   configuration = pnap_tag_api.Configuration(host = "127.0.0.1:1080/tag-manager/v1")
   api_client = pnap_tag_api.ApiClient(configuration)

   def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)


   def test_get_tags(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('tagapi/tags_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = tags_api.TagsApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    result = api_instance.tags_get(**opts)

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

   def test_create_tag(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('tagapi/tags_post')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = tags_api.TagsApi(self.api_client)
    tag_create = TagCreate(**TestUtils.extract_request_body(request), _spec_property_naming=True)

    result = api_instance.tags_post(tag_create)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_get_tag_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('tagapi/tags_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = tags_api.TagsApi(self.api_client)
    tag_id = TestUtils.extract_id_from(request)

    result = api_instance.tags_tag_id_get(tag_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_patch_tag_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('tagapi/tags_patch_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = tags_api.TagsApi(self.api_client)
    tag_id = TestUtils.extract_id_from(request)
    tag_update = TagUpdate(**TestUtils.extract_request_body(request), _spec_property_naming=True)

    result = api_instance.tags_tag_id_patch(tag_id, tag_update)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_delete_tag_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('tagapi/tags_delete_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = tags_api.TagsApi(self.api_client)
    tag_id = TestUtils.extract_id_from(request)

    result = api_instance.tags_tag_id_delete(tag_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once (expectation_id)

   def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False)
