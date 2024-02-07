# ThresholdConfigurationDetails

Threshold billing configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_amount** | **float** | Threshold billing amount. | 

## Example

```python
from pnap_billing_api.models.threshold_configuration_details import ThresholdConfigurationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ThresholdConfigurationDetails from a JSON string
threshold_configuration_details_instance = ThresholdConfigurationDetails.from_json(json)
# print the JSON string representation of the object
print ThresholdConfigurationDetails.to_json()

# convert the object into a dict
threshold_configuration_details_dict = threshold_configuration_details_instance.to_dict()
# create an instance of ThresholdConfigurationDetails from a dict
threshold_configuration_details_form_dict = threshold_configuration_details.from_dict(threshold_configuration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


