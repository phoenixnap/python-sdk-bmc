# StorageDetails

Details of the storage associated with this rated usage record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_storage_id** | **str** | Network storage ID. | 
**network_storage_name** | **str** | Network storage name. | 
**volume_id** | **str** | Volume ID. | 
**volume_name** | **str** | Volume name. | 
**capacity_in_gb** | **int** | Capacity in GB. | 
**created_on** | **datetime** | Timestamp when the record was created. | 

## Example

```python
from pnap_billing_api.models.storage_details import StorageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDetails from a JSON string
storage_details_instance = StorageDetails.from_json(json)
# print the JSON string representation of the object
print StorageDetails.to_json()

# convert the object into a dict
storage_details_dict = storage_details_instance.to_dict()
# create an instance of StorageDetails from a dict
storage_details_form_dict = storage_details.from_dict(storage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


