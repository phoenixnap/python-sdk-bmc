# ResetResult

Result of a successful reset action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | Message describing the reset result. | 
**password** | **str** | Password set for user Admin on Windows server or user root on ESXi server. | [optional] 
**os_configuration** | [**OsConfigurationMap**](OsConfigurationMap.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.reset_result import ResetResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResetResult from a JSON string
reset_result_instance = ResetResult.from_json(json)
# print the JSON string representation of the object
print ResetResult.to_json()

# convert the object into a dict
reset_result_dict = reset_result_instance.to_dict()
# create an instance of ResetResult from a dict
reset_result_form_dict = reset_result.from_dict(reset_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


