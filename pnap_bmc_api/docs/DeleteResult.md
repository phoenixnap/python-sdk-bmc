# DeleteResult

Result of a successful delete action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Server has been deleted. | 
**server_id** | **str** | The unique identifier of the server. | 

## Example

```python
from pnap_bmc_api.models.delete_result import DeleteResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResult from a JSON string
delete_result_instance = DeleteResult.from_json(json)
# print the JSON string representation of the object
print DeleteResult.to_json()

# convert the object into a dict
delete_result_dict = delete_result_instance.to_dict()
# create an instance of DeleteResult from a dict
delete_result_form_dict = delete_result.from_dict(delete_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


