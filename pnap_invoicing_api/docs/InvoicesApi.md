# pnap_invoicing_api.InvoicesApi

All URIs are relative to *https://api.phoenixnap.com/invoicing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_get**](InvoicesApi.md#invoices_get) | **GET** /invoices | List invoices.
[**invoices_invoice_id_generate_pdf_post**](InvoicesApi.md#invoices_invoice_id_generate_pdf_post) | **POST** /invoices/{invoiceId}/actions/generate-pdf | Generate invoice details as PDF.
[**invoices_invoice_id_get**](InvoicesApi.md#invoices_invoice_id_get) | **GET** /invoices/{invoiceId} | Get invoice details.
[**invoices_invoice_id_pay_post**](InvoicesApi.md#invoices_invoice_id_pay_post) | **POST** /invoices/{invoiceId}/actions/pay | Pay an invoice.


# **invoices_get**
> PaginatedInvoices invoices_get(number=number, status=status, sent_on_from=sent_on_from, sent_on_to=sent_on_to, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)

List invoices.

List invoices.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_invoicing_api
from pnap_invoicing_api.models.paginated_invoices import PaginatedInvoices
from pnap_invoicing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/invoicing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_invoicing_api.Configuration(
    host = "https://api.phoenixnap.com/invoicing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_invoicing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_invoicing_api.InvoicesApi(api_client)
    number = '13218-1180326' # str | A user-friendly reference number assigned to the invoice. (optional)
    status = 'status_example' # str | Payment status of the invoice. (optional)
    sent_on_from = '2020-04-13T00:00:00.000Z' # datetime | Minimum value to filter invoices by sent on date. (optional)
    sent_on_to = '2022-04-13T00:00:00.000Z' # datetime | Maximum value to filter invoices by sent on date. (optional)
    limit = 100 # int | The limit of the number of results returned. The number of records returned may be smaller than the limit. (optional) (default to 100)
    offset = 0 # int | The number of items to skip in the results. (optional) (default to 0)
    sort_field = 'sentOn' # str | If a sortField is requested, pagination will be done after sorting. Default sorting is by number. (optional) (default to 'sentOn')
    sort_direction = 'DESC' # str | Sort Given Field depending on the desired direction. Default sorting is descending. (optional) (default to 'DESC')

    try:
        # List invoices.
        api_response = api_instance.invoices_get(number=number, status=status, sent_on_from=sent_on_from, sent_on_to=sent_on_to, limit=limit, offset=offset, sort_field=sort_field, sort_direction=sort_direction)
        print("The response of InvoicesApi->invoices_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| A user-friendly reference number assigned to the invoice. | [optional] 
 **status** | **str**| Payment status of the invoice. | [optional] 
 **sent_on_from** | **datetime**| Minimum value to filter invoices by sent on date. | [optional] 
 **sent_on_to** | **datetime**| Maximum value to filter invoices by sent on date. | [optional] 
 **limit** | **int**| The limit of the number of results returned. The number of records returned may be smaller than the limit. | [optional] [default to 100]
 **offset** | **int**| The number of items to skip in the results. | [optional] [default to 0]
 **sort_field** | **str**| If a sortField is requested, pagination will be done after sorting. Default sorting is by number. | [optional] [default to &#39;sentOn&#39;]
 **sort_direction** | **str**| Sort Given Field depending on the desired direction. Default sorting is descending. | [optional] [default to &#39;DESC&#39;]

### Return type

[**PaginatedInvoices**](PaginatedInvoices.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all invoices. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_invoice_id_generate_pdf_post**
> bytearray invoices_invoice_id_generate_pdf_post(invoice_id)

Generate invoice details as PDF.

Generate invoice details as PDF.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_invoicing_api
from pnap_invoicing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/invoicing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_invoicing_api.Configuration(
    host = "https://api.phoenixnap.com/invoicing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_invoicing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_invoicing_api.InvoicesApi(api_client)
    invoice_id = '5fa54d1e91867c03a0a7b4a4' # str | The unique resource identifier of the Invoice.

    try:
        # Generate invoice details as PDF.
        api_response = api_instance.invoices_invoice_id_generate_pdf_post(invoice_id)
        print("The response of InvoicesApi->invoices_invoice_id_generate_pdf_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_generate_pdf_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The unique resource identifier of the Invoice. | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Generated invoice details as pdf. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_invoice_id_get**
> Invoice invoices_invoice_id_get(invoice_id)

Get invoice details.

Get invoice details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_invoicing_api
from pnap_invoicing_api.models.invoice import Invoice
from pnap_invoicing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/invoicing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_invoicing_api.Configuration(
    host = "https://api.phoenixnap.com/invoicing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_invoicing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_invoicing_api.InvoicesApi(api_client)
    invoice_id = '5fa54d1e91867c03a0a7b4a4' # str | The unique resource identifier of the Invoice.

    try:
        # Get invoice details.
        api_response = api_instance.invoices_invoice_id_get(invoice_id)
        print("The response of InvoicesApi->invoices_invoice_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The unique resource identifier of the Invoice. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get invoice details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_invoice_id_pay_post**
> object invoices_invoice_id_pay_post(invoice_id, body=body)

Pay an invoice.

Manually pay an invoice.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_invoicing_api
from pnap_invoicing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/invoicing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_invoicing_api.Configuration(
    host = "https://api.phoenixnap.com/invoicing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_invoicing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_invoicing_api.InvoicesApi(api_client)
    invoice_id = '5fa54d1e91867c03a0a7b4a4' # str | The unique resource identifier of the Invoice.
    body = None # object |  (optional)

    try:
        # Pay an invoice.
        api_response = api_instance.invoices_invoice_id_pay_post(invoice_id, body=body)
        print("The response of InvoicesApi->invoices_invoice_id_pay_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->invoices_invoice_id_pay_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The unique resource identifier of the Invoice. | 
 **body** | **object**|  | [optional] 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Invoice payment is being processed |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

