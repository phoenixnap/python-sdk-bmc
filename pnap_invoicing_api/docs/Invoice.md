# Invoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique resource identifier of the Invoice. | 
**number** | **str** | A user-friendly reference number assigned to the invoice. | 
**currency** | **str** | The currency of the invoice. Currently, this field should be set to &#x60;EUR&#x60; or &#x60;USD&#x60;. | 
**amount** | **float** | The invoice amount. | 
**outstanding_amount** | **float** | The invoice outstanding amount. | 
**status** | **str** | The status of the invoice. Currently, this field should be set to &#x60;PAID&#x60;, &#x60;OVERDUE&#x60;, &#x60;PROCESSING_PAYMENT&#x60;, or &#x60;UNPAID&#x60;. | 
**sent_on** | **datetime** | Date and time when the invoice was sent. | 
**due_date** | **datetime** | Date and time when the invoice payment is due. | 

## Example

```python
from pnap_invoicing_api.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


