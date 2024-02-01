# Transaction

Transaction response model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Transaction ID. | 
**status** | **str** | The Transaction status. Status may be: SUCCESS, PROCESSING, FAILED | 
**details** | **str** | Details about the transaction. Contains failure reason in case of failed transactions. | [optional] 
**amount** | **float** | The transaction amount. | 
**currency** | **str** | The transaction currency. | 
**var_date** | **datetime** | Date and time when transaction was created. | 
**metadata** | [**TransactionMetadata**](TransactionMetadata.md) |  | 
**card_payment_method_details** | [**CardPaymentMethodDetails**](CardPaymentMethodDetails.md) |  | 

## Example

```python
from pnap_payments_api.models.transaction import Transaction

# TODO update the JSON string below
json = "{}"
# create an instance of Transaction from a JSON string
transaction_instance = Transaction.from_json(json)
# print the JSON string representation of the object
print Transaction.to_json()

# convert the object into a dict
transaction_dict = transaction_instance.to_dict()
# create an instance of Transaction from a dict
transaction_form_dict = transaction.from_dict(transaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


