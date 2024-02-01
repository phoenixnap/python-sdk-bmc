# ReservationRequest

Reservation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sku** | **str** | The sku code of product pricing plan. | 

## Example

```python
from pnap_billing_api.models.reservation_request import ReservationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationRequest from a JSON string
reservation_request_instance = ReservationRequest.from_json(json)
# print the JSON string representation of the object
print ReservationRequest.to_json()

# convert the object into a dict
reservation_request_dict = reservation_request_instance.to_dict()
# create an instance of ReservationRequest from a dict
reservation_request_form_dict = reservation_request.from_dict(reservation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


