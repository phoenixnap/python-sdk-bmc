# VolumeUpdate

Update storage network volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Volume friendly name. | [optional] 
**description** | **str** | Volume description. | [optional] 
**capacity_in_gb** | **int** | Capacity of Volume in GB. Currently only whole numbers and multiples of 1000GB are supported. | [optional] 
**path_suffix** | **str** | Last part of volume&#39;s path. | [optional] 
**permissions** | [**PermissionsUpdate**](PermissionsUpdate.md) |  | [optional] 

## Example

```python
from pnap_network_storage_api.models.volume_update import VolumeUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeUpdate from a JSON string
volume_update_instance = VolumeUpdate.from_json(json)
# print the JSON string representation of the object
print VolumeUpdate.to_json()

# convert the object into a dict
volume_update_dict = volume_update_instance.to_dict()
# create an instance of VolumeUpdate from a dict
volume_update_form_dict = volume_update.from_dict(volume_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


