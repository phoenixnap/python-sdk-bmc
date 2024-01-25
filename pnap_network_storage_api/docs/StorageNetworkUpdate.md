# StorageNetworkUpdate

Update storage network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Storage network friendly name. | [optional] 
**description** | **str** | Storage network description. | [optional] 

## Example

```python
from pnap_network_storage_api.models.storage_network_update import StorageNetworkUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNetworkUpdate from a JSON string
storage_network_update_instance = StorageNetworkUpdate.from_json(json)
# print the JSON string representation of the object
print StorageNetworkUpdate.to_json()

# convert the object into a dict
storage_network_update_dict = storage_network_update_instance.to_dict()
# create an instance of StorageNetworkUpdate from a dict
storage_network_update_form_dict = storage_network_update.from_dict(storage_network_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


