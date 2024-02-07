# ProductsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | The code identifying the product. This code has significant across all locations. | 
**product_category** | **str** | The product category. | 
**plans** | [**List[PricingPlan]**](PricingPlan.md) | The pricing plans available for this product. | [optional] 
**metadata** | [**ServerProductMetadata**](ServerProductMetadata.md) |  | 

## Example

```python
from pnap_billing_api.models.products_get200_response_inner import ProductsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ProductsGet200ResponseInner from a JSON string
products_get200_response_inner_instance = ProductsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ProductsGet200ResponseInner.to_json()

# convert the object into a dict
products_get200_response_inner_dict = products_get200_response_inner_instance.to_dict()
# create an instance of ProductsGet200ResponseInner from a dict
products_get200_response_inner_form_dict = products_get200_response_inner.from_dict(products_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


