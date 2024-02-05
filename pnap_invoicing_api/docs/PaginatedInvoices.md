# PaginatedInvoices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Maximum number of items in the page (actual returned length can be less). | 
**offset** | **int** | The number of returned items skipped. | 
**total** | **int** | The total number of records available for retrieval. | 
**results** | [**List[Invoice]**](Invoice.md) |  | 

## Example

```python
from pnap_invoicing_api.models.paginated_invoices import PaginatedInvoices

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedInvoices from a JSON string
paginated_invoices_instance = PaginatedInvoices.from_json(json)
# print the JSON string representation of the object
print PaginatedInvoices.to_json()

# convert the object into a dict
paginated_invoices_dict = paginated_invoices_instance.to_dict()
# create an instance of PaginatedInvoices from a dict
paginated_invoices_form_dict = paginated_invoices.from_dict(paginated_invoices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


