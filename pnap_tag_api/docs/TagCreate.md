# TagCreate

Tag creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name of the tag. Tag names are case-sensitive, and should be composed of a maximum of 100 characters including UTF-8 Unicode letters, numbers, and the following symbols: &#39;-&#39;, &#39;_&#39;. Regex: [A-zÀ-ú0-9_-]{1,100} | 
**description** | **str** | The description of the tag. | [optional] 
**is_billing_tag** | **bool** | Whether or not to show the tag as part of billing and invoices. | 

## Example

```python
from pnap_tag_api.models.tag_create import TagCreate

# TODO update the JSON string below
json = "{}"
# create an instance of TagCreate from a JSON string
tag_create_instance = TagCreate.from_json(json)
# print the JSON string representation of the object
print TagCreate.to_json()

# convert the object into a dict
tag_create_dict = tag_create_instance.to_dict()
# create an instance of TagCreate from a dict
tag_create_form_dict = tag_create.from_dict(tag_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


