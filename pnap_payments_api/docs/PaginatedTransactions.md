# PaginatedTransactions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Transaction]**](Transaction.md) |  | 
**limit** | **int** | Maximum number of items in the page (actual returned length can be less). | 
**offset** | **int** | The number of returned items skipped. | 
**total** | **int** | The total number of records available for retrieval. | 

## Example

```python
from pnap_payments_api.models.paginated_transactions import PaginatedTransactions

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTransactions from a JSON string
paginated_transactions_instance = PaginatedTransactions.from_json(json)
# print the JSON string representation of the object
print PaginatedTransactions.to_json()

# convert the object into a dict
paginated_transactions_dict = paginated_transactions_instance.to_dict()
# create an instance of PaginatedTransactions from a dict
paginated_transactions_form_dict = paginated_transactions.from_dict(paginated_transactions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


