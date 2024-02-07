# OperatingSystemDetails

Details of the operating system associated with this rated usage record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **int** | Number of cores. | 
**correlation_id** | **str** | Correlation is used to associate Operating System License charges and the Server on which it was installed. In this scenario, the correlation ID will be equal to the rated usage record ID representing the charge for the Server. | 

## Example

```python
from pnap_billing_api.models.operating_system_details import OperatingSystemDetails

# TODO update the JSON string below
json = "{}"
# create an instance of OperatingSystemDetails from a JSON string
operating_system_details_instance = OperatingSystemDetails.from_json(json)
# print the JSON string representation of the object
print OperatingSystemDetails.to_json()

# convert the object into a dict
operating_system_details_dict = operating_system_details_instance.to_dict()
# create an instance of OperatingSystemDetails from a dict
operating_system_details_form_dict = operating_system_details.from_dict(operating_system_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


