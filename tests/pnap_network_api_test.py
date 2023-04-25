import unittest
import xmlrunner
from dateutil.parser import parse

from test_utils import TestUtils

import pnap_network_api
from pnap_network_api.api import private_networks_api
from pnap_network_api.api import public_networks_api
from pnap_network_api.model.private_network_create import PrivateNetworkCreate
from pnap_network_api.model.private_network_modify import PrivateNetworkModify
from pnap_network_api.model.public_network_create import PublicNetworkCreate
from pnap_network_api.model.public_network_modify import PublicNetworkModify
from pnap_network_api.model.public_network_ip_block import PublicNetworkIpBlock
from pnap_network_api.model_utils import model_to_dict

class TestNetworkApi(unittest.TestCase):
   configuration = pnap_network_api.Configuration(host = "127.0.0.1:1080/networks/v1")
   api_client = pnap_network_api.ApiClient(configuration)

   def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)


   def test_get_private_networks(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('networkapi/private_networks_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = private_networks_api.PrivateNetworksApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    result = api_instance.private_networks_get(**opts)

    response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

   def test_create_private_network(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('networkapi/private_networks_post')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = private_networks_api.PrivateNetworksApi(self.api_client)
    private_network_create = PrivateNetworkCreate(**TestUtils.extract_request_body(request))
    opts = TestUtils.generate_query_params(request)

    result = api_instance.private_networks_post(force=opts['force'] == "true", private_network_create=private_network_create)

    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_get_private_network_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('networkapi/private_networks_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = private_networks_api.PrivateNetworksApi(self.api_client)
    network_id = TestUtils.extract_id_from(request)

    result = api_instance.private_networks_network_id_get(network_id)

    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_put_private_network_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('networkapi/private_networks_put_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)

    api_instance = private_networks_api.PrivateNetworksApi(self.api_client)
    network_id = TestUtils.extract_id_from(request)
    private_network_modify = PrivateNetworkModify(**TestUtils.extract_request_body(request), _spec_property_naming=True)

    result = api_instance.private_networks_network_id_put(network_id, private_network_modify=private_network_modify)

    response['body']['createdOn'] = parse(response['body']['createdOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

   def test_delete_private_network_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('networkapi/private_networks_delete_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = private_networks_api.PrivateNetworksApi(self.api_client)
    network_id = TestUtils.extract_id_from(request)

    api_instance.private_networks_network_id_delete(network_id)

    self.verify_called_once(expectation_id)

   def test_get_public_networks(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_get')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      opts = TestUtils.generate_query_params(request)

      result = api_instance.public_networks_get(**opts)

      response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])

      self.assertEqual(response['body'][0], model_to_dict(result[0]))

      self.verify_called_once(expectation_id)

   def test_create_public_network(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_post')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      public_network_create = PublicNetworkCreate(**TestUtils.extract_request_body(request))

      result = api_instance.public_networks_post(public_network_create=public_network_create)

      response['body']['createdOn'] = parse(response['body']['createdOn'])

      self.assertEqual(response['body'], model_to_dict(result))

      self.verify_called_once(expectation_id)

   def test_delete_public_network_by_id(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_delete_by_id')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      network_id = TestUtils.extract_id_from(request)

      api_instance.public_networks_network_id_delete(network_id)

      self.verify_called_once(expectation_id)

   def test_get_public_network_by_id(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_get_by_id')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      network_id = TestUtils.extract_id_from(request)

      result = api_instance.public_networks_network_id_get(network_id)

      response['body']['createdOn'] = parse(response['body']['createdOn'])

      self.assertEqual(response['body'], model_to_dict(result))

      self.verify_called_once(expectation_id)

   def test_public_network_delete_ip_block_by_id(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_delete_ip_block_by_id')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      network_id = TestUtils.extract_id_from(request, "networkId")
      ip_id = TestUtils.extract_id_from(request, "ipId")
      opts = TestUtils.generate_query_params(request)['force']

      api_instance.public_networks_network_id_ip_blocks_ip_block_id_delete(network_id, ip_id, force=bool(opts))

      self.verify_called_once(expectation_id)
      pass

   def test_public_network_create_ip_block(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_post_ip_block')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      network_id = TestUtils.extract_id_from(request)
      public_network_ip_block = PublicNetworkIpBlock(**TestUtils.extract_request_body(request))

      result = api_instance.public_networks_network_id_ip_blocks_post(network_id, public_network_ip_block=public_network_ip_block)

      self.assertEqual(response['body'], model_to_dict(result))

      self.verify_called_once(expectation_id)

   def test_patch_public_network_by_id(self):
      # Setting up expectation
      request, response = TestUtils.generate_payloads_from('networkapi/public_networks_patch_by_id')
      expectation_id = TestUtils.setup_expectation(request, response, 1)
      
      api_instance = public_networks_api.PublicNetworksApi(self.api_client)
      network_id = TestUtils.extract_id_from(request)
      public_network_modify = PublicNetworkModify(**TestUtils.extract_request_body(request))

      result = api_instance.public_networks_network_id_patch(network_id, public_network_modify=public_network_modify)

      response['body']['createdOn'] = parse(response['body']['createdOn'])

      self.assertEqual(response['body'], model_to_dict(result))

      self.verify_called_once(expectation_id)

   

   def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
   TestUtils.reset_mockserver()
   unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
      failfast=False, buffer=False, catchbreak=False)
