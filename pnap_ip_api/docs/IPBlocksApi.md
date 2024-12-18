# pnap_ip_api.IPBlocksApi

All URIs are relative to *https://api.phoenixnap.com/ips/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ip_blocks_get**](IPBlocksApi.md#ip_blocks_get) | **GET** /ip-blocks | List IP Blocks.
[**ip_blocks_ip_block_id_delete**](IPBlocksApi.md#ip_blocks_ip_block_id_delete) | **DELETE** /ip-blocks/{ipBlockId} | Delete IP Block.
[**ip_blocks_ip_block_id_get**](IPBlocksApi.md#ip_blocks_ip_block_id_get) | **GET** /ip-blocks/{ipBlockId} | Get IP Block.
[**ip_blocks_ip_block_id_patch**](IPBlocksApi.md#ip_blocks_ip_block_id_patch) | **PATCH** /ip-blocks/{ipBlockId} | Update IP block.
[**ip_blocks_ip_block_id_tags_put**](IPBlocksApi.md#ip_blocks_ip_block_id_tags_put) | **PUT** /ip-blocks/{ipBlockId}/tags | Overwrite tags assigned for IP Block.
[**ip_blocks_post**](IPBlocksApi.md#ip_blocks_post) | **POST** /ip-blocks | Create an IP Block.


# **ip_blocks_get**
> List[IpBlock] ip_blocks_get(tag=tag)

List IP Blocks.

List all IP Blocks.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_ip_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    tag = ['[\"env.dev\",\"loc.phx\"]'] # List[str] | List of tags, in the form tagName.tagValue, to filter by. (optional)

    try:
        # List IP Blocks.
        api_response = api_instance.ip_blocks_get(tag=tag)
        print("The response of IPBlocksApi->ip_blocks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPBlocksApi->ip_blocks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**List[str]**](str.md)| List of tags, in the form tagName.tagValue, to filter by. | [optional] 

### Return type

[**List[IpBlock]**](IpBlock.md)

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
import os
import pnap_ip_api
from pnap_ip_api.models.delete_ip_block_result import DeleteIpBlockResult
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.

    try:
        # Delete IP Block.
        api_response = api_instance.ip_blocks_ip_block_id_delete(ip_block_id)
        print("The response of IPBlocksApi->ip_blocks_ip_block_id_delete:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import pnap_ip_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.

    try:
        # Get IP Block.
        api_response = api_instance.ip_blocks_ip_block_id_get(ip_block_id)
        print("The response of IPBlocksApi->ip_blocks_ip_block_id_get:\n")
        pprint(api_response)
    except Exception as e:
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
> IpBlock ip_blocks_ip_block_id_patch(ip_block_id, ip_block_patch)

Update IP block.

Update IP Block's details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_ip_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.models.ip_block_patch import IpBlockPatch
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.
    ip_block_patch = {"description":"Ip Block description"} # IpBlockPatch | 

    try:
        # Update IP block.
        api_response = api_instance.ip_blocks_ip_block_id_patch(ip_block_id, ip_block_patch)
        print("The response of IPBlocksApi->ip_blocks_ip_block_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_id** | **str**| The IP Block identifier. | 
 **ip_block_patch** | [**IpBlockPatch**](IpBlockPatch.md)|  | 

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

# **ip_blocks_ip_block_id_tags_put**
> IpBlock ip_blocks_ip_block_id_tags_put(ip_block_id, tag_assignment_request)

Overwrite tags assigned for IP Block.

Overwrites tags assigned for IP Block and unassigns any tags not part of the request.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_ip_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.models.tag_assignment_request import TagAssignmentRequest
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.
    tag_assignment_request = [pnap_ip_api.TagAssignmentRequest()] # List[TagAssignmentRequest] | 

    try:
        # Overwrite tags assigned for IP Block.
        api_response = api_instance.ip_blocks_ip_block_id_tags_put(ip_block_id, tag_assignment_request)
        print("The response of IPBlocksApi->ip_blocks_ip_block_id_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPBlocksApi->ip_blocks_ip_block_id_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_id** | **str**| The IP Block identifier. | 
 **tag_assignment_request** | [**List[TagAssignmentRequest]**](TagAssignmentRequest.md)|  | 

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
**200** | IP Blocks tags set. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_blocks_post**
> IpBlock ip_blocks_post(ip_block_create)

Create an IP Block.

Request an IP Block. An IP Block is a set of contiguous IPs that can be assigned to other resources such as servers.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_ip_api
from pnap_ip_api.models.ip_block import IpBlock
from pnap_ip_api.models.ip_block_create import IpBlockCreate
from pnap_ip_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_ip_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_ip_api.IPBlocksApi(api_client)
    ip_block_create = {"cidrBlockSize":"/24","location":"PHX"} # IpBlockCreate | 

    try:
        # Create an IP Block.
        api_response = api_instance.ip_blocks_post(ip_block_create)
        print("The response of IPBlocksApi->ip_blocks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPBlocksApi->ip_blocks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_block_create** | [**IpBlockCreate**](IpBlockCreate.md)|  | 

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
**406** | No IP Blocks available of provided cidr block size. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

