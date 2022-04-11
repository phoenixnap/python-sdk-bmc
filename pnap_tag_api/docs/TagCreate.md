# TagCreate

Tag creation model.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the tag. Tag names are case-sensitive, and should be composed of a maximum of 100 characters including UTF-8 Unicode letters, numbers, and the following symbols: &#39;-&#39;, &#39;_&#39;. Regex: [A-zÀ-ú0-9_-]{1,100} | 
**is_billing_tag** | **bool** | Whether or not to show the tag as part of billing and invoices. | 
**description** | **str** | The description of the tag. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


