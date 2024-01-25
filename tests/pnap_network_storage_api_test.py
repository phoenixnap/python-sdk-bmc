import unittest
import xmlrunner
from dateutil.parser import parse

from test_utils import TestUtils

import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.models.storage_network_create import StorageNetworkCreate
from pnap_network_storage_api.models.volume_create import VolumeCreate
from pnap_network_storage_api.models.storage_network_volume_create import StorageNetworkVolumeCreate
from pnap_network_storage_api.models.volume_update import VolumeUpdate
from pnap_network_storage_api.models.storage_network_update import StorageNetworkUpdate

class TestIpApi(unittest.TestCase):
	configuration = pnap_network_storage_api.Configuration(host = "127.0.0.1:1080/network-storage/v1")
	api_client = pnap_network_storage_api.ApiClient(configuration)

	def verify_called_once(self, expectation_id):
		# Result retrieved from server's verification
		# Verifying expectation matched exactly once.
		verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

		# Asserts a successful result.
		self.assertEqual(202, verifyResult.status_code)

	def tearDown(self):
		TestUtils.reset_expectations()
		self.api_client.close()

	def test_get_network_storages(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_get')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		opts = TestUtils.generate_query_params(request)

		result = api_instance.storage_networks_get(**opts)

		response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])
		response['body'][0]['volumes'][0]['createdOn'] = parse(response['body'][0]['volumes'][0]['createdOn'])

		# self.assertEqual(response['body'][0], model_to_dict(result[0]))

		self.verify_called_once(expectation_id)

	def test_get_network_storages_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_get_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")

		result = api_instance.storage_networks_id_get(storage_network_id)

		response['body']['createdOn'] = parse(response['body']['createdOn'])
		response['body']['volumes'][0]['createdOn'] = parse(response['body']['volumes'][0]['createdOn'])

		#self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_create_network_storage(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_post')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_create_dict = TestUtils.extract_request_body(request)
		storage_network_create_dict['volumes'] = [StorageNetworkVolumeCreate(**storage_network_create_dict['volumes'][0], _spec_property_naming=True)]
		storage_network_create = StorageNetworkCreate(**storage_network_create_dict)

		result = api_instance.storage_networks_post(storage_network_create=storage_network_create)

		response['body']['createdOn'] = parse(response['body']['createdOn'])
		response['body']['volumes'][0]['createdOn'] = parse(response['body']['volumes'][0]['createdOn'])

		# self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_network_storage_get_volumes(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_get_volumes')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")

		result = api_instance.storage_networks_storage_network_id_volumes_get(storage_network_id)

		response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])

		# self.assertEqual(response['body'][0], model_to_dict(result[0]))

		self.verify_called_once(expectation_id)

	def test_network_storage_get_volume_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_get_volume_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")
		volume_id = TestUtils.extract_id_from(request, "volumeId")

		result = api_instance.storage_networks_storage_network_id_volumes_volume_id_get(storage_network_id, volume_id)

		response['body']['createdOn'] = parse(response['body']['createdOn'])

		# self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_delete_network_storage_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_delete_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")

		result = api_instance.storage_networks_id_delete(storage_network_id)

		# self.assertEqual(response['body'][0], model_to_dict(result[0]))

		self.verify_called_once(expectation_id)

	def test_patch_network_storage_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_patch_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")
		storage_network_update = StorageNetworkUpdate(**TestUtils.extract_request_body(request))

		result = api_instance.storage_networks_id_patch(storage_network_id, storage_network_update=storage_network_update)

		response['body']['createdOn'] = parse(response['body']['createdOn'])
		response['body']['volumes'][0]['createdOn'] = parse(response['body']['volumes'][0]['createdOn'])

		# self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_networkstorage_post_volume(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_post_volume')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)
		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")

		volume_create = VolumeCreate(**TestUtils.convert_camel_to_snake_case(request))

		result = api_instance.storage_networks_storage_network_id_volumes_post(storage_network_id, volume_create=volume_create)

		response['body']['createdOn'] = parse(response['body']['createdOn'])

		# self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_network_storage_patch_volume_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_patch_volume_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")
		volume_id = TestUtils.extract_id_from(request, "volumeId")

		volume_update = VolumeUpdate(**TestUtils.extract_request_body(request))

		result = api_instance.storage_networks_storage_network_id_volumes_volume_id_patch(storage_network_id, volume_id, volume_update=volume_update)

		response['body']['createdOn'] = parse(response['body']['createdOn'])

		# self.assertEqual(response['body'], model_to_dict(result))

		self.verify_called_once(expectation_id)

	def test_network_storage_delete_volume_by_id(self):
		# Setting up expectation
		request, response = TestUtils.generate_payloads_from('networkstorageapi/networkstorage_delete_volume_by_id')
		expectation_id = TestUtils.setup_expectation(request, response, 1)

		api_instance = storage_networks_api.StorageNetworksApi(self.api_client)

		storage_network_id = TestUtils.extract_id_from(request, "storageNetworkId")
		volume_id = TestUtils.extract_id_from(request, "volumeId")

		result = api_instance.storage_networks_storage_network_id_volumes_volume_id_delete(storage_network_id, volume_id)

		# self.assertEqual(response['body'][0], model_to_dict(result[0]))

		self.verify_called_once(expectation_id)	

if __name__ == '__main__':
	TestUtils.reset_mockserver()
	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
		failfast=False, buffer=False, catchbreak=False)