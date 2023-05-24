# StorageConfigurationRootPartition

Root partition configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raid** | **str** | Software RAID configuration. The following RAID options are available: NO_RAID, RAID_0, RAID_1. | [optional]  if omitted the server will use the default value of "NO_RAID"
**size** | **int** | The size of the root partition in GB. -1 to use all available space. | [optional]  if omitted the server will use the default value of -1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


