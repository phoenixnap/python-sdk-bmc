# TagAssignmentRequest

Tag request to assign to resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the tag. Tag names are case-sensitive, and should be composed of a maximum of 100 characters including UTF-8 Unicode letters, numbers, and the following symbols: &#39;-&#39;, &#39;_&#39;. Regex: [A-zÀ-ú0-9_-]{1,100}. | 
**value** | **str** | The value of the tag assigned to the resource. Tag values are case-sensitive, and should be composed of a maximum of 100 characters including UTF-8 Unicode letters, numbers, and the following symbols: &#39;-&#39;, &#39;_&#39;. Regex: [A-zÀ-ú0-9_-]{1,100}. | [optional] 

## Example

```python
from pnap_network_storage_api.models.tag_assignment_request import TagAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TagAssignmentRequest from a JSON string
tag_assignment_request_instance = TagAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print TagAssignmentRequest.to_json()

# convert the object into a dict
tag_assignment_request_dict = tag_assignment_request_instance.to_dict()
# create an instance of TagAssignmentRequest from a dict
tag_assignment_request_form_dict = tag_assignment_request.from_dict(tag_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


