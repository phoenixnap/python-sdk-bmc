# DeleteSshKeyResult

Result of a successful delete action on a SSH key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Resource has been deleted. | 
**ssh_key_id** | **str** | The unique identifier of the deleted resource. | 

## Example

```python
from pnap_bmc_api.models.delete_ssh_key_result import DeleteSshKeyResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSshKeyResult from a JSON string
delete_ssh_key_result_instance = DeleteSshKeyResult.from_json(json)
# print the JSON string representation of the object
print DeleteSshKeyResult.to_json()

# convert the object into a dict
delete_ssh_key_result_dict = delete_ssh_key_result_instance.to_dict()
# create an instance of DeleteSshKeyResult from a dict
delete_ssh_key_result_form_dict = delete_ssh_key_result.from_dict(delete_ssh_key_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


