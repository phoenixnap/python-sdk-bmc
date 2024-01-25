# VolumeCreate

Create Volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Volume friendly name. | 
**description** | **str** | Volume description. | [optional] 
**path_suffix** | **str** | Last part of volume&#39;s path. | [optional] 
**capacity_in_gb** | **int** | Capacity of Volume in GB. Currently only whole numbers and multiples of 1000GB are supported. | 
**permissions** | [**PermissionsCreate**](PermissionsCreate.md) |  | [optional] 
**tags** | [**List[TagAssignmentRequest]**](TagAssignmentRequest.md) | Tags to set to the resource. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview). | [optional] 

## Example

```python
from pnap_network_storage_api.models.volume_create import VolumeCreate

# TODO update the JSON string below
json = "{}"
# create an instance of VolumeCreate from a JSON string
volume_create_instance = VolumeCreate.from_json(json)
# print the JSON string representation of the object
print VolumeCreate.to_json()

# convert the object into a dict
volume_create_dict = volume_create_instance.to_dict()
# create an instance of VolumeCreate from a dict
volume_create_form_dict = volume_create.from_dict(volume_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


