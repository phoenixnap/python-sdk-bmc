# ProductAvailability

Product availability details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | Product code. | 
**product_category** | **str** | Product category. | 
**location_availability_details** | [**List[LocationAvailabilityDetail]**](LocationAvailabilityDetail.md) |  | 

## Example

```python
from pnap_billing_api.models.product_availability import ProductAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAvailability from a JSON string
product_availability_instance = ProductAvailability.from_json(json)
# print the JSON string representation of the object
print ProductAvailability.to_json()

# convert the object into a dict
product_availability_dict = product_availability_instance.to_dict()
# create an instance of ProductAvailability from a dict
product_availability_form_dict = product_availability.from_dict(product_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


