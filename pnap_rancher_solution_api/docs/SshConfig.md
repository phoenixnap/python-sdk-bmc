# SshConfig

(Write-only) Configuration defining which public SSH keys are pre-installed as authorized on the server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_default_keys** | **bool** | Define whether public keys marked as default should be installed on this node. These are public keys that were already recorded on this system. Use &lt;a href&#x3D;&#39;https://developers.phoenixnap.com/docs/bmc/1/routes/ssh-keys/get&#39; target&#x3D;&#39;_blank&#39;&gt;GET /ssh-keys&lt;/a&gt; to retrieve a list of possible values. | [optional]  if omitted the server will use the default value of True
**keys** | **[str]** | List of public SSH keys. | [optional] 
**key_ids** | **[str]** | List of public SSH key identifiers. These are public keys that were already recorded on this system. Use &lt;a href&#x3D;&#39;https://developers.phoenixnap.com/docs/bmc/1/routes/ssh-keys/get&#39; target&#x3D;&#39;_blank&#39;&gt;GET /ssh-keys&lt;/a&gt; to retrieve a list of possible values. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


