# ActionResult

Result of a successful action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Message describing the action&#39;s result. | 

## Example

```python
from pnap_bmc_api.models.action_result import ActionResult

# TODO update the JSON string below
json = "{}"
# create an instance of ActionResult from a JSON string
action_result_instance = ActionResult.from_json(json)
# print the JSON string representation of the object
print ActionResult.to_json()

# convert the object into a dict
action_result_dict = action_result_instance.to_dict()
# create an instance of ActionResult from a dict
action_result_form_dict = action_result.from_dict(action_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


