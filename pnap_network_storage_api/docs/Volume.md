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
**permissions** | [**Permissions**](Permissions.md) |  | [optional] 
**tags** | [**[TagAssignment]**](TagAssignment.md) | The tags assigned if any. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


