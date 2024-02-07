# ConfigurationDetails

Billing configuration details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_configuration** | [**ThresholdConfigurationDetails**](ThresholdConfigurationDetails.md) |  | [optional] 

## Example

```python
from pnap_billing_api.models.configuration_details import ConfigurationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationDetails from a JSON string
configuration_details_instance = ConfigurationDetails.from_json(json)
# print the JSON string representation of the object
print ConfigurationDetails.to_json()

# convert the object into a dict
configuration_details_dict = configuration_details_instance.to_dict()
# create an instance of ConfigurationDetails from a dict
configuration_details_form_dict = configuration_details.from_dict(configuration_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


