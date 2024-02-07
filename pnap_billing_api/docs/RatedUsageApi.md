# pnap_billing_api.RatedUsageApi

All URIs are relative to *https://api.phoenixnap.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rated_usage_get**](RatedUsageApi.md#rated_usage_get) | **GET** /rated-usage | List the rated usage.
[**rated_usage_month_to_date_get**](RatedUsageApi.md#rated_usage_month_to_date_get) | **GET** /rated-usage/month-to-date | List the rated usage records for the current calendar month.


# **rated_usage_get**
> List[RatedUsageGet200ResponseInner] rated_usage_get(from_year_month, to_year_month, product_category=product_category)

List the rated usage.

Retrieves all rated usage for given time period. The information is presented as a list of rated usage records. Every record corresponds to a charge. All date & times are in UTC.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.product_category_enum import ProductCategoryEnum
from pnap_billing_api.models.rated_usage_get200_response_inner import RatedUsageGet200ResponseInner
from pnap_billing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_billing_api.Configuration(
    host = "https://api.phoenixnap.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_billing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_billing_api.RatedUsageApi(api_client)
    from_year_month = '2020-03' # str | From year month (inclusive) to filter rated usage records by.
    to_year_month = '2020-04' # str | To year month (inclusive) to filter rated usage records by.
    product_category = pnap_billing_api.ProductCategoryEnum() # ProductCategoryEnum | The product category (optional)

    try:
        # List the rated usage.
        api_response = api_instance.rated_usage_get(from_year_month, to_year_month, product_category=product_category)
        print("The response of RatedUsageApi->rated_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatedUsageApi->rated_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_year_month** | **str**| From year month (inclusive) to filter rated usage records by. | 
 **to_year_month** | **str**| To year month (inclusive) to filter rated usage records by. | 
 **product_category** | [**ProductCategoryEnum**](.md)| The product category | [optional] 

### Return type

[**List[RatedUsageGet200ResponseInner]**](RatedUsageGet200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the rated usage records for given period of months. If productCategory filter is not used returns all records. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rated_usage_month_to_date_get**
> List[RatedUsageGet200ResponseInner] rated_usage_month_to_date_get(product_category=product_category)

List the rated usage records for the current calendar month.

Retrieves all rated usage for the current calendar month. The information is presented as a list of rated usage records. Every record corresponds to a charge. All date & times are in UTC.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.product_category_enum import ProductCategoryEnum
from pnap_billing_api.models.rated_usage_get200_response_inner import RatedUsageGet200ResponseInner
from pnap_billing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_billing_api.Configuration(
    host = "https://api.phoenixnap.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_billing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_billing_api.RatedUsageApi(api_client)
    product_category = pnap_billing_api.ProductCategoryEnum() # ProductCategoryEnum | The product category (optional)

    try:
        # List the rated usage records for the current calendar month.
        api_response = api_instance.rated_usage_month_to_date_get(product_category=product_category)
        print("The response of RatedUsageApi->rated_usage_month_to_date_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatedUsageApi->rated_usage_month_to_date_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | [**ProductCategoryEnum**](.md)| The product category | [optional] 

### Return type

[**List[RatedUsageGet200ResponseInner]**](RatedUsageGet200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the rated usage records. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

