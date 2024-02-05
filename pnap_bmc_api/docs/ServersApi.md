# pnap_bmc_api.ServersApi

All URIs are relative to *https://api.phoenixnap.com/bmc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_private_network**](ServersApi.md#delete_private_network) | **DELETE** /servers/{serverId}/network-configuration/private-network-configuration/private-networks/{privateNetworkId} | Removes the server from private network.
[**servers_get**](ServersApi.md#servers_get) | **GET** /servers | List servers.
[**servers_post**](ServersApi.md#servers_post) | **POST** /servers | Create new server.
[**servers_server_id_actions_deprovision_post**](ServersApi.md#servers_server_id_actions_deprovision_post) | **POST** /servers/{serverId}/actions/deprovision | Deprovision a server.
[**servers_server_id_actions_power_off_post**](ServersApi.md#servers_server_id_actions_power_off_post) | **POST** /servers/{serverId}/actions/power-off | Power off server.
[**servers_server_id_actions_power_on_post**](ServersApi.md#servers_server_id_actions_power_on_post) | **POST** /servers/{serverId}/actions/power-on | Power on server.
[**servers_server_id_actions_provision_post**](ServersApi.md#servers_server_id_actions_provision_post) | **POST** /servers/{serverId}/actions/provision | Provision server.
[**servers_server_id_actions_reboot_post**](ServersApi.md#servers_server_id_actions_reboot_post) | **POST** /servers/{serverId}/actions/reboot | Reboot server.
[**servers_server_id_actions_reserve_post**](ServersApi.md#servers_server_id_actions_reserve_post) | **POST** /servers/{serverId}/actions/reserve | Reserve server.
[**servers_server_id_actions_reset_post**](ServersApi.md#servers_server_id_actions_reset_post) | **POST** /servers/{serverId}/actions/reset | Reset server.
[**servers_server_id_actions_shutdown_post**](ServersApi.md#servers_server_id_actions_shutdown_post) | **POST** /servers/{serverId}/actions/shutdown | Shutdown server.
[**servers_server_id_delete**](ServersApi.md#servers_server_id_delete) | **DELETE** /servers/{serverId} | Delete server.
[**servers_server_id_get**](ServersApi.md#servers_server_id_get) | **GET** /servers/{serverId} | Get server.
[**servers_server_id_ip_blocks_ip_block_id_delete**](ServersApi.md#servers_server_id_ip_blocks_ip_block_id_delete) | **DELETE** /servers/{serverId}/network-configuration/ip-block-configurations/ip-blocks/{ipBlockId} | Unassign IP Block from Server.
[**servers_server_id_ip_blocks_post**](ServersApi.md#servers_server_id_ip_blocks_post) | **POST** /servers/{serverId}/network-configuration/ip-block-configurations/ip-blocks | Assign IP Block to Server.
[**servers_server_id_patch**](ServersApi.md#servers_server_id_patch) | **PATCH** /servers/{serverId} | Patch a Server.
[**servers_server_id_private_networks_patch**](ServersApi.md#servers_server_id_private_networks_patch) | **PATCH** /servers/{serverId}/network-configuration/private-network-configuration/private-networks/{privateNetworkId} | Updates the server&#39;s private network&#39;s IP addresses
[**servers_server_id_private_networks_post**](ServersApi.md#servers_server_id_private_networks_post) | **POST** /servers/{serverId}/network-configuration/private-network-configuration/private-networks | Adds the server to a private network.
[**servers_server_id_public_networks_delete**](ServersApi.md#servers_server_id_public_networks_delete) | **DELETE** /servers/{serverId}/network-configuration/public-network-configuration/public-networks/{publicNetworkId} | Removes the server from the Public Network
[**servers_server_id_public_networks_patch**](ServersApi.md#servers_server_id_public_networks_patch) | **PATCH** /servers/{serverId}/network-configuration/public-network-configuration/public-networks/{publicNetworkId} | Updates the server&#39;s public network&#39;s IP addresses.
[**servers_server_id_public_networks_post**](ServersApi.md#servers_server_id_public_networks_post) | **POST** /servers/{serverId}/network-configuration/public-network-configuration/public-networks | Adds the server to a Public Network.
[**servers_server_id_tags_put**](ServersApi.md#servers_server_id_tags_put) | **PUT** /servers/{serverId}/tags | Overwrite tags assigned for Server.


# **delete_private_network**
> str delete_private_network(server_id, private_network_id)

Removes the server from private network.

Removes the server from private network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. <b>This is an advanced network action that can make your server completely unavailable over any network. Make sure this server is reachable over remote console for guaranteed access in case of misconfiguration.</b>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    private_network_id = '603f3b2cfcaf050643b89a4b' # str | The private network identifier.

    try:
        # Removes the server from private network.
        api_response = api_instance.delete_private_network(server_id, private_network_id)
        print("The response of ServersApi->delete_private_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->delete_private_network: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **private_network_id** | **str**| The private network identifier. | 

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
**202** | The server is being removed from the specified private network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_get**
> List[Server] servers_get(tag=tag)

List servers.

List all servers owned by account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    tag = ['env.dev'] # List[str] | A list of query parameters related to tags in the form of tagName.tagValue (optional)

    try:
        # List servers.
        api_response = api_instance.servers_get(tag=tag)
        print("The response of ServersApi->servers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**List[str]**](str.md)| A list of query parameters related to tags in the form of tagName.tagValue | [optional] 

### Return type

[**List[Server]**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the servers owned by account. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_post**
> Server servers_post(server_create, force=force)

Create new server.

Create (request) a new server for the account. Server DNS will be configured to access Google's public DNS at 8.8.8.8 . Note that the product availability API can be used prior to doing the provision request. Refer to https://developers.phoenixnap.com/docs/bmc-billing/1/routes/product-availability/get.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.models.server_create import ServerCreate
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_create = {"hostname":"my-server-1","location":"PHX","os":"ubuntu/bionic","type":"s1.c1.small"} # ServerCreate | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Create new server.
        api_response = api_instance.servers_post(server_create, force=force)
        print("The response of ServersApi->servers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_create** | [**ServerCreate**](ServerCreate.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request to create server is accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**406** | There are currently no servers available for the selected instance type. Check the availability of instance types at specific locations by using the &#39;product availability API GET&#39; call. Refer to https://developers.phoenixnap.com/docs/bmc-billing/1/routes/product-availability/get. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_deprovision_post**
> str servers_server_id_actions_deprovision_post(server_id, relinquish_ip_block)

Deprovision a server.

Deprovision the server. Supports advanced deprovision configuration.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.relinquish_ip_block import RelinquishIpBlock
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    relinquish_ip_block = {"deleteIpBlocks":false} # RelinquishIpBlock | 

    try:
        # Deprovision a server.
        api_response = api_instance.servers_server_id_actions_deprovision_post(server_id, relinquish_ip_block)
        print("The response of ServersApi->servers_server_id_actions_deprovision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_deprovision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **relinquish_ip_block** | [**RelinquishIpBlock**](RelinquishIpBlock.md)|  | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The server has been deprovisioned and related network setup is being updated. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_power_off_post**
> ActionResult servers_server_id_actions_power_off_post(server_id)

Power off server.

Power off specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.action_result import ActionResult
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Power off server.
        api_response = api_instance.servers_server_id_actions_power_off_post(server_id)
        print("The response of ServersApi->servers_server_id_actions_power_off_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_power_off_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Powering off server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_power_on_post**
> ActionResult servers_server_id_actions_power_on_post(server_id)

Power on server.

Power on specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.action_result import ActionResult
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Power on server.
        api_response = api_instance.servers_server_id_actions_power_on_post(server_id)
        print("The response of ServersApi->servers_server_id_actions_power_on_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_power_on_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Powering on server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_provision_post**
> Server servers_server_id_actions_provision_post(server_id, server_provision, force=force)

Provision server.

Provision reserved server. Server DNS will be configured to access Google's public DNS at 8.8.8.8.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.models.server_provision import ServerProvision
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_provision = {"hostname":"my-server-1","os":"ubuntu/bionic"} # ServerProvision | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Provision server.
        api_response = api_instance.servers_server_id_actions_provision_post(server_id, server_provision, force=force)
        print("The response of ServersApi->servers_server_id_actions_provision_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_provision_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_provision** | [**ServerProvision**](ServerProvision.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Request to provision server is accepted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**406** | No server available of type server type. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_reboot_post**
> ActionResult servers_server_id_actions_reboot_post(server_id)

Reboot server.

Reboot specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.action_result import ActionResult
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Reboot server.
        api_response = api_instance.servers_server_id_actions_reboot_post(server_id)
        print("The response of ServersApi->servers_server_id_actions_reboot_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reboot_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rebooting server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_reserve_post**
> Server servers_server_id_actions_reserve_post(server_id, server_reserve)

Reserve server.

Reserve specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.models.server_reserve import ServerReserve
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_reserve = {"pricingModel":"ONE_MONTH_RESERVATION"} # ServerReserve | 

    try:
        # Reserve server.
        api_response = api_instance.servers_server_id_actions_reserve_post(server_id, server_reserve)
        print("The response of ServersApi->servers_server_id_actions_reserve_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reserve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_reserve** | [**ServerReserve**](ServerReserve.md)|  | 

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reserved server details. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_reset_post**
> ResetResult servers_server_id_actions_reset_post(server_id, server_reset)

Reset server.

Deprecated: Reset specific server. Reset only supports network configurations of type 'private network' or 'IP blocks'. As an alternative, the suggested action is to deprovision the server and provision a new one with the same configuration.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.reset_result import ResetResult
from pnap_bmc_api.models.server_reset import ServerReset
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_reset = {"installDefaultSshKeys":true,"sshKeys":["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDF9LdAFElNCi7JoWh6KUcchrJ2Gac1aqGRPpdZNowObpRtmiRCecAMb7bUgNAaNfcmwiQi7tos9TlnFgprIcfMWb8MSs3ABYHmBgqEEt3RWYf0fAc9CsIpJdMCUG28TPGTlRXCEUVNKgLMdcseAlJoGp1CgbHWIN65fB3he3kAZcfpPn5mapV0tsl2p+ZyuAGRYdn5dJv2RZDHUZBkOeUobwsij+weHCKAFmKQKtCP7ybgVHaQjAPrj8MGnk1jBbjDt5ws+Be+9JNjQJee9zCKbAOsIo3i+GcUIkrw5jxPU/RTGlWBcemPaKHdciSzGcjWboapzIy49qypQhZe1U75 user@my_ip"],"sshKeyIds":["5fa54d1e91867c03a0a7b4a4"]} # ServerReset | 

    try:
        # Reset server.
        api_response = api_instance.servers_server_id_actions_reset_post(server_id, server_reset)
        print("The response of ServersApi->servers_server_id_actions_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_reset** | [**ServerReset**](ServerReset.md)|  | 

### Return type

[**ResetResult**](ResetResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resetting server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_shutdown_post**
> ActionResult servers_server_id_actions_shutdown_post(server_id)

Shutdown server.

Shut down specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.action_result import ActionResult
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Shutdown server.
        api_response = api_instance.servers_server_id_actions_shutdown_post(server_id)
        print("The response of ServersApi->servers_server_id_actions_shutdown_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_actions_shutdown_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**ActionResult**](ActionResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Shutting down server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_delete**
> DeleteResult servers_server_id_delete(server_id)

Delete server.

Deprovision specific server. Any IP blocks assigned to this server will also be relinquished and deleted. Deprecated: see /servers/{serverId}/actions/deprovision

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.delete_result import DeleteResult
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Delete server.
        api_response = api_instance.servers_server_id_delete(server_id)
        print("The response of ServersApi->servers_server_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**DeleteResult**](DeleteResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deprovisioned server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_get**
> Server servers_server_id_get(server_id)

Get server.

Get server properties.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.

    try:
        # Get server.
        api_response = api_instance.servers_server_id_get(server_id)
        print("The response of ServersApi->servers_server_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific server details. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_ip_blocks_ip_block_id_delete**
> str servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id, relinquish_ip_block)

Unassign IP Block from Server.

Removes the IP block from the server. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. <b>This is an advanced network action that can make your server completely unavailable over any network. Make sure this server is reachable over remote console for guaranteed access in case of misconfiguration.</b>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.relinquish_ip_block import RelinquishIpBlock
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    ip_block_id = '6047127fed34ecc3ba8402d2' # str | The IP Block identifier.
    relinquish_ip_block = {"deleteIpBlocks":false} # RelinquishIpBlock | 

    try:
        # Unassign IP Block from Server.
        api_response = api_instance.servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id, relinquish_ip_block)
        print("The response of ServersApi->servers_server_id_ip_blocks_ip_block_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_ip_block_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **ip_block_id** | **str**| The IP Block identifier. | 
 **relinquish_ip_block** | [**RelinquishIpBlock**](RelinquishIpBlock.md)|  | 

### Return type

**str**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The specified IP block is being removed from the server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_ip_blocks_post**
> ServerIpBlock servers_server_id_ip_blocks_post(server_id, server_ip_block)

Assign IP Block to Server.

Adds an IP block to this server. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-server-with-public-ip-block#ftoc-heading-2' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server_ip_block import ServerIpBlock
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_ip_block = {"id":"60473a6115e34466c9f8f083"} # ServerIpBlock | 

    try:
        # Assign IP Block to Server.
        api_response = api_instance.servers_server_id_ip_blocks_post(server_id, server_ip_block)
        print("The response of ServersApi->servers_server_id_ip_blocks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_ip_block** | [**ServerIpBlock**](ServerIpBlock.md)|  | 

### Return type

[**ServerIpBlock**](ServerIpBlock.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The specified IP block is being added to the server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_patch**
> Server servers_server_id_patch(server_id, server_patch)

Patch a Server.

Any changes to the hostname or description using the BMC API will reflect solely in the BMC API and portal. The changes are intended to keep the BMC data up to date with your server. We do not have access to your server's settings. Local changes to the server's hostname will not be reflected in the API or portal.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.models.server_patch import ServerPatch
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_patch = {"description":"My custom server edit","hostname":"my-server"} # ServerPatch | 

    try:
        # Patch a Server.
        api_response = api_instance.servers_server_id_patch(server_id, server_patch)
        print("The response of ServersApi->servers_server_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_patch** | [**ServerPatch**](ServerPatch.md)|  | 

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_private_networks_patch**
> ServerPrivateNetwork servers_server_id_private_networks_patch(server_id, private_network_id, server_network_update, force=force)

Updates the server's private network's IP addresses

IP address changes intended to keep the BMC data up to date with server's operating system. We do not have access to the server's operating system and therefore manual configuration is required to apply the changes on the host. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-6' target='_blank'>here</a>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server_network_update import ServerNetworkUpdate
from pnap_bmc_api.models.server_private_network import ServerPrivateNetwork
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    private_network_id = '603f3b2cfcaf050643b89a4b' # str | The private network identifier.
    server_network_update = {"ips":["10.0.0.1","10.0.0.2"]} # ServerNetworkUpdate | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Updates the server's private network's IP addresses
        api_response = api_instance.servers_server_id_private_networks_patch(server_id, private_network_id, server_network_update, force=force)
        print("The response of ServersApi->servers_server_id_private_networks_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_private_networks_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **private_network_id** | **str**| The private network identifier. | 
 **server_network_update** | [**ServerNetworkUpdate**](ServerNetworkUpdate.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**ServerPrivateNetwork**](ServerPrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP addresses assigned to server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_private_networks_post**
> ServerPrivateNetwork servers_server_id_private_networks_post(server_id, server_private_network, force=force)

Adds the server to a private network.

Adds the server to a private network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-bmc-server-after-adding-to-network#ftoc-heading-3' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server_private_network import ServerPrivateNetwork
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_private_network = {"id":"60473a6115e34466c9f8f083","ips":["10.0.0.1","10.0.0.2"],"dhcp":false} # ServerPrivateNetwork | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Adds the server to a private network.
        api_response = api_instance.servers_server_id_private_networks_post(server_id, server_private_network, force=force)
        print("The response of ServersApi->servers_server_id_private_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_private_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_private_network** | [**ServerPrivateNetwork**](ServerPrivateNetwork.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**ServerPrivateNetwork**](ServerPrivateNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The server is being added to the specified private network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_public_networks_delete**
> str servers_server_id_public_networks_delete(server_id, public_network_id)

Removes the server from the Public Network

Removes the server from the Public Network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. <b>This is an advanced network action that can make your server completely unavailable over any network. Make sure this server is reachable over remote console for guaranteed access in case of misconfiguration.</b>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.

    try:
        # Removes the server from the Public Network
        api_response = api_instance.servers_server_id_public_networks_delete(server_id, public_network_id)
        print("The response of ServersApi->servers_server_id_public_networks_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_public_networks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **public_network_id** | **str**| The Public Network identifier. | 

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
**202** | The server is being removed from the specified Public Network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_public_networks_patch**
> ServerPublicNetwork servers_server_id_public_networks_patch(server_id, public_network_id, server_network_update, force=force)

Updates the server's public network's IP addresses.

IP address changes intended to keep the BMC data up to date with server's operating system. We do not have access to the server's operating system and therefore manual configuration is required to apply the changes on the host. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/bmc-server-management-via-api#ftoc-heading-6' target='_blank'>here</a>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server_network_update import ServerNetworkUpdate
from pnap_bmc_api.models.server_public_network import ServerPublicNetwork
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    public_network_id = '603f3b2cfcaf050643b89a4b' # str | The Public Network identifier.
    server_network_update = {"ips":["182.16.0.146","182.16.0.147"]} # ServerNetworkUpdate | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Updates the server's public network's IP addresses.
        api_response = api_instance.servers_server_id_public_networks_patch(server_id, public_network_id, server_network_update, force=force)
        print("The response of ServersApi->servers_server_id_public_networks_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_public_networks_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **public_network_id** | **str**| The Public Network identifier. | 
 **server_network_update** | [**ServerNetworkUpdate**](ServerNetworkUpdate.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**ServerPublicNetwork**](ServerPublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated IP addresses assigned to server. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_public_networks_post**
> ServerPublicNetwork servers_server_id_public_networks_post(server_id, server_public_network, force=force)

Adds the server to a Public Network.

Adds the server to a Public Network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-bmc-server-after-adding-to-network#ftoc-heading-3' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server_public_network import ServerPublicNetwork
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    server_public_network = {"id":"60473c2509268bc77fd06d29","ips":["182.16.0.146","182.16.0.147"]} # ServerPublicNetwork | 
    force = False # bool | Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. (optional) (default to False)

    try:
        # Adds the server to a Public Network.
        api_response = api_instance.servers_server_id_public_networks_post(server_id, server_public_network, force=force)
        print("The response of ServersApi->servers_server_id_public_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_public_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **server_public_network** | [**ServerPublicNetwork**](ServerPublicNetwork.md)|  | 
 **force** | **bool**| Query parameter controlling advanced features availability. Currently applicable for networking. It is advised to use with caution since it might lead to unhealthy setups. | [optional] [default to False]

### Return type

[**ServerPublicNetwork**](ServerPublicNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The server is being added to the specified Public Network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_tags_put**
> Server servers_server_id_tags_put(server_id, tag_assignment_request)

Overwrite tags assigned for Server.

Overwrites tags assigned for Server and unassigns any tags not part of the request.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.server import Server
from pnap_bmc_api.models.tag_assignment_request import TagAssignmentRequest
from pnap_bmc_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/bmc/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_bmc_api.ServersApi(api_client)
    server_id = '60473a6115e34466c9f8f083' # str | The server's ID.
    tag_assignment_request = [pnap_bmc_api.TagAssignmentRequest()] # List[TagAssignmentRequest] | 

    try:
        # Overwrite tags assigned for Server.
        api_response = api_instance.servers_server_id_tags_put(server_id, tag_assignment_request)
        print("The response of ServersApi->servers_server_id_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->servers_server_id_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. | 
 **tag_assignment_request** | [**List[TagAssignmentRequest]**](TagAssignmentRequest.md)|  | 

### Return type

[**Server**](Server.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server tags set. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

