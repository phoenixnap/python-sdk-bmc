# TagAssignment

Tag assigned to resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the tag. | 
**name** | **str** | The name of the tag. | 
**value** | **str** | The value of the tag assigned to the resource. | [optional] 
**is_billing_tag** | **bool** | Whether or not to show the tag as part of billing and invoices | 
**created_by** | **str** | Who the tag was created by. | [optional] 

## Example

```python
from pnap_network_storage_api.models.tag_assignment import TagAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of TagAssignment from a JSON string
tag_assignment_instance = TagAssignment.from_json(json)
# print the JSON string representation of the object
print TagAssignment.to_json()

# convert the object into a dict
tag_assignment_dict = tag_assignment_instance.to_dict()
# create an instance of TagAssignment from a dict
tag_assignment_form_dict = tag_assignment.from_dict(tag_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


