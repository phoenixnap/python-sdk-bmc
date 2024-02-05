# ServerReserve

Bare metal server reservation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing_model** | **str** | Server pricing model. Currently this field should be set to &#x60;ONE_MONTH_RESERVATION&#x60;, &#x60;TWELVE_MONTHS_RESERVATION&#x60;, &#x60;TWENTY_FOUR_MONTHS_RESERVATION&#x60; or &#x60;THIRTY_SIX_MONTHS_RESERVATION&#x60;. | 

## Example

```python
from pnap_bmc_api.models.server_reserve import ServerReserve

# TODO update the JSON string below
json = "{}"
# create an instance of ServerReserve from a JSON string
server_reserve_instance = ServerReserve.from_json(json)
# print the JSON string representation of the object
print ServerReserve.to_json()

# convert the object into a dict
server_reserve_dict = server_reserve_instance.to_dict()
# create an instance of ServerReserve from a dict
server_reserve_form_dict = server_reserve.from_dict(server_reserve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


