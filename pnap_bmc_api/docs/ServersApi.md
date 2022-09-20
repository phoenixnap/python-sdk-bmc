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
[**servers_server_id_actions_reboot_post**](ServersApi.md#servers_server_id_actions_reboot_post) | **POST** /servers/{serverId}/actions/reboot | Reboot server.
[**servers_server_id_actions_reserve_post**](ServersApi.md#servers_server_id_actions_reserve_post) | **POST** /servers/{serverId}/actions/reserve | Reserve server.
[**servers_server_id_actions_reset_post**](ServersApi.md#servers_server_id_actions_reset_post) | **POST** /servers/{serverId}/actions/reset | Reset server.
[**servers_server_id_actions_shutdown_post**](ServersApi.md#servers_server_id_actions_shutdown_post) | **POST** /servers/{serverId}/actions/shutdown | Shutdown server.
[**servers_server_id_delete**](ServersApi.md#servers_server_id_delete) | **DELETE** /servers/{serverId} | Delete server.
[**servers_server_id_get**](ServersApi.md#servers_server_id_get) | **GET** /servers/{serverId} | Get server.
[**servers_server_id_ip_blocks_ip_block_id_delete**](ServersApi.md#servers_server_id_ip_blocks_ip_block_id_delete) | **DELETE** /servers/{serverId}/network-configuration/ip-block-configurations/ip-blocks/{ipBlockId} | Unassign IP Block from Server.
[**servers_server_id_ip_blocks_post**](ServersApi.md#servers_server_id_ip_blocks_post) | **POST** /servers/{serverId}/network-configuration/ip-block-configurations/ip-blocks | Assign IP Block to Server.
[**servers_server_id_patch**](ServersApi.md#servers_server_id_patch) | **PATCH** /servers/{serverId} | Patch a Server.
[**servers_server_id_private_networks_post**](ServersApi.md#servers_server_id_private_networks_post) | **POST** /servers/{serverId}/network-configuration/private-network-configuration/private-networks | Adds the server to a private network.
[**servers_server_id_public_networks_delete**](ServersApi.md#servers_server_id_public_networks_delete) | **DELETE** /servers/{serverId}/network-configuration/public-network-configuration/public-networks/{publicNetworkId} | Removes the server from the Public Network
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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    private_network_id = "603f3b2cfcaf050643b89a4b" # str | The private network identifier.

    # example passing only required values which don't have defaults set
    try:
        # Removes the server from private network.
        api_response = api_instance.delete_private_network(server_id, private_network_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_get**
> [Server] servers_get()

List servers.

List all servers owned by account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    tag = [
        "env.dev",
    ] # [str] | A list of query parameters related to tags in the form of tagName.tagValue (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List servers.
        api_response = api_instance.servers_get(tag=tag)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **[str]**| A list of query parameters related to tags in the form of tagName.tagValue | [optional]

### Return type

[**[Server]**](Server.md)

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
> Server servers_post()

Create new server.

Create (request) new server for account. Server DNS will be configured to access Google's public DNS at 8.8.8.8 .

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.error import Error
from pnap_bmc_api.model.server_create import ServerCreate
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_create = ServerCreate(
        hostname="my-server-1",
        description="Server #1 used for computing.",
        os="ubuntu/bionic",
        type="s1.c1.small",
        location="PHX",
        install_default_ssh_keys=False,
        ssh_keys=["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDF9LdAFElNCi7JoWh6KUcchrJ2Gac1aqGRPpdZNowObpRtmiRCecAMb7bUgNAaNfcmwiQi7tos9TlnFgprIcfMWb8MSs3ABYHmBgqEEt3RWYf0fAc9CsIpJdMCUG28TPGTlRXCEUVNKgLMdcseAlJoGp1CgbHWIN65fB3he3kAZcfpPn5mapV0tsl2p+ZyuAGRYdn5dJv2RZDHUZBkOeUobwsij+weHCKAFmKQKtCP7ybgVHaQjAPrj8MGnk1jBbjDt5ws+Be+9JNjQJee9zCKbAOsIo3i+GcUIkrw5jxPU/RTGlWBcemPaKHdciSzGcjWboapzIy49qypQhZe1U75 user@my_ip"],
        ssh_key_ids=["5fa942e71c16abcfbead275f","5fa94303cc6dc49346404fca","5fa943127bda760ad80c237e"],
        reservation_id="5f622c8032b458306b40d824",
        pricing_model="ONE_MONTH_RESERVATION",
        network_type="PUBLIC_AND_PRIVATE",
        os_configuration=OsConfiguration(
            windows=OsConfigurationWindows(
                rdp_allowed_ips=["172.217.22.14","10.111.14.40/29","10.111.14.66 - 10.111.14.71"],
            ),
            management_access_allowed_ips=["172.217.22.14","10.111.14.40/29","10.111.14.66 - 10.111.14.71"],
            install_os_to_ram=False,
        ),
        tags=[
            TagAssignmentRequest(
                name="Environment",
                value="PROD",
            ),
        ],
        network_configuration=NetworkConfiguration(
            gateway_address="182.16.0.145",
            private_network_configuration=PrivateNetworkConfiguration(
                gateway_address="10.0.0.10",
                configuration_type="USER_DEFINED",
                private_networks=[
                    ServerPrivateNetwork(
                        id="603f3b2cfcaf050643b89a4b",
                        ips=["10.1.1.1","10.1.1.2"],
                        dhcp=False,
                    ),
                ],
            ),
            ip_blocks_configuration=IpBlocksConfiguration(
                configuration_type="PURCHASE_NEW",
                ip_blocks=[
                    ServerIpBlock(
                        id="60473a6115e34466c9f8f083",
                    ),
                ],
            ),
            public_network_configuration=PublicNetworkConfiguration(
                public_networks=[
                    ServerPublicNetwork(
                        id="60473c2509268bc77fd06d29",
                        ips=["182.16.0.146","182.16.0.147"],
                    ),
                ],
            ),
        ),
    ) # ServerCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create new server.
        api_response = api_instance.servers_post(server_create=server_create)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_create** | [**ServerCreate**](ServerCreate.md)|  | [optional]

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
**406** | No server available of type server.type. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **servers_server_id_actions_deprovision_post**
> str servers_server_id_actions_deprovision_post(server_id)

Deprovision a server.

Deprovision the server. Supports advanced deprovision configuration.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.relinquish_ip_block import RelinquishIpBlock
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    relinquish_ip_block = RelinquishIpBlock(
        delete_ip_blocks=True,
    ) # RelinquishIpBlock |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deprovision a server.
        api_response = api_instance.servers_server_id_actions_deprovision_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_deprovision_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deprovision a server.
        api_response = api_instance.servers_server_id_actions_deprovision_post(server_id, relinquish_ip_block=relinquish_ip_block)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_deprovision_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **relinquish_ip_block** | [**RelinquishIpBlock**](RelinquishIpBlock.md)|  | [optional]

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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.action_result import ActionResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Power off server.
        api_response = api_instance.servers_server_id_actions_power_off_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.action_result import ActionResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Power on server.
        api_response = api_instance.servers_server_id_actions_power_on_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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

# **servers_server_id_actions_reboot_post**
> ActionResult servers_server_id_actions_reboot_post(server_id)

Reboot server.

Reboot specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.action_result import ActionResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Reboot server.
        api_response = api_instance.servers_server_id_actions_reboot_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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
> Server servers_server_id_actions_reserve_post(server_id)

Reserve server.

Reserve specific server.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.server_reserve import ServerReserve
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_reserve = ServerReserve(
        pricing_model="ONE_MONTH_RESERVATION",
    ) # ServerReserve |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reserve server.
        api_response = api_instance.servers_server_id_actions_reserve_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reserve_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reserve server.
        api_response = api_instance.servers_server_id_actions_reserve_post(server_id, server_reserve=server_reserve)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reserve_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_reserve** | [**ServerReserve**](ServerReserve.md)|  | [optional]

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
> ResetResult servers_server_id_actions_reset_post(server_id)

Reset server.

Deprecated: Reset specific server. Reset only supports network configurations of type 'private network' or 'IP blocks'. As an alternative, the suggested action is to deprovision the server and provision a new one with the same configuration.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server_reset import ServerReset
from pnap_bmc_api.model.reset_result import ResetResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_reset = ServerReset(
        install_default_ssh_keys=False,
        ssh_keys=["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDF9LdAFElNCi7JoWh6KUcchrJ2Gac1aqGRPpdZNowObpRtmiRCecAMb7bUgNAaNfcmwiQi7tos9TlnFgprIcfMWb8MSs3ABYHmBgqEEt3RWYf0fAc9CsIpJdMCUG28TPGTlRXCEUVNKgLMdcseAlJoGp1CgbHWIN65fB3he3kAZcfpPn5mapV0tsl2p+ZyuAGRYdn5dJv2RZDHUZBkOeUobwsij+weHCKAFmKQKtCP7ybgVHaQjAPrj8MGnk1jBbjDt5ws+Be+9JNjQJee9zCKbAOsIo3i+GcUIkrw5jxPU/RTGlWBcemPaKHdciSzGcjWboapzIy49qypQhZe1U75 user@my_ip"],
        ssh_key_ids=["5fa942e71c16abcfbead275f","5fa94303cc6dc49346404fca","5fa943127bda760ad80c237e"],
        os_configuration=OsConfigurationMap(
            windows=OsConfigurationWindows(
                rdp_allowed_ips=["172.217.22.14","10.111.14.40/29","10.111.14.66 - 10.111.14.71"],
            ),
            esxi=OsConfigurationMapEsxi(
                management_access_allowed_ips=["172.217.22.14","10.111.14.40/29","10.111.14.66 - 10.111.14.71"],
            ),
            proxmox=OsConfigurationMapProxmox(
                management_access_allowed_ips=["172.217.22.14","10.111.14.40/29","10.111.14.66 - 10.111.14.71"],
            ),
        ),
    ) # ServerReset |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset server.
        api_response = api_instance.servers_server_id_actions_reset_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reset_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset server.
        api_response = api_instance.servers_server_id_actions_reset_post(server_id, server_reset=server_reset)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_actions_reset_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_reset** | [**ServerReset**](ServerReset.md)|  | [optional]

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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.action_result import ActionResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Shutdown server.
        api_response = api_instance.servers_server_id_actions_shutdown_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.delete_result import DeleteResult
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete server.
        api_response = api_instance.servers_server_id_delete(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.

    # example passing only required values which don't have defaults set
    try:
        # Get server.
        api_response = api_instance.servers_server_id_get(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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
> str servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id)

Unassign IP Block from Server.

Removes the IP block from the server. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. <b>This is an advanced network action that can make your server completely unavailable over any network. Make sure this server is reachable over remote console for guaranteed access in case of misconfiguration.</b>

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.relinquish_ip_block import RelinquishIpBlock
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    ip_block_id = "6047127fed34ecc3ba8402d2" # str | The IP Block identifier.
    relinquish_ip_block = RelinquishIpBlock(
        delete_ip_blocks=True,
    ) # RelinquishIpBlock |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unassign IP Block from Server.
        api_response = api_instance.servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_ip_block_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unassign IP Block from Server.
        api_response = api_instance.servers_server_id_ip_blocks_ip_block_id_delete(server_id, ip_block_id, relinquish_ip_block=relinquish_ip_block)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_ip_block_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **ip_block_id** | **str**| The IP Block identifier. |
 **relinquish_ip_block** | [**RelinquishIpBlock**](RelinquishIpBlock.md)|  | [optional]

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
> ServerIpBlock servers_server_id_ip_blocks_post(server_id)

Assign IP Block to Server.

Adds an IP block to this server. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-server-with-public-ip-block#ftoc-heading-2' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server_ip_block import ServerIpBlock
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_ip_block = ServerIpBlock(
        id="60473a6115e34466c9f8f083",
    ) # ServerIpBlock |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assign IP Block to Server.
        api_response = api_instance.servers_server_id_ip_blocks_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assign IP Block to Server.
        api_response = api_instance.servers_server_id_ip_blocks_post(server_id, server_ip_block=server_ip_block)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_ip_blocks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_ip_block** | [**ServerIpBlock**](ServerIpBlock.md)|  | [optional]

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
> Server servers_server_id_patch(server_id)

Patch a Server.

Any changes to the hostname or description using the BMC API will reflect solely in the BMC API and portal. The changes are intended to keep the BMC data up to date with your server. We do not have access to your server's settings. Local changes to the server's hostname will not be reflected in the API or portal.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.error import Error
from pnap_bmc_api.model.server_patch import ServerPatch
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_patch = ServerPatch(
        description="Server #1 used for computing.",
        hostname="my-server",
    ) # ServerPatch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch a Server.
        api_response = api_instance.servers_server_id_patch(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch a Server.
        api_response = api_instance.servers_server_id_patch(server_id, server_patch=server_patch)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_patch** | [**ServerPatch**](ServerPatch.md)|  | [optional]

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

# **servers_server_id_private_networks_post**
> ServerPrivateNetwork servers_server_id_private_networks_post(server_id)

Adds the server to a private network.

Adds the server to a private network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. If the network contains a membership of type 'storage', the first twelve IPs are already reserved by BMC and not usable. These will return a Bad Request (400) if selected. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-bmc-server-after-adding-to-network#ftoc-heading-3' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server_private_network import ServerPrivateNetwork
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_private_network = ServerPrivateNetwork(
        id="603f3b2cfcaf050643b89a4b",
        ips=["10.1.1.1","10.1.1.2"],
        dhcp=False,
    ) # ServerPrivateNetwork |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds the server to a private network.
        api_response = api_instance.servers_server_id_private_networks_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_private_networks_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds the server to a private network.
        api_response = api_instance.servers_server_id_private_networks_post(server_id, server_private_network=server_private_network)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_private_networks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_private_network** | [**ServerPrivateNetwork**](ServerPrivateNetwork.md)|  | [optional]

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
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    public_network_id = "603f3b2cfcaf050643b89a4b" # str | The Public Network identifier.

    # example passing only required values which don't have defaults set
    try:
        # Removes the server from the Public Network
        api_response = api_instance.servers_server_id_public_networks_delete(server_id, public_network_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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

# **servers_server_id_public_networks_post**
> ServerPublicNetwork servers_server_id_public_networks_post(server_id)

Adds the server to a Public Network.

Adds the server to a Public Network. <b>No actual configuration is performed on the operating system.</b> BMC configures exclusively the networking devices in the datacenter infrastructure. Manual network configuration changes in the operating system of this server are required. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/configure-bmc-server-after-adding-to-network#ftoc-heading-3' target='_blank'>here</a>.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.server_public_network import ServerPublicNetwork
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    server_public_network = ServerPublicNetwork(
        id="60473c2509268bc77fd06d29",
        ips=["182.16.0.146","182.16.0.147"],
    ) # ServerPublicNetwork |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds the server to a Public Network.
        api_response = api_instance.servers_server_id_public_networks_post(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_public_networks_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds the server to a Public Network.
        api_response = api_instance.servers_server_id_public_networks_post(server_id, server_public_network=server_public_network)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_public_networks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **server_public_network** | [**ServerPublicNetwork**](ServerPublicNetwork.md)|  | [optional]

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
> Server servers_server_id_tags_put(server_id)

Overwrite tags assigned for Server.

Overwrites tags assigned for Server and unassigns any tags not part of the request.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import servers_api
from pnap_bmc_api.model.tag_assignment_request import TagAssignmentRequest
from pnap_bmc_api.model.server import Server
from pnap_bmc_api.model.error import Error
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

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_bmc_api.Configuration(
    host = "https://api.phoenixnap.com/bmc/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_bmc_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = servers_api.ServersApi(api_client)
    server_id = "e6afba51-7de8-4080-83ab-0f915570659c" # str | The server's ID.
    tag_assignment_request = [
        TagAssignmentRequest(
            name="Environment",
            value="PROD",
        ),
    ] # [TagAssignmentRequest] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Overwrite tags assigned for Server.
        api_response = api_instance.servers_server_id_tags_put(server_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_tags_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Overwrite tags assigned for Server.
        api_response = api_instance.servers_server_id_tags_put(server_id, tag_assignment_request=tag_assignment_request)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling ServersApi->servers_server_id_tags_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | **str**| The server&#39;s ID. |
 **tag_assignment_request** | [**[TagAssignmentRequest]**](TagAssignmentRequest.md)|  | [optional]

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

