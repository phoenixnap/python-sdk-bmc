# pnap_network_api.BGPPeerGroupsApi

All URIs are relative to *https://api.phoenixnap.com/networks/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bgp_peer_groups_get**](BGPPeerGroupsApi.md#bgp_peer_groups_get) | **GET** /bgp-peer-groups | List BGP Peer Groups.
[**bgp_peer_groups_peer_group_id_delete**](BGPPeerGroupsApi.md#bgp_peer_groups_peer_group_id_delete) | **DELETE** /bgp-peer-groups/{bgpPeerGroupId} | Delete a BGP Peer Group.
[**bgp_peer_groups_peer_group_id_get**](BGPPeerGroupsApi.md#bgp_peer_groups_peer_group_id_get) | **GET** /bgp-peer-groups/{bgpPeerGroupId} | Get a BGP Peer Group.
[**bgp_peer_groups_peer_group_id_patch**](BGPPeerGroupsApi.md#bgp_peer_groups_peer_group_id_patch) | **PATCH** /bgp-peer-groups/{bgpPeerGroupId} | Modify a BGP Peer Group.
[**bgp_peer_groups_post**](BGPPeerGroupsApi.md#bgp_peer_groups_post) | **POST** /bgp-peer-groups | Create a BGP Peer Group.


# **bgp_peer_groups_get**
> List[BgpPeerGroup] bgp_peer_groups_get(location=location)

List BGP Peer Groups.

List all BGP Peer Groups owned by account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
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
    api_instance = pnap_network_api.BGPPeerGroupsApi(api_client)
    location = 'PHX' # str | If present will filter the result by the given location of the BGP Peer Group. (optional)

    try:
        # List BGP Peer Groups.
        api_response = api_instance.bgp_peer_groups_get(location=location)
        print("The response of BGPPeerGroupsApi->bgp_peer_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPPeerGroupsApi->bgp_peer_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| If present will filter the result by the given location of the BGP Peer Group. | [optional] 

### Return type

[**List[BgpPeerGroup]**](BgpPeerGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all BGP Peer Groups owned by account. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_peer_groups_peer_group_id_delete**
> BgpPeerGroup bgp_peer_groups_peer_group_id_delete(bgp_peer_group_id)

Delete a BGP Peer Group.

Deletes BGP Peer Group by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
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
    api_instance = pnap_network_api.BGPPeerGroupsApi(api_client)
    bgp_peer_group_id = '603f3b2cfcaf050643b89a4b' # str | The BGP peer group ID.

    try:
        # Delete a BGP Peer Group.
        api_response = api_instance.bgp_peer_groups_peer_group_id_delete(bgp_peer_group_id)
        print("The response of BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_peer_group_id** | **str**| The BGP peer group ID. | 

### Return type

[**BgpPeerGroup**](BgpPeerGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request to delete BGP Peer Group is accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_peer_groups_peer_group_id_get**
> BgpPeerGroup bgp_peer_groups_peer_group_id_get(bgp_peer_group_id)

Get a BGP Peer Group.

Retrieves BGP Peer Group by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
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
    api_instance = pnap_network_api.BGPPeerGroupsApi(api_client)
    bgp_peer_group_id = '603f3b2cfcaf050643b89a4b' # str | The BGP peer group ID.

    try:
        # Get a BGP Peer Group.
        api_response = api_instance.bgp_peer_groups_peer_group_id_get(bgp_peer_group_id)
        print("The response of BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_peer_group_id** | **str**| The BGP peer group ID. | 

### Return type

[**BgpPeerGroup**](BgpPeerGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | BGP Peer Group by ID. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_peer_groups_peer_group_id_patch**
> BgpPeerGroup bgp_peer_groups_peer_group_id_patch(bgp_peer_group_id, bgp_peer_group_patch)

Modify a BGP Peer Group.

Modifies BGP Peer Group by ID.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
from pnap_network_api.models.bgp_peer_group_patch import BgpPeerGroupPatch
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
    api_instance = pnap_network_api.BGPPeerGroupsApi(api_client)
    bgp_peer_group_id = '603f3b2cfcaf050643b89a4b' # str | The BGP peer group ID.
    bgp_peer_group_patch = {"password":"E!73423ghhjfge46","advertisedRoutes":"DEFAULT"} # BgpPeerGroupPatch | 

    try:
        # Modify a BGP Peer Group.
        api_response = api_instance.bgp_peer_groups_peer_group_id_patch(bgp_peer_group_id, bgp_peer_group_patch)
        print("The response of BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPPeerGroupsApi->bgp_peer_groups_peer_group_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_peer_group_id** | **str**| The BGP peer group ID. | 
 **bgp_peer_group_patch** | [**BgpPeerGroupPatch**](BgpPeerGroupPatch.md)|  | 

### Return type

[**BgpPeerGroup**](BgpPeerGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request to modify BGP Peer Group is accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bgp_peer_groups_post**
> BgpPeerGroup bgp_peer_groups_post(bgp_peer_group_create)

Create a BGP Peer Group.

Create a BGP Peer Group.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_api
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup
from pnap_network_api.models.bgp_peer_group_create import BgpPeerGroupCreate
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
    api_instance = pnap_network_api.BGPPeerGroupsApi(api_client)
    bgp_peer_group_create = {"location":"PHX","asn":65401,"advertisedRoutes":"NONE"} # BgpPeerGroupCreate | 

    try:
        # Create a BGP Peer Group.
        api_response = api_instance.bgp_peer_groups_post(bgp_peer_group_create)
        print("The response of BGPPeerGroupsApi->bgp_peer_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPPeerGroupsApi->bgp_peer_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_peer_group_create** | [**BgpPeerGroupCreate**](BgpPeerGroupCreate.md)|  | 

### Return type

[**BgpPeerGroup**](BgpPeerGroup.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request to create BGP Peer Group is accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**406** | Creation of BGP Peer Group in location is presently not available. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

