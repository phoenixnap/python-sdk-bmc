# Quota

Quota.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Quota. | 
**name** | **str** | The name of the Quota. | 
**description** | **str** | The Quota description. | 
**status** | **str** | The status of the quota resource usage. | 
**limit** | **int** | The limit set for the quota. | 
**unit** | **str** | Unit of the quota type. Supported values are &#39;COUNT&#39; and &#39;GB&#39;. | 
**used** | **int** | The quota used expressed as a number. | 
**quota_edit_limit_request_details** | [**List[QuotaEditLimitRequestDetails]**](QuotaEditLimitRequestDetails.md) |  | [readonly] 

## Example

```python
from pnap_bmc_api.models.quota import Quota

# TODO update the JSON string below
json = "{}"
# create an instance of Quota from a JSON string
quota_instance = Quota.from_json(json)
# print the JSON string representation of the object
print Quota.to_json()

# convert the object into a dict
quota_dict = quota_instance.to_dict()
# create an instance of Quota from a dict
quota_form_dict = quota.from_dict(quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


