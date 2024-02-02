# pnap_payments_api.TransactionsApi

All URIs are relative to *https://api.phoenixnap.com/payments/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transaction_id_get**](TransactionsApi.md#transaction_id_get) | **GET** /transactions/{transactionId} | Get Transaction.
[**transactions_get**](TransactionsApi.md#transactions_get) | **GET** /transactions | Get Transactions.


# **transaction_id_get**
> Transaction transaction_id_get(transaction_id)

Get Transaction.

Get transaction details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_payments_api
from pnap_payments_api.models.transaction import Transaction
from pnap_payments_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/payments/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_payments_api.Configuration(
    host = "https://api.phoenixnap.com/payments/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_payments_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_payments_api.TransactionsApi(api_client)
    transaction_id = '0a1b2c3d4f5g6h7i8j9k' # str | The transaction identifier.

    try:
        # Get Transaction.
        api_response = api_instance.transaction_id_get(transaction_id)
        print("The response of TransactionsApi->transaction_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transaction_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | **str**| The transaction identifier. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> PaginatedTransactions transactions_get(limit=limit, offset=offset, sort_direction=sort_direction, sort_field=sort_field, var_from=var_from, to=to)

Get Transactions.

A paginated list of client's transactions.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_payments_api
from pnap_payments_api.models.paginated_transactions import PaginatedTransactions
from pnap_payments_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/payments/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_payments_api.Configuration(
    host = "https://api.phoenixnap.com/payments/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_payments_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_payments_api.TransactionsApi(api_client)
    limit = 100 # int | The limit of the number of results returned. The number of records returned may be smaller than the limit. (optional) (default to 100)
    offset = 0 # int | The number of items to skip in the results. (optional) (default to 0)
    sort_direction = 'DESC' # str | Sort Given Field depending on the desired direction. Default sorting is descending. (optional) (default to 'DESC')
    sort_field = 'date' # str | If a sortField is requested, pagination will be done after sorting. Default sorting is by date. (optional) (default to 'date')
    var_from = '2021-04-27T16:24:57.123Z' # datetime | From the date and time (inclusive) to filter transactions by. (optional)
    to = '2021-04-29T16:24:57.123Z' # datetime | To the date and time (inclusive) to filter transactions by. (optional)

    try:
        # Get Transactions.
        api_response = api_instance.transactions_get(limit=limit, offset=offset, sort_direction=sort_direction, sort_field=sort_field, var_from=var_from, to=to)
        print("The response of TransactionsApi->transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransactionsApi->transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The limit of the number of results returned. The number of records returned may be smaller than the limit. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip in the results. | [optional] [default to 0]
 **sort_direction** | **str**| Sort Given Field depending on the desired direction. Default sorting is descending. | [optional] [default to &#39;DESC&#39;]
 **sort_field** | **str**| If a sortField is requested, pagination will be done after sorting. Default sorting is by date. | [optional] [default to &#39;date&#39;]
 **var_from** | **datetime**| From the date and time (inclusive) to filter transactions by. | [optional] 
 **to** | **datetime**| To the date and time (inclusive) to filter transactions by. | [optional] 

### Return type

[**PaginatedTransactions**](PaginatedTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Paginated list of client&#39;s transactions. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

