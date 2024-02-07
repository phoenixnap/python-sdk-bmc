# Product

Product details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | The code identifying the product. This code has significant across all locations. | 
**product_category** | **str** | The product category. | 
**plans** | [**List[PricingPlan]**](PricingPlan.md) | The pricing plans available for this product. | [optional] 

## Example

```python
from pnap_billing_api.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print Product.to_json()

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


