# CardPaymentMethodDetails

Card payment details of a transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | The Card Type. Supported Card Types include: VISA, MASTERCARD, DISCOVER, JCB &amp; AMEX. | 
**last_four_digits** | **str** | The last four digits of the card number. | 

## Example

```python
from pnap_payments_api.models.card_payment_method_details import CardPaymentMethodDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CardPaymentMethodDetails from a JSON string
card_payment_method_details_instance = CardPaymentMethodDetails.from_json(json)
# print the JSON string representation of the object
print CardPaymentMethodDetails.to_json()

# convert the object into a dict
card_payment_method_details_dict = card_payment_method_details_instance.to_dict()
# create an instance of CardPaymentMethodDetails from a dict
card_payment_method_details_form_dict = card_payment_method_details.from_dict(card_payment_method_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


