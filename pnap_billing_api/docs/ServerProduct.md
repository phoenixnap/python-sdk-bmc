# ServerProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_code** | **str** | The code identifying the product. This code has significant across all locations. | 
**product_category** | **str** | The product category. | 
**plans** | [**List[PricingPlan]**](PricingPlan.md) | The pricing plans available for this product. | [optional] 
**metadata** | [**ServerProductMetadata**](ServerProductMetadata.md) |  | 

## Example

```python
from pnap_billing_api.models.server_product import ServerProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ServerProduct from a JSON string
server_product_instance = ServerProduct.from_json(json)
# print the JSON string representation of the object
print ServerProduct.to_json()

# convert the object into a dict
server_product_dict = server_product_instance.to_dict()
# create an instance of ServerProduct from a dict
server_product_form_dict = server_product.from_dict(server_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


