# pnap_network_api.PrivateNetworksApi

All URIs are relative to *https://api.phoenixnap.com/networks/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**private_networks_get**](PrivateNetworksApi.md#private_networks_get) | **GET** /private-networks | List Private Networks.
[**private_networks_network_id_delete**](PrivateNetworksApi.md#private_networks_network_id_delete) | **DELETE** /private-networks/{privateNetworkId} | Delete a Private Network.
[**private_networks_network_id_get**](PrivateNetworksApi.md#private_networks_network_id_get) | **GET** /private-networks/{privateNetworkId} | Get a Private Network.
[**private_networks_network_id_put**](PrivateNetworksApi.md#private_networks_network_id_put) | **PUT** /private-networks/{privateNetworkId} | Update a Private Network.
[**private_networks_post**](PrivateNetworksApi.md#private_networks_post) | **POST** /private-networks | Create a Private Network.


# **private_networks_get**
> List[PrivateNetwork] private_networks_get(location=location)

List Private Networks.

List all Private Networks owned by account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.private_network import PrivateNetwork
from pnap_network_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/networks/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_api.Configuration(
    host = "https://api.phoenixnap.com/networks/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_api.PrivateNetworksApi(api_client)
    location = 'PHX' # str | If present will filter the result by the given location of the Private Networks. (optional)

    try:
        # List Private Networks.
        api_response = api_instance.private_networks_get(location=location)
        print("The response of PrivateNetworksApi->private_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->private_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| If present will filter the result by the given location of the Private Networks. | [optional] 

### Return type

[**List[PrivateNetwork]**](PrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the Private Networks owned by account. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_networks_network_id_delete**
> private_networks_network_id_delete(private_network_id)

Delete a Private Network.

Delete Private Network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/networks/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_api.Configuration(
    host = "https://api.phoenixnap.com/networks/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_api.PrivateNetworksApi(api_client)
    private_network_id = '603f3b2cfcaf050643b89a4b' # str | The private network identifier.

    try:
        # Delete a Private Network.
        api_instance.private_networks_network_id_delete(private_network_id)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->private_networks_network_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_network_id** | **str**| The private network identifier. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Private Network deleted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_networks_network_id_get**
> PrivateNetwork private_networks_network_id_get(private_network_id)

Get a Private Network.

Retrieve Private Network Details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.private_network import PrivateNetwork
from pnap_network_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/networks/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_api.Configuration(
    host = "https://api.phoenixnap.com/networks/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_api.PrivateNetworksApi(api_client)
    private_network_id = '603f3b2cfcaf050643b89a4b' # str | The private network identifier.

    try:
        # Get a Private Network.
        api_response = api_instance.private_networks_network_id_get(private_network_id)
        print("The response of PrivateNetworksApi->private_networks_network_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->private_networks_network_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_network_id** | **str**| The private network identifier. | 

### Return type

[**PrivateNetwork**](PrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Network Details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_networks_network_id_put**
> PrivateNetwork private_networks_network_id_put(private_network_id, private_network_modify)

Update a Private Network.

Update Private Network Details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.private_network import PrivateNetwork
from pnap_network_api.models.private_network_modify import PrivateNetworkModify
from pnap_network_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/networks/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_api.Configuration(
    host = "https://api.phoenixnap.com/networks/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_api.PrivateNetworksApi(api_client)
    private_network_id = '603f3b2cfcaf050643b89a4b' # str | The private network identifier.
    private_network_modify = {"name":"My Default Backend Network","description":"My Default Backend Network","locationDefault":true} # PrivateNetworkModify | 

    try:
        # Update a Private Network.
        api_response = api_instance.private_networks_network_id_put(private_network_id, private_network_modify)
        print("The response of PrivateNetworksApi->private_networks_network_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->private_networks_network_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_network_id** | **str**| The private network identifier. | 
 **private_network_modify** | [**PrivateNetworkModify**](PrivateNetworkModify.md)|  | 

### Return type

[**PrivateNetwork**](PrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Network successfully updated. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **private_networks_post**
> PrivateNetwork private_networks_post(private_network_create, force=force)

Create a Private Network.

Create a Private Network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.private_network import PrivateNetwork
from pnap_network_api.models.private_network_create import PrivateNetworkCreate
from pnap_network_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/networks/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_api.Configuration(
    host = "https://api.phoenixnap.com/networks/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_api.PrivateNetworksApi(api_client)
    private_network_create = {"name":"My Default Backend Network","location":"PHX","locationDefault":true,"description":"My Default Backend Network","cidr":"10.0.0.0/24"} # PrivateNetworkCreate | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Create a Private Network.
        api_response = api_instance.private_networks_post(private_network_create, force=force)
        print("The response of PrivateNetworksApi->private_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateNetworksApi->private_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **private_network_create** | [**PrivateNetworkCreate**](PrivateNetworkCreate.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**PrivateNetwork**](PrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Private Network successfully created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

