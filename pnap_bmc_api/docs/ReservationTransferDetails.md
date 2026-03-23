# ReservationTransferDetails

Reservation transfer details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_server_id** | **str** | ID of target server to transfer reservation to. | 

## Example

```python
from pnap_bmc_api.models.reservation_transfer_details import ReservationTransferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationTransferDetails from a JSON string
reservation_transfer_details_instance = ReservationTransferDetails.from_json(json)
# print the JSON string representation of the object
print ReservationTransferDetails.to_json()

# convert the object into a dict
reservation_transfer_details_dict = reservation_transfer_details_instance.to_dict()
# create an instance of ReservationTransferDetails from a dict
reservation_transfer_details_form_dict = reservation_transfer_details.from_dict(reservation_transfer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


