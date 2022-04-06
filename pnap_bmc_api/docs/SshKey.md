# SshKey

SSH Key.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the SSH Key. | 
**default** | **bool** | Keys marked as default are always included on server creation and reset unless toggled off in creation/reset request. | 
**name** | **str** | Friendly SSH key name to represent an SSH key. | 
**key** | **str** | SSH Key value. | 
**fingerprint** | **str** | SSH key auto-generated SHA-256 fingerprint. | 
**created_on** | **datetime** | Date and time of creation. | 
**last_updated_on** | **datetime** | Date and time of last update. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


