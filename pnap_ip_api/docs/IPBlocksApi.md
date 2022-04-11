# pnap_ip_api.IPBlocksApi

All URIs are relative to *https://api.phoenixnap.com/ips/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_blocks_get**](IPBlocksApi.md#ip_blocks_get) | **GET** /ip-blocks | List IP Blocks.
[**ip_blocks_ip_block_id_delete**](IPBlocksApi.md#ip_blocks_ip_block_id_delete) | **DELETE** /ip-blocks/{ipBlockId} | Delete IP Block.
[**ip_blocks_ip_block_id_get**](IPBlocksApi.md#ip_blocks_ip_block_id_get) | **GET** /ip-blocks/{ipBlockId} | Get IP Block.
[**ip_blocks_ip_block_id_patch**](IPBlocksApi.md#ip_blocks_ip_block_id_patch) | **PATCH** /ip-blocks/{ipBlockId} | Update IP block.
[**ip_blocks_post**](IPBlocksApi.md#ip_blocks_post) | **POST** /ip-blocks | Create an IP Block.


# **ip_blocks_get**
> [IpBlock] ip_blocks_get()

List IP Blocks.

List all IP Blocks.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.model.error import Error
from pnap_ip_api.model.ip_block import IpBlock
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/ips/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ip_blocks_api.IPBlocksApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List IP Blocks.
        api_response = api_instance.ip_blocks_get()
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[IpBlock]**](IpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Blocks list. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_blocks_ip_block_id_delete**
> DeleteIpBlockResult ip_blocks_ip_block_id_delete(ip_block_id)

Delete IP Block.

Delete an IP Block. An IP Block can only be deleted if not assigned to any resource.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.model.delete_ip_block_result import DeleteIpBlockResult
from pnap_ip_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/ips/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ip_blocks_api.IPBlocksApi(api_client)
    ip_block_id = "6047127fed34ecc3ba8402d2" # str | The IP Block identifier.

    # example passing only required values which don't have defaults set
    try:
        # Delete IP Block.
        api_response = api_instance.ip_blocks_ip_block_id_delete(ip_block_id)
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_id** | **str**| The IP Block identifier. |

### Return type

[**DeleteIpBlockResult**](DeleteIpBlockResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Block deleted. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_blocks_ip_block_id_get**
> IpBlock ip_blocks_ip_block_id_get(ip_block_id)

Get IP Block.

Get IP Block.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.model.error import Error
from pnap_ip_api.model.ip_block import IpBlock
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/ips/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ip_blocks_api.IPBlocksApi(api_client)
    ip_block_id = "6047127fed34ecc3ba8402d2" # str | The IP Block identifier.

    # example passing only required values which don't have defaults set
    try:
        # Get IP Block.
        api_response = api_instance.ip_blocks_ip_block_id_get(ip_block_id)
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_id** | **str**| The IP Block identifier. |

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific IP Block details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_blocks_ip_block_id_patch**
> IpBlock ip_blocks_ip_block_id_patch(ip_block_id)

Update IP block.

Update IP Block's details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.model.ip_block_patch import IpBlockPatch
from pnap_ip_api.model.error import Error
from pnap_ip_api.model.ip_block import IpBlock
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/ips/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ip_blocks_api.IPBlocksApi(api_client)
    ip_block_id = "6047127fed34ecc3ba8402d2" # str | The IP Block identifier.
    ip_block_patch = IpBlockPatch(
        description="Ip Block allocation.",
    ) # IpBlockPatch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update IP block.
        api_response = api_instance.ip_blocks_ip_block_id_patch(ip_block_id)
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update IP block.
        api_response = api_instance.ip_blocks_ip_block_id_patch(ip_block_id, ip_block_patch=ip_block_patch)
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_id** | **str**| The IP Block identifier. |
 **ip_block_patch** | [**IpBlockPatch**](IpBlockPatch.md)|  | [optional]

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IpBlock. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_blocks_post**
> IpBlock ip_blocks_post()

Create an IP Block.

Request an IP Block. An IP Block is a set of contiguous IPs that can be assigned to other resources such as servers.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_ip_api
from pnap_ip_api.api import ip_blocks_api
from pnap_ip_api.model.ip_block_create import IpBlockCreate
from pnap_ip_api.model.error import Error
from pnap_ip_api.model.ip_block import IpBlock
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/ips/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_ip_api.Configuration(
    host = "https://api.phoenixnap.com/ips/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ip_blocks_api.IPBlocksApi(api_client)
    ip_block_create = IpBlockCreate(
        location="PHX",
        cidr_block_size="/30",
        description="IP Block #1 used for publicly accessing server #1.",
    ) # IpBlockCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an IP Block.
        api_response = api_instance.ip_blocks_post(ip_block_create=ip_block_create)
        pprint(api_response)
    except pnap_ip_api.ApiException as e:
        print("Exception when calling IPBlocksApi->ip_blocks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_create** | [**IpBlockCreate**](IpBlockCreate.md)|  | [optional]

### Return type

[**IpBlock**](IpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | IP Block created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**406** | No server available of type server.type. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

