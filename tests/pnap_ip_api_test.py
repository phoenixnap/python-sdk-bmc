import unittest
import xmlrunner
from dateutil.parser import parse

from test_utils import TestUtils

import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.models.ip_block_create import IpBlockCreate
from pnap_ip_api.models.ip_block_patch import IpBlockPatch
from pnap_ip_api.models.tag_assignment_request import TagAssignmentRequest

class TestIpApi(unittest.TestCase):
   configuration = pnap_ip_api.Configuration(host = "127.0.0.1:1080/ips/v1")
   api_client = pnap_ip_api.ApiClient(configuration)

   def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)


   def test_get_ip_blocks(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ip_blocks_api.IPBlocksApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    result = api_instance.ip_blocks_get(tag=[opts['tag']])

    response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])

    self.assertEqual(response['body'][0], result[0].to_dict())

    self.verify_called_once(expectation_id)

   def test_create_ip_block(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_post')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = ip_blocks_api.IPBlocksApi(self.api_client)

      ip_block_create_dict = TestUtils.extract_request_body(request)
      ip_block_create_dict['tags'] = [TagAssignmentRequest(**ip_block_create_dict['tags'][0])]
      ip_block_create =  IpBlockCreate(**ip_block_create_dict, _spec_property_naming=True)

      result = api_instance.ip_blocks_post(ip_block_create=ip_block_create)

      response['body']['createdOn'] = parse(response['body']['createdOn'])

      self.assertEqual(response['body'], result.to_dict())

      self.verify_called_once(expectation_id)

   def test_get_ip_block_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = ip_blocks_api.IPBlocksApi(self.api_client)
    ip_block_id = TestUtils.extract_id_from(request)

    result = api_instance.ip_blocks_ip_block_id_get(ip_block_id)

    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation_id)

   def test_patch_ip_block_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_patch_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = ip_blocks_api.IPBlocksApi(self.api_client)
    ip_block_id = TestUtils.extract_id_from(request)
    
    ip_block_patch = IpBlockPatch(**TestUtils.extract_request_body(request))
    
    result = api_instance.ip_blocks_ip_block_id_patch(ip_block_id, ip_block_patch=ip_block_patch)

    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation_id)

   def test_delete_ip_block_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_delete_by_id')
    expectation = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ip_blocks_api.IPBlocksApi(self.api_client)
    ip_block_id = TestUtils.extract_id_from(request)

    result = api_instance.ip_blocks_ip_block_id_delete(ip_block_id)

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation)

   def test_ip_block_put_tags_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('ipapi/ip_blocks_put_tags_by_id')
    expectation = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ip_blocks_api.IPBlocksApi(self.api_client)
    ip_block_id = TestUtils.extract_id_from(request)
    tag_assignment_request = [TagAssignmentRequest(**TestUtils.extract_request_body(request)[0])]

    result = api_instance.ip_blocks_ip_block_id_tags_put(ip_block_id, tag_assignment_request=tag_assignment_request)

    # Parsing time for comparison
    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation)

   def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
   TestUtils.reset_mockserver()
   unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
      failfast=False, buffer=False, catchbreak=False)
