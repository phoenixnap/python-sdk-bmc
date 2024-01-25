# QuotaEditLimitRequest

A request to change the limit on a quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The new limit that is requested. Minimum allowed limit values: - 0 (Server, IPs) - 1000 (Network Storage) | 
**reason** | **str** | The reason for changing the limit. | 

## Example

```python
from pnap_bmc_api.models.quota_edit_limit_request import QuotaEditLimitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaEditLimitRequest from a JSON string
quota_edit_limit_request_instance = QuotaEditLimitRequest.from_json(json)
# print the JSON string representation of the object
print QuotaEditLimitRequest.to_json()

# convert the object into a dict
quota_edit_limit_request_dict = quota_edit_limit_request_instance.to_dict()
# create an instance of QuotaEditLimitRequest from a dict
quota_edit_limit_request_form_dict = quota_edit_limit_request.from_dict(quota_edit_limit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


