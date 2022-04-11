import unittest
import xmlrunner
from dateutil.parser import parse

from test_utils import TestUtils

import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.api import ssh_keys_api
from pnap_bmc_api.api import quotas_api
from pnap_bmc_api.model.ssh_key_create import SshKeyCreate
from pnap_bmc_api.model.ssh_key_update import SshKeyUpdate
from pnap_bmc_api.model.server_create import ServerCreate
from pnap_bmc_api.model.server_patch import ServerPatch
from pnap_bmc_api.model.server_reserve import ServerReserve
from pnap_bmc_api.model.server_reset import ServerReset
from pnap_bmc_api.model.tag_assignment_request import TagAssignmentRequest
from pnap_bmc_api.model.relinquish_ip_block import RelinquishIpBlock
from pnap_bmc_api.model.server_ip_block import ServerIpBlock
from pnap_bmc_api.model.server_private_network import ServerPrivateNetwork
from pnap_bmc_api.model.tag_assignment_request import TagAssignmentRequest
from pnap_bmc_api.model.quota_edit_limit_request import QuotaEditLimitRequest
from pnap_bmc_api.model_utils import model_to_dict

class  TestBmcApi(unittest.TestCase):
  configuration = pnap_bmc_api.Configuration(host = "127.0.0.1:1080/bmc/v1")
  api_client = pnap_bmc_api.ApiClient(configuration)


  def verify_called_once(self, expectation_id):
    # Result retrieved from server's verification
    # Verifying expectation matched exactly once.
    verifyResult = TestUtils.verify_expectation_matched_times(expectation_id, 1)

    # Asserts a successful result.
    self.assertEqual(202, verifyResult.status_code)

  def test_get_quotas(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/quotas/quotas_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = quotas_api.QuotasApi(self.api_client)

    result = api_instance.quotas_get()

    # Parsing time for comparison
    response['body'][0]['quotaEditLimitRequestDetails'][0]['requestedOn'] = parse(response['body'][0]['quotaEditLimitRequestDetails'][0]['requestedOn'])

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

  def test_get_quota_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/quotas/quotas_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = quotas_api.QuotasApi(self.api_client)
    quota_id = TestUtils.extract_id_from(request)

    result = api_instance.quotas_quota_id_get(quota_id)

    # Parsing time for comparison
    response['body']['quotaEditLimitRequestDetails'][0]['requestedOn'] = parse(response['body']['quotaEditLimitRequestDetails'][0]['requestedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_quota_request_edit(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/quotas/quotas_action_request_edit')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = quotas_api.QuotasApi(self.api_client)
    quota_id = TestUtils.extract_id_from(request)
    quota_edit_limit_request = QuotaEditLimitRequest(**TestUtils.extract_request_body(request))

    api_instance.quotas_quota_id_actions_request_edit_post(quota_id, quota_edit_limit_request=quota_edit_limit_request)

    self.verify_called_once(expectation_id)

  def test_get_sshkeys(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/sshkeys/sshkeys_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ssh_keys_api.SSHKeysApi(self.api_client)

    result = api_instance.ssh_keys_get()

    # Parsing time for comparison
    response['body'][0]['createdOn'] = parse(response['body'][0]['createdOn'])
    response['body'][0]['lastUpdatedOn'] = parse(response['body'][0]['lastUpdatedOn'])

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

  def test_get_sshkey_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/sshkeys/sshkeys_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ssh_keys_api.SSHKeysApi(self.api_client)

    ssh_key_id = TestUtils.extract_id_from(request)

    result = api_instance.ssh_keys_ssh_key_id_get(ssh_key_id)

    # Parsing time for comparison
    response['body']['createdOn'] = parse(response['body']['createdOn'])
    response['body']['lastUpdatedOn'] = parse(response['body']['lastUpdatedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_post_sshkey(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/sshkeys/sshkeys_post')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ssh_keys_api.SSHKeysApi(self.api_client)

    ssh_key_create = SshKeyCreate(**TestUtils.extract_request_body(request))
    result = api_instance.ssh_keys_post(ssh_key_create=ssh_key_create)

    # Parsing time for comparison
    response['body']['createdOn'] = parse(response['body']['createdOn'])
    response['body']['lastUpdatedOn'] = parse(response['body']['lastUpdatedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_put_sshkey_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/sshkeys/sshkeys_put_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ssh_keys_api.SSHKeysApi(self.api_client)

    ssh_key_id = TestUtils.extract_id_from(request)
    ssh_key_update = SshKeyUpdate(**TestUtils.extract_request_body(request))

    result = api_instance.ssh_keys_ssh_key_id_put(ssh_key_id, ssh_key_update=ssh_key_update)

    # Parsing time for comparison
    response['body']['createdOn'] = parse(response['body']['createdOn'])
    response['body']['lastUpdatedOn'] = parse(response['body']['lastUpdatedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_delete_sshkey_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/sshkeys/sshkeys_delete_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = ssh_keys_api.SSHKeysApi(self.api_client)

    ssh_key_id = TestUtils.extract_id_from(request)

    result = api_instance.ssh_keys_ssh_key_id_delete(ssh_key_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_get_servers(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_get')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    opts = TestUtils.generate_query_params(request)

    result = api_instance.servers_get(tag=[opts['tag']])

    # Parsing time for comparison
    response['body'][0]['provisionedOn'] = parse(response['body'][0]['provisionedOn'])

    self.assertEqual(response['body'][0], model_to_dict(result[0]))

    self.verify_called_once(expectation_id)

  def test_get_servers_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_get_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_get(server_id)

    # Parsing time for comparison
    response['body']['provisionedOn'] = parse(response['body']['provisionedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_create_server(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_post')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_create_dict = TestUtils.extract_request_body(request)
    server_create_dict['tags'] = [TagAssignmentRequest(**server_create_dict['tags'][0])]
    server_create = ServerCreate(**server_create_dict)

    result = api_instance.servers_post(server_create=server_create)

    # Parsing time for comparison
    response['body']['provisionedOn'] = parse(response['body']['provisionedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_delete_servers_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_delete_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_delete(server_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_patch_server(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_patch_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    server_patch = ServerPatch(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_patch(server_id, server_patch=server_patch)

    # Parsing time for comparison
    response['body']['provisionedOn'] = parse(response['body']['provisionedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_deprovision(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_deprovision')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    relinquish_ip_block = RelinquishIpBlock(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_actions_deprovision_post(server_id, relinquish_ip_block=relinquish_ip_block)

    self.assertEqual(response['body'], result)

    self.verify_called_once(expectation_id)

  def test_server_power_off(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_power_off')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_actions_power_off_post(server_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_power_on(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_power_on')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_actions_power_on_post(server_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_reboot(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_reboot')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_actions_reboot_post(server_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_reserve(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_reserve')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    server_reserve = ServerReserve(**TestUtils.extract_request_body(request), _spec_property_naming=True)

    result = api_instance.servers_server_id_actions_reserve_post(server_id, server_reserve=server_reserve)

    # Parsing time for comparison
    response['body']['provisionedOn'] = parse(response['body']['provisionedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_reset(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_reset')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    server_reset = ServerReset(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_actions_reset_post(server_id, server_reset=server_reset)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_shutdown(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_action_shutdown')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)

    result = api_instance.servers_server_id_actions_shutdown_post(server_id)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_create_ip_block(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_post_ip_block')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    server_ip_block = ServerIpBlock(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_ip_blocks_post(server_id, server_ip_block=server_ip_block)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_delete_ip_block(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_delete_ip_block_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    ip_block_id = TestUtils.extract_id_from(request, 'ipId')
    relinquish_ip_block = RelinquishIpBlock(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id, relinquish_ip_block=relinquish_ip_block)

    self.assertEqual(response['body'], result)

    self.verify_called_once(expectation_id)

  def test_server_create_private_network(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_post_private_networks')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    server_private_network = ServerPrivateNetwork(**TestUtils.extract_request_body(request))

    result = api_instance.servers_server_id_private_networks_post(server_id, server_private_network=server_private_network)

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def test_server_delete_private_network(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_delete_private_network_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    private_network_id = TestUtils.extract_id_from(request, 'networkId')

    result = api_instance.delete_private_network(server_id, private_network_id)

    self.assertEqual(response['body'], result)

    self.verify_called_once(expectation_id)

  def test_server_put_tags_by_id(self):
    # Setting up expectation
    request, response = TestUtils.generate_payloads_from('bmcapi/servers/servers_put_tags_by_id')
    expectation_id = TestUtils.setup_expectation(request, response, 1)
    
    api_instance = servers_api.ServersApi(self.api_client)
    server_id = TestUtils.extract_id_from(request)
    tag_assignment_request = [TagAssignmentRequest(**TestUtils.extract_request_body(request)[0])]

    result = api_instance.servers_server_id_tags_put(server_id, tag_assignment_request=tag_assignment_request)

    # Parsing time for comparison
    response['body']['provisionedOn'] = parse(response['body']['provisionedOn'])

    self.assertEqual(response['body'], model_to_dict(result))

    self.verify_called_once(expectation_id)

  def tearDown(self):
    TestUtils.reset_expectations()
    self.api_client.close()

if __name__ == '__main__':
     unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        failfast=False, buffer=False, catchbreak=False)