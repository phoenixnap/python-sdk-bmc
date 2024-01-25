# StorageConfiguration

Storage configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_partition** | [**StorageConfigurationRootPartition**](StorageConfigurationRootPartition.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.storage_configuration import StorageConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of StorageConfiguration from a JSON string
storage_configuration_instance = StorageConfiguration.from_json(json)
# print the JSON string representation of the object
print StorageConfiguration.to_json()

# convert the object into a dict
storage_configuration_dict = storage_configuration_instance.to_dict()
# create an instance of StorageConfiguration from a dict
storage_configuration_form_dict = storage_configuration.from_dict(storage_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


