# Quota

Quota.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Quota. | 
**name** | **str** | The name of the Quota. | 
**description** | **str** | The Quota description. | 
**status** | **str** | The status of the quota resource usage. | 
**limit** | **int** | The limit set for the quota. | 
**used** | **int** | The quota used expressed as a number. | 
**quota_edit_limit_request_details** | [**[QuotaEditLimitRequestDetails]**](QuotaEditLimitRequestDetails.md) |  | [readonly] 
**unit** | **str** | An enum field describing what the limit is measured in. | defaults to "COUNT"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


