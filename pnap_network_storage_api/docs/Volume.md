# Volume

Volume for a storage network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Volume ID. | [optional] 
**name** | **str** | Volume friendly name. | [optional] 
**description** | **str** | Volume description. | [optional] 
**path** | **str** | Volume&#39;s full path. It is in form of &#x60;/{volumeId}/pathSuffix&#x60;&#39;. | [optional] 
**path_suffix** | **str** | Last part of volume&#39;s path. | [optional] 
**capacity_in_gb** | **int** | Maximum capacity in GB. | [optional] 
**used_capacity_in_gb** | **int** | Used capacity in GB, updated periodically. | [optional] 
**protocol** | **str** | File system protocol. Currently this field should be set to &#x60;NFS&#x60;. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**delete_requested_on** | **datetime** | Date and time of the initial request for volume deletion. | [optional] 
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**tags** | [**List[TagAssignment]**](TagAssignment.md) | The tags assigned if any. | [optional] 

## Example

```python
from pnap_network_storage_api.models.volume import Volume

# TODO update the JSON string below
json = "{}"
# create an instance of Volume from a JSON string
volume_instance = Volume.from_json(json)
# print the JSON string representation of the object
print Volume.to_json()

# convert the object into a dict
volume_dict = volume_instance.to_dict()
# create an instance of Volume from a dict
volume_form_dict = volume.from_dict(volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


