# pnap_billing_api.ProductsApi

All URIs are relative to *https://api.phoenixnap.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_availability_get**](ProductsApi.md#product_availability_get) | **GET** /product-availability | List all Product availabilities.
[**products_get**](ProductsApi.md#products_get) | **GET** /products | List all Products.


# **product_availability_get**
> List[ProductAvailability] product_availability_get(product_category=product_category, product_code=product_code, show_only_min_quantity_available=show_only_min_quantity_available, location=location, solution=solution, min_quantity=min_quantity)

List all Product availabilities.

Retrieves the list of product availability details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.location_enum import LocationEnum
from pnap_billing_api.models.product_availability import ProductAvailability
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
    api_instance = pnap_billing_api.ProductsApi(api_client)
    product_category = ['[\"SERVER\"]'] # List[str] | Product category. Currently only SERVER category is supported. (optional)
    product_code = ['[\"d1.c1.small\"]'] # List[str] |  (optional)
    show_only_min_quantity_available = True # bool | Show only locations where product with requested quantity is available or all locations where product is offered. (optional) (default to True)
    location = [pnap_billing_api.LocationEnum()] # List[LocationEnum] |  (optional)
    solution = ['[\"SERVER_RANCHER\"]'] # List[str] |  (optional)
    min_quantity = 2 # float | Minimal quantity of product needed. Minimum, maximum and default values might differ for different products. For servers, they are 1, 10 and 1 respectively. (optional)

    try:
        # List all Product availabilities.
        api_response = api_instance.product_availability_get(product_category=product_category, product_code=product_code, show_only_min_quantity_available=show_only_min_quantity_available, location=location, solution=solution, min_quantity=min_quantity)
        print("The response of ProductsApi->product_availability_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->product_availability_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | [**List[str]**](str.md)| Product category. Currently only SERVER category is supported. | [optional] 
 **product_code** | [**List[str]**](str.md)|  | [optional] 
 **show_only_min_quantity_available** | **bool**| Show only locations where product with requested quantity is available or all locations where product is offered. | [optional] [default to True]
 **location** | [**List[LocationEnum]**](LocationEnum.md)|  | [optional] 
 **solution** | [**List[str]**](str.md)|  | [optional] 
 **min_quantity** | **float**| Minimal quantity of product needed. Minimum, maximum and default values might differ for different products. For servers, they are 1, 10 and 1 respectively. | [optional] 

### Return type

[**List[ProductAvailability]**](ProductAvailability.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all product availabilities. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get**
> List[ProductsGet200ResponseInner] products_get(product_code=product_code, product_category=product_category, sku_code=sku_code, location=location)

List all Products.

Retrieves all Products.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.products_get200_response_inner import ProductsGet200ResponseInner
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
    api_instance = pnap_billing_api.ProductsApi(api_client)
    product_code = 's1.c1.small' # str |  (optional)
    product_category = 'SERVER' # str |  (optional)
    sku_code = 'xxx-xxx-xxx' # str |  (optional)
    location = 'PHX' # str |  (optional)

    try:
        # List all Products.
        api_response = api_instance.products_get(product_code=product_code, product_category=product_category, sku_code=sku_code, location=location)
        print("The response of ProductsApi->products_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->products_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_code** | **str**|  | [optional] 
 **product_category** | **str**|  | [optional] 
 **sku_code** | **str**|  | [optional] 
 **location** | **str**|  | [optional] 

### Return type

[**List[ProductsGet200ResponseInner]**](ProductsGet200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the products. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

