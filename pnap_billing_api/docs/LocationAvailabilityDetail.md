# LocationAvailabilityDetail

Info about location, solutions and availability for a product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**LocationEnum**](LocationEnum.md) |  | 
**min_quantity_requested** | **float** | Requested quantity. | 
**min_quantity_available** | **bool** | Is product available in specific location for requested quantity | 
**available_quantity** | **float** | Total available quantity of product in specific location. Max value is 10. | 
**solutions** | **List[str]** | Solutions supported in specific location for a product. | 

## Example

```python
from pnap_billing_api.models.location_availability_detail import LocationAvailabilityDetail

# TODO update the JSON string below
json = "{}"
# create an instance of LocationAvailabilityDetail from a JSON string
location_availability_detail_instance = LocationAvailabilityDetail.from_json(json)
# print the JSON string representation of the object
print LocationAvailabilityDetail.to_json()

# convert the object into a dict
location_availability_detail_dict = location_availability_detail_instance.to_dict()
# create an instance of LocationAvailabilityDetail from a dict
location_availability_detail_form_dict = location_availability_detail.from_dict(location_availability_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


