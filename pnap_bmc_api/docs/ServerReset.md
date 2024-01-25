# ServerReset

Reset bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_default_ssh_keys** | **bool** | Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request. | [optional] [default to True]
**ssh_keys** | **List[str]** | A list of SSH keys that will be installed on the server. | [optional] 
**ssh_key_ids** | **List[str]** | A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request. | [optional] 
**os_configuration** | [**OsConfigurationMap**](OsConfigurationMap.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.server_reset import ServerReset

# TODO update the JSON string below
json = "{}"
# create an instance of ServerReset from a JSON string
server_reset_instance = ServerReset.from_json(json)
# print the JSON string representation of the object
print ServerReset.to_json()

# convert the object into a dict
server_reset_dict = server_reset_instance.to_dict()
# create an instance of ServerReset from a dict
server_reset_form_dict = server_reset.from_dict(server_reset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


