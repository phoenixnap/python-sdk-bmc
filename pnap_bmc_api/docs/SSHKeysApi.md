# pnap_bmc_api.SSHKeysApi

All URIs are relative to *https://api.phoenixnap.com/bmc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ssh_keys_get**](SSHKeysApi.md#ssh_keys_get) | **GET** /ssh-keys | List SSH Keys.
[**ssh_keys_post**](SSHKeysApi.md#ssh_keys_post) | **POST** /ssh-keys | Create SSH Key.
[**ssh_keys_ssh_key_id_delete**](SSHKeysApi.md#ssh_keys_ssh_key_id_delete) | **DELETE** /ssh-keys/{sshKeyId} | Delete SSH Key.
[**ssh_keys_ssh_key_id_get**](SSHKeysApi.md#ssh_keys_ssh_key_id_get) | **GET** /ssh-keys/{sshKeyId} | Get SSH Key.
[**ssh_keys_ssh_key_id_put**](SSHKeysApi.md#ssh_keys_ssh_key_id_put) | **PUT** /ssh-keys/{sshKeyId} | Edit SSH Key.


# **ssh_keys_get**
> List[SshKey] ssh_keys_get()

List SSH Keys.

List all SSH Keys.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.ssh_key import SshKey
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
    api_instance = pnap_bmc_api.SSHKeysApi(api_client)

    try:
        # List SSH Keys.
        api_response = api_instance.ssh_keys_get()
        print("The response of SSHKeysApi->ssh_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->ssh_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[SshKey]**](SshKey.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of all the SSH Keys owned by account. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_keys_post**
> SshKey ssh_keys_post(ssh_key_create)

Create SSH Key.

Create an SSH Key. SSH Keys created can be used for server creation and reset functionality.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.ssh_key import SshKey
from pnap_bmc_api.models.ssh_key_create import SshKeyCreate
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
    api_instance = pnap_bmc_api.SSHKeysApi(api_client)
    ssh_key_create = {"name":"my-sshkey-01","default":false,"key":"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDF9LdAFElNCi7JoWh6KUcchrJ2Gac1aqGRPpdZNowObpRtmiRCecAMb7bUgNAaNfcmwiQi7tos9TlnFgprIcfMWb8MSs3ABYHmBgqEEt3RWYf0fAc9CsIpJdMCUG28TPGTlRXCEUVNKgLMdcseAlJoGp1CgbHWIN65fB3he3kAZcfpPn5mapV0tsl2p+ZyuAGRYdn5dJv2RZDHUZBkOeUobwsij+weHCKAFmKQKtCP7ybgVHaQjAPrj8MGnk1jBbjDt5ws+Be+9JNjQJee9zCKbAOsIo3i+GcUIkrw5jxPU/RTGlWBcemPaKHdciSzGcjWboapzIy49qypQhZe1U75 user@my_ip"} # SshKeyCreate | 

    try:
        # Create SSH Key.
        api_response = api_instance.ssh_keys_post(ssh_key_create)
        print("The response of SSHKeysApi->ssh_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->ssh_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_create** | [**SshKeyCreate**](SshKeyCreate.md)|  | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SSH Key successfully created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_keys_ssh_key_id_delete**
> DeleteSshKeyResult ssh_keys_ssh_key_id_delete(ssh_key_id)

Delete SSH Key.

Delete an SSH Key.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.delete_ssh_key_result import DeleteSshKeyResult
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
    api_instance = pnap_bmc_api.SSHKeysApi(api_client)
    ssh_key_id = '5fa54d1e91867c03a0a7b4a4' # str | The SSH Key's ID.

    try:
        # Delete SSH Key.
        api_response = api_instance.ssh_keys_ssh_key_id_delete(ssh_key_id)
        print("The response of SSHKeysApi->ssh_keys_ssh_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->ssh_keys_ssh_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **str**| The SSH Key&#39;s ID. | 

### Return type

[**DeleteSshKeyResult**](DeleteSshKeyResult.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | SSH Key deleted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_keys_ssh_key_id_get**
> SshKey ssh_keys_ssh_key_id_get(ssh_key_id)

Get SSH Key.

Get SSH Key details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.ssh_key import SshKey
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
    api_instance = pnap_bmc_api.SSHKeysApi(api_client)
    ssh_key_id = '5fa54d1e91867c03a0a7b4a4' # str | The SSH Key's ID.

    try:
        # Get SSH Key.
        api_response = api_instance.ssh_keys_ssh_key_id_get(ssh_key_id)
        print("The response of SSHKeysApi->ssh_keys_ssh_key_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->ssh_keys_ssh_key_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **str**| The SSH Key&#39;s ID. | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific SSH Key details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ssh_keys_ssh_key_id_put**
> SshKey ssh_keys_ssh_key_id_put(ssh_key_id, ssh_key_update)

Edit SSH Key.

Edit SSH Key details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.ssh_key import SshKey
from pnap_bmc_api.models.ssh_key_update import SshKeyUpdate
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
    api_instance = pnap_bmc_api.SSHKeysApi(api_client)
    ssh_key_id = '5fa54d1e91867c03a0a7b4a4' # str | The SSH Key's ID.
    ssh_key_update = {"name":"my-sshkey-01","default":false} # SshKeyUpdate | 

    try:
        # Edit SSH Key.
        api_response = api_instance.ssh_keys_ssh_key_id_put(ssh_key_id, ssh_key_update)
        print("The response of SSHKeysApi->ssh_keys_ssh_key_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHKeysApi->ssh_keys_ssh_key_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | **str**| The SSH Key&#39;s ID. | 
 **ssh_key_update** | [**SshKeyUpdate**](SshKeyUpdate.md)|  | 

### Return type

[**SshKey**](SshKey.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific SSH Key details. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

