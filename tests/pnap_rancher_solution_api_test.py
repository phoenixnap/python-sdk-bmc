import unittest
import xmlrunner

from test_utils import TestUtils

import pnap_rancher_solution_api
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.models.cluster import Cluster
from pnap_rancher_solution_api.models.delete_result import DeleteResult

class  TestAuditApi(unittest.TestCase):
  configuration = pnap_rancher_solution_api.Configuration(host = "127.0.0.1:1080/solutions/rancher/v1beta")
  api_client = pnap_rancher_solution_api.ApiClient(configuration)


  def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)

  def test_get_clusters(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('rancherapi/clusters_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = clusters_api.ClustersApi(self.api_client)
    
    result = api_instance.clusters_get()

    self.assertEqual(response['body'][0], result[0].to_dict())

    self.verify_called_once(expectation_id)

  def test_create_cluster(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('rancherapi/clusters_post')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = clusters_api.ClustersApi(self.api_client)
    cluster = TestUtils.extract_request_body(request)
    
    result = api_instance.clusters_post(cluster=cluster)

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation_id)

  def test_get_cluster_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('rancherapi/clusters_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = clusters_api.ClustersApi(self.api_client)
    id = TestUtils.extract_id_from(request)
    
    result = api_instance.clusters_id_get(id)

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation_id)

  def test_delete_cluster_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('rancherapi/clusters_delete_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    # Creating new instance
    api_instance = clusters_api.ClustersApi(self.api_client)
    id = TestUtils.extract_id_from(request)
    
    result = api_instance.clusters_id_delete(id)

    self.assertEqual(response['body'], result.to_dict())

    self.verify_called_once(expectation_id)

  def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
  TestUtils.reset_mockserver()
  unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
    failfast=False, buffer=False, catchbreak=False)