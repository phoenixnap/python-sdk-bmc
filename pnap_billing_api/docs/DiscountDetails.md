# DiscountDetails

Represents the details of a discount applied to a product or charge.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | A unique code associated with the discount. | 
**type** | **str** | The type of discount applied. | 
**value** | **float** | The value or amount of the discount. The interpretation of this value depends on the &#39;type&#39; of discount.  | 

## Example

```python
from pnap_billing_api.models.discount_details import DiscountDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DiscountDetails from a JSON string
discount_details_instance = DiscountDetails.from_json(json)
# print the JSON string representation of the object
print DiscountDetails.to_json()

# convert the object into a dict
discount_details_dict = discount_details_instance.to_dict()
# create an instance of DiscountDetails from a dict
discount_details_form_dict = discount_details.from_dict(discount_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


