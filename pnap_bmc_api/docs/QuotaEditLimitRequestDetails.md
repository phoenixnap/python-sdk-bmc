# QuotaEditLimitRequestDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The new limit that is requested. Minimum allowed limit values: - 0 (Server, IPs) - 1000 (Network Storage) | 
**reason** | **str** | The reason for changing the limit. | 
**requested_on** | **datetime** | The point in time the request was submitted. | 

## Example

```python
from pnap_bmc_api.models.quota_edit_limit_request_details import QuotaEditLimitRequestDetails

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaEditLimitRequestDetails from a JSON string
quota_edit_limit_request_details_instance = QuotaEditLimitRequestDetails.from_json(json)
# print the JSON string representation of the object
print QuotaEditLimitRequestDetails.to_json()

# convert the object into a dict
quota_edit_limit_request_details_dict = quota_edit_limit_request_details_instance.to_dict()
# create an instance of QuotaEditLimitRequestDetails from a dict
quota_edit_limit_request_details_form_dict = quota_edit_limit_request_details.from_dict(quota_edit_limit_request_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


