# pnap_network_storage_api.StorageNetworksApi

All URIs are relative to *https://api.phoenixnap.com/network-storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_networks_get**](StorageNetworksApi.md#storage_networks_get) | **GET** /storage-networks | List all storage networks.
[**storage_networks_id_delete**](StorageNetworksApi.md#storage_networks_id_delete) | **DELETE** /storage-networks/{storageNetworkId} | Delete a storage network and its volume.
[**storage_networks_id_get**](StorageNetworksApi.md#storage_networks_id_get) | **GET** /storage-networks/{storageNetworkId} | Get storage network details.
[**storage_networks_id_patch**](StorageNetworksApi.md#storage_networks_id_patch) | **PATCH** /storage-networks/{storageNetworkId} | Update storage network details.
[**storage_networks_post**](StorageNetworksApi.md#storage_networks_post) | **POST** /storage-networks | Create a storage network and volume.
[**storage_networks_storage_network_id_volumes_get**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_get) | **GET** /storage-networks/{storageNetworkId}/volumes | Display one or more volumes belonging to a storage network.
[**storage_networks_storage_network_id_volumes_volume_id_delete**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_delete) | **DELETE** /storage-networks/{storageNetworkId}/volumes/{volumeId} | Delete a Storage Network&#39;s Volume
[**storage_networks_storage_network_id_volumes_volume_id_get**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_get) | **GET** /storage-networks/{storageNetworkId}/volumes/{volumeId} | Get a storage network&#39;s volume details.
[**storage_networks_storage_network_id_volumes_volume_id_patch**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_patch) | **PATCH** /storage-networks/{storageNetworkId}/volumes/{volumeId} | Update a storage network&#39;s volume details.


# **storage_networks_get**
> [StorageNetwork] storage_networks_get()

List all storage networks.

List all storage networks.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.storage_network import StorageNetwork
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    location = "PHX" # str | If present will filter the result by the given location. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all storage networks.
        api_response = api_instance.storage_networks_get(location=location)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| If present will filter the result by the given location. | [optional]

### Return type

[**[StorageNetwork]**](StorageNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all storage networks. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_id_delete**
> storage_networks_id_delete(storage_network_id)

Delete a storage network and its volume.

Delete a storage network and its volume. A storage network can only be removed if it's not in 'BUSY' state. Billing stops on storage network deletion.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.

    # example passing only required values which don't have defaults set
    try:
        # Delete a storage network and its volume.
        api_instance.storage_networks_id_delete(storage_network_id)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |

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
**204** | Storage Network is deleted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_id_get**
> StorageNetwork storage_networks_id_get(storage_network_id)

Get storage network details.

Get storage network details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.storage_network import StorageNetwork
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.

    # example passing only required values which don't have defaults set
    try:
        # Get storage network details.
        api_response = api_instance.storage_networks_id_get(storage_network_id)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |

### Return type

[**StorageNetwork**](StorageNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get storage network details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_id_patch**
> StorageNetwork storage_networks_id_patch(storage_network_id)

Update storage network details.

Update storage network details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.storage_network import StorageNetwork
from pnap_network_storage_api.model.storage_network_update import StorageNetworkUpdate
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.
    storage_network_update = StorageNetworkUpdate(
        name="My storage network",
        description="My storage network description",
    ) # StorageNetworkUpdate | Storage network to be updated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update storage network details.
        api_response = api_instance.storage_networks_id_patch(storage_network_id)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update storage network details.
        api_response = api_instance.storage_networks_id_patch(storage_network_id, storage_network_update=storage_network_update)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |
 **storage_network_update** | [**StorageNetworkUpdate**](StorageNetworkUpdate.md)| Storage network to be updated. | [optional]

### Return type

[**StorageNetwork**](StorageNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated storage network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_post**
> StorageNetwork storage_networks_post()

Create a storage network and volume.

Create a storage network and volume.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.storage_network_create import StorageNetworkCreate
from pnap_network_storage_api.model.storage_network import StorageNetwork
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_create = StorageNetworkCreate(
        name="My storage network",
        description="My storage network description",
        location="PHX",
        volumes=[
            VolumeCreate(
                name="My volume name",
                description="My volume description",
                path_suffix="/shared-docs",
                capacity_in_gb=2000,
            ),
        ],
    ) # StorageNetworkCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a storage network and volume.
        api_response = api_instance.storage_networks_post(storage_network_create=storage_network_create)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_create** | [**StorageNetworkCreate**](StorageNetworkCreate.md)|  | [optional]

### Return type

[**StorageNetwork**](StorageNetwork.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted request for creating a Storage network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_get**
> [Volume] storage_networks_storage_network_id_volumes_get(storage_network_id)

Display one or more volumes belonging to a storage network.

Display one or more volumes belonging to a storage network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.volume import Volume
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.

    # example passing only required values which don't have defaults set
    try:
        # Display one or more volumes belonging to a storage network.
        api_response = api_instance.storage_networks_storage_network_id_volumes_get(storage_network_id)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |

### Return type

[**[Volume]**](Volume.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a storage network&#39;s volume details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_delete**
> storage_networks_storage_network_id_volumes_volume_id_delete(storage_network_id, volume_id)

Delete a Storage Network's Volume

Delete a Storage Network's Volume

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.
    volume_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of volume.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Storage Network's Volume
        api_instance.storage_networks_storage_network_id_volumes_volume_id_delete(storage_network_id, volume_id)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |
 **volume_id** | **str**| ID of volume. |

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
**204** | Volume is deleted. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_get**
> Volume storage_networks_storage_network_id_volumes_volume_id_get(storage_network_id, volume_id)

Get a storage network's volume details.

Get a storage network's volume details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.volume import Volume
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.
    volume_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of volume.

    # example passing only required values which don't have defaults set
    try:
        # Get a storage network's volume details.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_get(storage_network_id, volume_id)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |
 **volume_id** | **str**| ID of volume. |

### Return type

[**Volume**](Volume.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a storage network&#39;s volume details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_patch**
> Volume storage_networks_storage_network_id_volumes_volume_id_patch(storage_network_id, volume_id)

Update a storage network's volume details.

Update a storage network's volume details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_network_storage_api
from pnap_network_storage_api.api import storage_networks_api
from pnap_network_storage_api.model.volume import Volume
from pnap_network_storage_api.model.volume_update import VolumeUpdate
from pnap_network_storage_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/network-storage/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_network_storage_api.Configuration(
    host = "https://api.phoenixnap.com/network-storage/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = storage_networks_api.StorageNetworksApi(api_client)
    storage_network_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of storage network.
    volume_id = "50dc434c-9bba-427b-bcd6-0bdba45c4dd2" # str | ID of volume.
    volume_update = VolumeUpdate(
        capacity_in_gb=2000,
    ) # VolumeUpdate | Storage network volume to be updated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a storage network's volume details.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_patch(storage_network_id, volume_id)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a storage network's volume details.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_patch(storage_network_id, volume_id, volume_update=volume_update)
        pprint(api_response)
    except pnap_network_storage_api.ApiException as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_id** | **str**| ID of storage network. |
 **volume_id** | **str**| ID of volume. |
 **volume_update** | [**VolumeUpdate**](VolumeUpdate.md)| Storage network volume to be updated. | [optional]

### Return type

[**Volume**](Volume.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Updating volume details. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

