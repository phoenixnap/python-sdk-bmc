# PricingPlan

Pricing plan details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | The SKU identifying this pricing plan. | 
**sku_description** | **str** | Description of this pricing plan. | [optional] 
**location** | **str** | The code identifying the location. | 
**pricing_model** | **str** | The pricing model. | 
**price** | **float** | The price per unit. | 
**price_unit** | [**PriceUnitEnum**](PriceUnitEnum.md) |  | 
**applicable_discounts** | [**ApplicableDiscounts**](ApplicableDiscounts.md) |  | [optional] 
**correlated_product_code** | **str** | Product code of the product this product is correlated with | [optional] 
**package_quantity** | **float** | Package size per month. | [optional] 
**package_unit** | **str** | Package size unit. | [optional] 

## Example

```python
from pnap_billing_api.models.pricing_plan import PricingPlan

# TODO update the JSON string below
json = "{}"
# create an instance of PricingPlan from a JSON string
pricing_plan_instance = PricingPlan.from_json(json)
# print the JSON string representation of the object
print PricingPlan.to_json()

# convert the object into a dict
pricing_plan_dict = pricing_plan_instance.to_dict()
# create an instance of PricingPlan from a dict
pricing_plan_form_dict = pricing_plan.from_dict(pricing_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


