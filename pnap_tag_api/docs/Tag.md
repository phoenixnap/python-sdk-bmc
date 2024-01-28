# Tag

Tag model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the tag. | 
**name** | **str** | The name of the tag. | 
**values** | **List[str]** | The optional values of the tag. | [optional] 
**description** | **str** | The description of the tag. | [optional] 
**is_billing_tag** | **bool** | Whether or not to show the tag as part of billing and invoices. | 
**resource_assignments** | [**List[ResourceAssignment]**](ResourceAssignment.md) | The tag&#39;s assigned resources. | [optional] 
**created_by** | **str** | The tag&#39;s creator. | [optional] [default to 'USER']

## Example

```python
from pnap_tag_api.models.tag import Tag

# TODO update the JSON string below
json = "{}"
# create an instance of Tag from a JSON string
tag_instance = Tag.from_json(json)
# print the JSON string representation of the object
print Tag.to_json()

# convert the object into a dict
tag_dict = tag_instance.to_dict()
# create an instance of Tag from a dict
tag_form_dict = tag.from_dict(tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


