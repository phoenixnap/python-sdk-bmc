# pnap_network_api.PublicNetworksApi

All URIs are relative to *https://api.phoenixnap.com/networks/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**public_networks_get**](PublicNetworksApi.md#public_networks_get) | **GET** /public-networks | List Public Networks.
[**public_networks_network_id_delete**](PublicNetworksApi.md#public_networks_network_id_delete) | **DELETE** /public-networks/{publicNetworkId} | Delete a Public Network.
[**public_networks_network_id_get**](PublicNetworksApi.md#public_networks_network_id_get) | **GET** /public-networks/{publicNetworkId} | Get a Public Network.
[**public_networks_network_id_ip_blocks_ip_block_id_delete**](PublicNetworksApi.md#public_networks_network_id_ip_blocks_ip_block_id_delete) | **DELETE** /public-networks/{publicNetworkId}/ip-blocks/{ipBlockId} | Removes the IP Block from the Public Network.
[**public_networks_network_id_ip_blocks_post**](PublicNetworksApi.md#public_networks_network_id_ip_blocks_post) | **POST** /public-networks/{publicNetworkId}/ip-blocks | Adds an IP block to this public network.
[**public_networks_network_id_patch**](PublicNetworksApi.md#public_networks_network_id_patch) | **PATCH** /public-networks/{publicNetworkId} | Update Public Network&#39;s Details.
[**public_networks_post**](PublicNetworksApi.md#public_networks_post) | **POST** /public-networks | Create a public network.


# **public_networks_get**
> List[PublicNetwork] public_networks_get(location=location)

List Public Networks.

List all Public Networks owned by account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.public_network import PublicNetwork
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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    location = 'PHX' # str | If present will filter the result by the given location of the Public Networks. (optional)

    try:
        # List Public Networks.
        api_response = api_instance.public_networks_get(location=location)
        print("The response of PublicNetworksApi->public_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| If present will filter the result by the given location of the Public Networks. | [optional] 

### Return type

[**List[PublicNetwork]**](PublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the Public Networks owned by account. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_network_id_delete**
> public_networks_network_id_delete(public_network_id)

Delete a Public Network.

Delete Public Network. The request is accepted only if no resources are members of this network. The IP Block(s) will be freed and can be re-used in the future.

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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.

    try:
        # Delete a Public Network.
        api_instance.public_networks_network_id_delete(public_network_id)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_network_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_id** | **str**| The Public Network identifier. | 

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
**204** | The Public Network has been deleted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_network_id_get**
> PublicNetwork public_networks_network_id_get(public_network_id)

Get a Public Network.

Retrieve Public Network Details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.public_network import PublicNetwork
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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.

    try:
        # Get a Public Network.
        api_response = api_instance.public_networks_network_id_get(public_network_id)
        print("The response of PublicNetworksApi->public_networks_network_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_network_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_id** | **str**| The Public Network identifier. | 

### Return type

[**PublicNetwork**](PublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public Network Details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_network_id_ip_blocks_ip_block_id_delete**
> str public_networks_network_id_ip_blocks_ip_block_id_delete(public_network_id, ip_block_id, force=force)

Removes the IP Block from the Public Network.

Removes the IP Block from the Public Network.<br> Please ensure that no resource members within this network have any IPs assigned from the IP Block being removed.<br> Defining `force` query parameter allows resource assigned IP block to be removed anyway.  As a result, traffic addressed to any IP within the block will not be routed to this network anymore.

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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Removes the IP Block from the Public Network.
        api_response = api_instance.public_networks_network_id_ip_blocks_ip_block_id_delete(public_network_id, ip_block_id, force=force)
        print("The response of PublicNetworksApi->public_networks_network_id_ip_blocks_ip_block_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_network_id_ip_blocks_ip_block_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_id** | **str**| The Public Network identifier. | 
 **ip_block_id** | **str**| The IP Block identifier. | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The specified IP block is being removed from the Public Network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_network_id_ip_blocks_post**
> PublicNetworkIpBlock public_networks_network_id_ip_blocks_post(public_network_id, public_network_ip_block_create)

Adds an IP block to this public network.

Adds an IP block to this public network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.public_network_ip_block import PublicNetworkIpBlock
from pnap_network_api.models.public_network_ip_block_create import PublicNetworkIpBlockCreate
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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.
    public_network_ip_block_create = {"id":"60473a6115e34466c9f8f083"} # PublicNetworkIpBlockCreate | 

    try:
        # Adds an IP block to this public network.
        api_response = api_instance.public_networks_network_id_ip_blocks_post(public_network_id, public_network_ip_block_create)
        print("The response of PublicNetworksApi->public_networks_network_id_ip_blocks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_network_id_ip_blocks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_id** | **str**| The Public Network identifier. | 
 **public_network_ip_block_create** | [**PublicNetworkIpBlockCreate**](PublicNetworkIpBlockCreate.md)|  | 

### Return type

[**PublicNetworkIpBlock**](PublicNetworkIpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The specified IP block is being added to the public network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_network_id_patch**
> PublicNetwork public_networks_network_id_patch(public_network_id, public_network_modify)

Update Public Network's Details.

Update Public Network's Details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.public_network import PublicNetwork
from pnap_network_api.models.public_network_modify import PublicNetworkModify
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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.
    public_network_modify = {"name":"My public network","description":"The new description of my public network","raEnabled":false} # PublicNetworkModify | 

    try:
        # Update Public Network's Details.
        api_response = api_instance.public_networks_network_id_patch(public_network_id, public_network_modify)
        print("The response of PublicNetworksApi->public_networks_network_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_network_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_id** | **str**| The Public Network identifier. | 
 **public_network_modify** | [**PublicNetworkModify**](PublicNetworkModify.md)|  | 

### Return type

[**PublicNetwork**](PublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network successfully updated. |  -  |
**202** | Network update has been accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_networks_post**
> PublicNetwork public_networks_post(public_network_create)

Create a public network.

Create a public network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.public_network import PublicNetwork
from pnap_network_api.models.public_network_create import PublicNetworkCreate
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
    api_instance = pnap_network_api.PublicNetworksApi(api_client)
    public_network_create = {"name":"Initial public network","location":"PHX"} # PublicNetworkCreate | 

    try:
        # Create a public network.
        api_response = api_instance.public_networks_post(public_network_create)
        print("The response of PublicNetworksApi->public_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicNetworksApi->public_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_network_create** | [**PublicNetworkCreate**](PublicNetworkCreate.md)|  | 

### Return type

[**PublicNetwork**](PublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Network successfully created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

