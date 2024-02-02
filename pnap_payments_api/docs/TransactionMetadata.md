# TransactionMetadata

Transaction's metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **str** | The Invoice ID that this transaction pertains to. | 
**invoice_number** | **str** | A user-friendly reference number assigned to the invoice that this transaction pertains to. | [optional] 
**is_auto_charge** | **bool** | Whether this transaction was triggered by an auto charge or not. | 

## Example

```python
from pnap_payments_api.models.transaction_metadata import TransactionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionMetadata from a JSON string
transaction_metadata_instance = TransactionMetadata.from_json(json)
# print the JSON string representation of the object
print TransactionMetadata.to_json()

# convert the object into a dict
transaction_metadata_dict = transaction_metadata_instance.to_dict()
# create an instance of TransactionMetadata from a dict
transaction_metadata_form_dict = transaction_metadata.from_dict(transaction_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


