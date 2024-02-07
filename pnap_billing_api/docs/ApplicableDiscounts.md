# ApplicableDiscounts

Represents the applicable discount details for a product, including the discounted price and discount information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discounted_price** | **float** | The price of the product after applying a discount. | [optional] 
**discount_details** | [**List[DiscountDetails]**](DiscountDetails.md) |  | [optional] 

## Example

```python
from pnap_billing_api.models.applicable_discounts import ApplicableDiscounts

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicableDiscounts from a JSON string
applicable_discounts_instance = ApplicableDiscounts.from_json(json)
# print the JSON string representation of the object
print ApplicableDiscounts.to_json()

# convert the object into a dict
applicable_discounts_dict = applicable_discounts_instance.to_dict()
# create an instance of ApplicableDiscounts from a dict
applicable_discounts_form_dict = applicable_discounts.from_dict(applicable_discounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


