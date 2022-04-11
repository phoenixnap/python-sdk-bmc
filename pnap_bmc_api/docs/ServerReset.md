# ServerReset

Reset bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**install_default_ssh_keys** | **bool** | Whether or not to install SSH keys marked as default in addition to any SSH keys specified in this request. | [optional]  if omitted the server will use the default value of True
**ssh_keys** | **[str]** | A list of SSH keys that will be installed on the server. | [optional] 
**ssh_key_ids** | **[str]** | A list of SSH key IDs that will be installed on the server in addition to any SSH keys specified in this request. | [optional] 
**os_configuration** | [**OsConfigurationMap**](OsConfigurationMap.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


