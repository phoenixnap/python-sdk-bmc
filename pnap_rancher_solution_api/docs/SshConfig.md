# SshConfig

(Write-only) Configuration defining which public SSH keys are pre-installed as authorized on the server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_default_keys** | **bool** | Define whether public keys marked as default should be installed on this node. These are public keys that were already recorded on this system. Use &lt;a href&#x3D;&#39;https://developers.phoenixnap.com/docs/bmc/1/routes/ssh-keys/get&#39; target&#x3D;&#39;_blank&#39;&gt;GET /ssh-keys&lt;/a&gt; to retrieve a list of possible values. | [optional] [default to True]
**keys** | **List[str]** | List of public SSH keys. | [optional] 
**key_ids** | **List[str]** | List of public SSH key identifiers. These are public keys that were already recorded on this system. Use &lt;a href&#x3D;&#39;https://developers.phoenixnap.com/docs/bmc/1/routes/ssh-keys/get&#39; target&#x3D;&#39;_blank&#39;&gt;GET /ssh-keys&lt;/a&gt; to retrieve a list of possible values. | [optional] 

## Example

```python
from pnap_rancher_solution_api.models.ssh_config import SshConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SshConfig from a JSON string
ssh_config_instance = SshConfig.from_json(json)
# print the JSON string representation of the object
print SshConfig.to_json()

# convert the object into a dict
ssh_config_dict = ssh_config_instance.to_dict()
# create an instance of SshConfig from a dict
ssh_config_form_dict = ssh_config.from_dict(ssh_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


