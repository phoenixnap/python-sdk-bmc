# StorageNetwork

Storage network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Storage network ID. | [optional] 
**name** | **str** | Storage network friendly name. | [optional] 
**description** | **str** | Storage network description. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**location** | **str** | Location of storage network. Currently this field should be set to &#x60;PHX&#x60; or &#x60;ASH&#x60;. | [optional] 
**network_id** | **str** | Id of network the storage belongs to. | [optional] 
**ips** | **List[str]** | IP of the storage network. | [optional] 
**created_on** | **datetime** | Date and time when this storage network was created. | [optional] 
**delete_requested_on** | **datetime** | Date and time of the initial request for storage network deletion. | [optional] 
**volumes** | [**List[Volume]**](Volume.md) | Volume for a storage network. | [optional] 

## Example

```python
from pnap_network_storage_api.models.storage_network import StorageNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of StorageNetwork from a JSON string
storage_network_instance = StorageNetwork.from_json(json)
# print the JSON string representation of the object
print StorageNetwork.to_json()

# convert the object into a dict
storage_network_dict = storage_network_instance.to_dict()
# create an instance of StorageNetwork from a dict
storage_network_form_dict = storage_network.from_dict(storage_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


