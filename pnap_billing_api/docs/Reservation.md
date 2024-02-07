# Reservation

Reservation details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The reservation identifier. | 
**product_code** | **str** | The code identifying the product. This code has significant across all locations. | 
**product_category** | **str** | The product category. | 
**location** | [**LocationEnum**](LocationEnum.md) |  | 
**reservation_model** | [**ReservationModelEnum**](ReservationModelEnum.md) |  | 
**initial_invoice_model** | [**ReservationInvoicingModelEnum**](ReservationInvoicingModelEnum.md) |  | [optional] 
**start_date_time** | **datetime** | The point in time (in UTC) when the reservation starts. | 
**end_date_time** | **datetime** | The point in time (in UTC) when the reservation end. | [optional] 
**last_renewal_date_time** | **datetime** | The point in time (in UTC) when the reservation was renewed last. | [optional] 
**next_renewal_date_time** | **datetime** | The point in time (in UTC) when the reservation will be renewed if auto renew is set to true. | [optional] 
**auto_renew** | **bool** | A flag indicating whether the reservation will auto-renew (default is true). | 
**sku** | **str** | The sku that will be applied to this reservation. It is useful to find out the price by querying the /product endpoint. | 
**price** | **float** | Reservation price. | 
**price_unit** | [**PriceUnitEnum**](PriceUnitEnum.md) |  | 
**assigned_resource_id** | **str** | The resource ID currently being assigned to Reservation. | [optional] 
**next_billing_date** | **date** | Next billing date for Reservation. | [optional] 

## Example

```python
from pnap_billing_api.models.reservation import Reservation

# TODO update the JSON string below
json = "{}"
# create an instance of Reservation from a JSON string
reservation_instance = Reservation.from_json(json)
# print the JSON string representation of the object
print Reservation.to_json()

# convert the object into a dict
reservation_dict = reservation_instance.to_dict()
# create an instance of Reservation from a dict
reservation_form_dict = reservation.from_dict(reservation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


