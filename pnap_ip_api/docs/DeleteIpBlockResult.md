# DeleteIpBlockResult

Result of a successful delete action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | IP Block has been deleted. | 
**ip_block_id** | **str** | The unique identifier of the IP Block. | 

## Example

```python
from pnap_ip_api.models.delete_ip_block_result import DeleteIpBlockResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIpBlockResult from a JSON string
delete_ip_block_result_instance = DeleteIpBlockResult.from_json(json)
# print the JSON string representation of the object
print DeleteIpBlockResult.to_json()

# convert the object into a dict
delete_ip_block_result_dict = delete_ip_block_result_instance.to_dict()
# create an instance of DeleteIpBlockResult from a dict
delete_ip_block_result_form_dict = delete_ip_block_result.from_dict(delete_ip_block_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


