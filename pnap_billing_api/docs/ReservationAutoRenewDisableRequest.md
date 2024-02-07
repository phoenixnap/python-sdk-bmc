# ReservationAutoRenewDisableRequest

Disabling auto-renewal for reservation request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_renew_disable_reason** | **str** |  | [optional] 

## Example

```python
from pnap_billing_api.models.reservation_auto_renew_disable_request import ReservationAutoRenewDisableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationAutoRenewDisableRequest from a JSON string
reservation_auto_renew_disable_request_instance = ReservationAutoRenewDisableRequest.from_json(json)
# print the JSON string representation of the object
print ReservationAutoRenewDisableRequest.to_json()

# convert the object into a dict
reservation_auto_renew_disable_request_dict = reservation_auto_renew_disable_request_instance.to_dict()
# create an instance of ReservationAutoRenewDisableRequest from a dict
reservation_auto_renew_disable_request_form_dict = reservation_auto_renew_disable_request.from_dict(reservation_auto_renew_disable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


