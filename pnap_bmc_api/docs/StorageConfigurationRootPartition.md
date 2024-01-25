# StorageConfigurationRootPartition

Root partition configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raid** | **str** | Software RAID configuration. The following RAID options are available: NO_RAID, RAID_0, RAID_1. | [optional] [default to 'NO_RAID']
**size** | **int** | The size of the root partition in GB. -1 to use all available space. | [optional] [default to -1]

## Example

```python
from pnap_bmc_api.models.storage_configuration_root_partition import StorageConfigurationRootPartition

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfigurationRootPartition from a JSON string
storage_configuration_root_partition_instance = StorageConfigurationRootPartition.from_json(json)
# print the JSON string representation of the object
print StorageConfigurationRootPartition.to_json()

# convert the object into a dict
storage_configuration_root_partition_dict = storage_configuration_root_partition_instance.to_dict()
# create an instance of StorageConfigurationRootPartition from a dict
storage_configuration_root_partition_form_dict = storage_configuration_root_partition.from_dict(storage_configuration_root_partition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


