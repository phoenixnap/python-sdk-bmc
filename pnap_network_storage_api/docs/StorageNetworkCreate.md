# StorageNetworkCreate

Create Storage Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Storage network friendly name. | 
**description** | **str** | Storage network description. | [optional] 
**location** | **str** | Location of storage network. Currently this field should be set to &#x60;PHX&#x60; or &#x60;ASH&#x60;. | 
**volumes** | [**List[StorageNetworkVolumeCreate]**](StorageNetworkVolumeCreate.md) | Volume to be created alongside storage. Currently only 1 volume is supported. | 
**client_vlan** | **int** | Custom Client VLAN that the Storage Network will be set to. | [optional] 

## Example

```python
from pnap_network_storage_api.models.storage_network_create import StorageNetworkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNetworkCreate from a JSON string
storage_network_create_instance = StorageNetworkCreate.from_json(json)
# print the JSON string representation of the object
print StorageNetworkCreate.to_json()

# convert the object into a dict
storage_network_create_dict = storage_network_create_instance.to_dict()
# create an instance of StorageNetworkCreate from a dict
storage_network_create_form_dict = storage_network_create.from_dict(storage_network_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


