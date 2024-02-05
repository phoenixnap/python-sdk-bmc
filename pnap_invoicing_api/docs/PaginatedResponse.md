# PaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of items in the page (actual returned length can be less). | 
**offset** | **int** | The number of returned items skipped. | 
**total** | **int** | The total number of records available for retrieval. | 

## Example

```python
from pnap_invoicing_api.models.paginated_response import PaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponse from a JSON string
paginated_response_instance = PaginatedResponse.from_json(json)
# print the JSON string representation of the object
print PaginatedResponse.to_json()

# convert the object into a dict
paginated_response_dict = paginated_response_instance.to_dict()
# create an instance of PaginatedResponse from a dict
paginated_response_form_dict = paginated_response.from_dict(paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


