# VolumeCreate

Create Volume.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Volume friendly name. | 
**capacity_in_gb** | **int** | Capacity of Volume in GB. Currently only whole numbers and multiples of 1000GB are supported. | 
**description** | **str** | Volume description. | [optional] 
**path_suffix** | **str** | Last part of volume&#39;s path. | [optional] 
**permissions** | [**PermissionsCreate**](PermissionsCreate.md) |  | [optional] 
**tags** | [**[TagAssignmentRequest]**](TagAssignmentRequest.md) | Tags to set to the resource. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


