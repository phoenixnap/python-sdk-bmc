# Tag

Tag model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the tag. | 
**name** | **str** | The name of the tag. | 
**is_billing_tag** | **bool** | Whether or not to show the tag as part of billing and invoices. | 
**values** | **[str]** | The optional values of the tag. | [optional] 
**description** | **str** | The description of the tag. | [optional] 
**resource_assignments** | [**[ResourceAssignment]**](ResourceAssignment.md) | The tag&#39;s assigned resources. | [optional] 
**created_by** | **str** | The tag&#39;s creator. | [optional]  if omitted the server will use the default value of "USER"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


