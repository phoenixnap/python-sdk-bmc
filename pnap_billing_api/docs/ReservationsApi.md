# pnap_billing_api.ReservationsApi

All URIs are relative to *https://api.phoenixnap.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reservations_get**](ReservationsApi.md#reservations_get) | **GET** /reservations | List all Reservations.
[**reservations_post**](ReservationsApi.md#reservations_post) | **POST** /reservations | Create a reservation.
[**reservations_reservation_id_actions_auto_renew_disable_post**](ReservationsApi.md#reservations_reservation_id_actions_auto_renew_disable_post) | **POST** /reservations/{reservationId}/actions/auto-renew/disable | Disable auto-renewal for reservation by id.
[**reservations_reservation_id_actions_auto_renew_enable_post**](ReservationsApi.md#reservations_reservation_id_actions_auto_renew_enable_post) | **POST** /reservations/{reservationId}/actions/auto-renew/enable | Enable auto-renewal for unexpired reservation by reservation id.
[**reservations_reservation_id_actions_convert_post**](ReservationsApi.md#reservations_reservation_id_actions_convert_post) | **POST** /reservations/{reservationId}/actions/convert | Convert reservation pricing model by reservation ID.
[**reservations_reservation_id_get**](ReservationsApi.md#reservations_reservation_id_get) | **GET** /reservations/{reservationId} | Get a reservation.


# **reservations_get**
> List[Reservation] reservations_get(product_category=product_category)

List all Reservations.

Retrieves all reservations associated with the authenticated account. All date & times are in UTC.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.product_category_enum import ProductCategoryEnum
from pnap_billing_api.models.reservation import Reservation
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    product_category = pnap_billing_api.ProductCategoryEnum() # ProductCategoryEnum | The product category (optional)

    try:
        # List all Reservations.
        api_response = api_instance.reservations_get(product_category=product_category)
        print("The response of ReservationsApi->reservations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_category** | [**ProductCategoryEnum**](.md)| The product category | [optional] 

### Return type

[**List[Reservation]**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all reservations is returned if productCategory parameter is not specified. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reservations_post**
> Reservation reservations_post(reservation_request=reservation_request)

Create a reservation.

Creates new package reservation for authenticated account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.reservation import Reservation
from pnap_billing_api.models.reservation_request import ReservationRequest
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    reservation_request = pnap_billing_api.ReservationRequest() # ReservationRequest |  (optional)

    try:
        # Create a reservation.
        api_response = api_instance.reservations_post(reservation_request=reservation_request)
        print("The response of ReservationsApi->reservations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_request** | [**ReservationRequest**](ReservationRequest.md)|  | [optional] 

### Return type

[**Reservation**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returns created reservation instance. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reservations_reservation_id_actions_auto_renew_disable_post**
> Reservation reservations_reservation_id_actions_auto_renew_disable_post(reservation_id, reservation_auto_renew_disable_request=reservation_auto_renew_disable_request)

Disable auto-renewal for reservation by id.

Disable auto-renewal for reservation by reservation id.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.reservation import Reservation
from pnap_billing_api.models.reservation_auto_renew_disable_request import ReservationAutoRenewDisableRequest
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    reservation_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The reservation's ID.
    reservation_auto_renew_disable_request = pnap_billing_api.ReservationAutoRenewDisableRequest() # ReservationAutoRenewDisableRequest |  (optional)

    try:
        # Disable auto-renewal for reservation by id.
        api_response = api_instance.reservations_reservation_id_actions_auto_renew_disable_post(reservation_id, reservation_auto_renew_disable_request=reservation_auto_renew_disable_request)
        print("The response of ReservationsApi->reservations_reservation_id_actions_auto_renew_disable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_reservation_id_actions_auto_renew_disable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| The reservation&#39;s ID. | 
 **reservation_auto_renew_disable_request** | [**ReservationAutoRenewDisableRequest**](ReservationAutoRenewDisableRequest.md)|  | [optional] 

### Return type

[**Reservation**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reservation with auto-renewal disabled |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**409** | The request failed since the resource was not in the correct state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reservations_reservation_id_actions_auto_renew_enable_post**
> Reservation reservations_reservation_id_actions_auto_renew_enable_post(reservation_id)

Enable auto-renewal for unexpired reservation by reservation id.

Enable auto-renewal for unexpired reservation by reservation id.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.reservation import Reservation
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    reservation_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The reservation's ID.

    try:
        # Enable auto-renewal for unexpired reservation by reservation id.
        api_response = api_instance.reservations_reservation_id_actions_auto_renew_enable_post(reservation_id)
        print("The response of ReservationsApi->reservations_reservation_id_actions_auto_renew_enable_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_reservation_id_actions_auto_renew_enable_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| The reservation&#39;s ID. | 

### Return type

[**Reservation**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reservation with auto-renewal enabled. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**409** | The request failed since the resource was not in the correct state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reservations_reservation_id_actions_convert_post**
> Reservation reservations_reservation_id_actions_convert_post(reservation_id, reservation_request=reservation_request)

Convert reservation pricing model by reservation ID.

Convert reservation pricing model by reservation id.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.reservation import Reservation
from pnap_billing_api.models.reservation_request import ReservationRequest
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    reservation_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The reservation's ID.
    reservation_request = pnap_billing_api.ReservationRequest() # ReservationRequest |  (optional)

    try:
        # Convert reservation pricing model by reservation ID.
        api_response = api_instance.reservations_reservation_id_actions_convert_post(reservation_id, reservation_request=reservation_request)
        print("The response of ReservationsApi->reservations_reservation_id_actions_convert_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_reservation_id_actions_convert_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| The reservation&#39;s ID. | 
 **reservation_request** | [**ReservationRequest**](ReservationRequest.md)|  | [optional] 

### Return type

[**Reservation**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Converted reservation. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reservations_reservation_id_get**
> Reservation reservations_reservation_id_get(reservation_id)

Get a reservation.

Retrieves the reservations with the specified identifier. All date & times are in UTC.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.reservation import Reservation
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
    api_instance = pnap_billing_api.ReservationsApi(api_client)
    reservation_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The reservation's ID.

    try:
        # Get a reservation.
        api_response = api_instance.reservations_reservation_id_get(reservation_id)
        print("The response of ReservationsApi->reservations_reservation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReservationsApi->reservations_reservation_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**| The reservation&#39;s ID. | 

### Return type

[**Reservation**](Reservation.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matched reservation. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**409** | The request failed since the resource was not in the correct state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

