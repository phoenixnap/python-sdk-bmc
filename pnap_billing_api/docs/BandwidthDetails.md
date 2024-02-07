# BandwidthDetails

Details of the bandwidth associated with this rated usage record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ingress_gb** | **float** | The amount of GB consumed in ingress (IN). | 
**egress_gb** | **float** | The amount of GB consumed in egress (OUT). | 
**package_quantity** | **float** | Package size per month. | [optional] 
**package_unit** | **str** | Package size unit. | [optional] 

## Example

```python
from pnap_billing_api.models.bandwidth_details import BandwidthDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthDetails from a JSON string
bandwidth_details_instance = BandwidthDetails.from_json(json)
# print the JSON string representation of the object
print BandwidthDetails.to_json()

# convert the object into a dict
bandwidth_details_dict = bandwidth_details_instance.to_dict()
# create an instance of BandwidthDetails from a dict
bandwidth_details_form_dict = bandwidth_details.from_dict(bandwidth_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


