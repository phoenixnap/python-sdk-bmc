# pnap_network_storage_api.StorageNetworksApi

All URIs are relative to *https://api.phoenixnap.com/network-storage/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_networks_get**](StorageNetworksApi.md#storage_networks_get) | **GET** /storage-networks | List all storage networks.
[**storage_networks_id_delete**](StorageNetworksApi.md#storage_networks_id_delete) | **DELETE** /storage-networks/{storageId} | Delete a storage network and its volume.
[**storage_networks_id_get**](StorageNetworksApi.md#storage_networks_id_get) | **GET** /storage-networks/{storageId} | Get storage network details.
[**storage_networks_id_patch**](StorageNetworksApi.md#storage_networks_id_patch) | **PATCH** /storage-networks/{storageId} | Update storage network details.
[**storage_networks_post**](StorageNetworksApi.md#storage_networks_post) | **POST** /storage-networks | Create a storage network and volume.
[**storage_networks_storage_network_id_volumes_get**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_get) | **GET** /storage-networks/{storageId}/volumes | Display one or more volumes belonging to a storage network.
[**storage_networks_storage_network_id_volumes_post**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_post) | **POST** /storage-networks/{storageId}/volumes | Create a volume belonging to a storage network.
[**storage_networks_storage_network_id_volumes_volume_id_delete**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_delete) | **DELETE** /storage-networks/{storageId}/volumes/{volumeId} | Delete a Storage Network&#39;s Volume
[**storage_networks_storage_network_id_volumes_volume_id_get**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_get) | **GET** /storage-networks/{storageId}/volumes/{volumeId} | Get a storage network&#39;s volume details.
[**storage_networks_storage_network_id_volumes_volume_id_patch**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_patch) | **PATCH** /storage-networks/{storageId}/volumes/{volumeId} | Update a storage network&#39;s volume details.
[**storage_networks_storage_network_id_volumes_volume_id_tags_put**](StorageNetworksApi.md#storage_networks_storage_network_id_volumes_volume_id_tags_put) | **PUT** /storage-networks/{storageId}/volumes/{volumeId}/tags | Overwrites tags assigned for the volume.


# **storage_networks_get**
> List[StorageNetwork] storage_networks_get(location=location)

List all storage networks.

List all storage networks.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.storage_network import StorageNetwork
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    location = 'PHX' # str | If present will filter the result by the given location. (optional)

    try:
        # List all storage networks.
        api_response = api_instance.storage_networks_get(location=location)
        print("The response of StorageNetworksApi->storage_networks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| If present will filter the result by the given location. | [optional] 

### Return type

[**List[StorageNetwork]**](StorageNetwork.md)

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
> storage_networks_id_delete(storage_id)

Delete a storage network and its volume.

Delete a storage network and its volume. A storage network can only be removed if it's not in 'BUSY' state. Billing stops on storage network deletion.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.

    try:
        # Delete a storage network and its volume.
        api_instance.storage_networks_id_delete(storage_id)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 

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
**204** | Initiate the deletion process for the specified Storage Network. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The request failed because service is currently unavailable. Please try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_id_get**
> StorageNetwork storage_networks_id_get(storage_id)

Get storage network details.

Get storage network details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.storage_network import StorageNetwork
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.

    try:
        # Get storage network details.
        api_response = api_instance.storage_networks_id_get(storage_id)
        print("The response of StorageNetworksApi->storage_networks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 

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
> StorageNetwork storage_networks_id_patch(storage_id, storage_network_update)

Update storage network details.

Update storage network details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.storage_network import StorageNetwork
from pnap_network_storage_api.models.storage_network_update import StorageNetworkUpdate
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    storage_network_update = {"name":"My storage network","description":"Storage network description"} # StorageNetworkUpdate | Storage network to be updated.

    try:
        # Update storage network details.
        api_response = api_instance.storage_networks_id_patch(storage_id, storage_network_update)
        print("The response of StorageNetworksApi->storage_networks_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
 **storage_network_update** | [**StorageNetworkUpdate**](StorageNetworkUpdate.md)| Storage network to be updated. | 

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
> StorageNetwork storage_networks_post(storage_network_create)

Create a storage network and volume.

Create a storage network and volume.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.storage_network import StorageNetwork
from pnap_network_storage_api.models.storage_network_create import StorageNetworkCreate
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_network_create = pnap_network_storage_api.StorageNetworkCreate() # StorageNetworkCreate | 

    try:
        # Create a storage network and volume.
        api_response = api_instance.storage_networks_post(storage_network_create)
        print("The response of StorageNetworksApi->storage_networks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_network_create** | [**StorageNetworkCreate**](StorageNetworkCreate.md)|  | 

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
> List[Volume] storage_networks_storage_network_id_volumes_get(storage_id, tag=tag)

Display one or more volumes belonging to a storage network.

Display one or more volumes belonging to a storage network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.volume import Volume
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    tag = ['env.dev'] # List[str] | A list of query parameters related to tags in the form of tagName.tagValue (optional)

    try:
        # Display one or more volumes belonging to a storage network.
        api_response = api_instance.storage_networks_storage_network_id_volumes_get(storage_id, tag=tag)
        print("The response of StorageNetworksApi->storage_networks_storage_network_id_volumes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
 **tag** | [**List[str]**](str.md)| A list of query parameters related to tags in the form of tagName.tagValue | [optional] 

### Return type

[**List[Volume]**](Volume.md)

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

# **storage_networks_storage_network_id_volumes_post**
> Volume storage_networks_storage_network_id_volumes_post(storage_id, volume_create)

Create a volume belonging to a storage network.

Create a volume belonging to a storage network.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.volume import Volume
from pnap_network_storage_api.models.volume_create import VolumeCreate
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    volume_create = pnap_network_storage_api.VolumeCreate() # VolumeCreate | 

    try:
        # Create a volume belonging to a storage network.
        api_response = api_instance.storage_networks_storage_network_id_volumes_post(storage_id, volume_create)
        print("The response of StorageNetworksApi->storage_networks_storage_network_id_volumes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
 **volume_create** | [**VolumeCreate**](VolumeCreate.md)|  | 

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
**202** | Volume that is being created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The request failed because service is currently unavailable. Please try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_delete**
> storage_networks_storage_network_id_volumes_volume_id_delete(storage_id, volume_id)

Delete a Storage Network's Volume

Delete a Storage Network's Volume

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    volume_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of volume.

    try:
        # Delete a Storage Network's Volume
        api_instance.storage_networks_storage_network_id_volumes_volume_id_delete(storage_id, volume_id)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
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
**204** | Initiate the deletion process for the specified Volume. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_get**
> Volume storage_networks_storage_network_id_volumes_volume_id_get(storage_id, volume_id)

Get a storage network's volume details.

Get a storage network's volume details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.volume import Volume
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    volume_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of volume.

    try:
        # Get a storage network's volume details.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_get(storage_id, volume_id)
        print("The response of StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
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
> Volume storage_networks_storage_network_id_volumes_volume_id_patch(storage_id, volume_id, volume_update)

Update a storage network's volume details.

Update a storage network's volume details. Volume's capacity requested cannot be less than or equal to current volume's capacity.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.volume import Volume
from pnap_network_storage_api.models.volume_update import VolumeUpdate
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    volume_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of volume.
    volume_update = pnap_network_storage_api.VolumeUpdate() # VolumeUpdate | Storage network volume to be updated.

    try:
        # Update a storage network's volume details.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_patch(storage_id, volume_id, volume_update)
        print("The response of StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
 **volume_id** | **str**| ID of volume. | 
 **volume_update** | [**VolumeUpdate**](VolumeUpdate.md)| Storage network volume to be updated. | 

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
**200** | Updated volume details. |  -  |
**202** | Updating volume details. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |
**503** | The request failed because service is currently unavailable. Please try again later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_networks_storage_network_id_volumes_volume_id_tags_put**
> Volume storage_networks_storage_network_id_volumes_volume_id_tags_put(storage_id, volume_id, tag_assignment_request)

Overwrites tags assigned for the volume.

Overwrites tags assigned for the volume.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_network_storage_api
from pnap_network_storage_api.models.tag_assignment_request import TagAssignmentRequest
from pnap_network_storage_api.models.volume import Volume
from pnap_network_storage_api.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_network_storage_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_network_storage_api.StorageNetworksApi(api_client)
    storage_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of the storage.
    volume_id = '50dc434c-9bba-427b-bcd6-0bdba45c4dd2' # str | ID of volume.
    tag_assignment_request = [pnap_network_storage_api.TagAssignmentRequest()] # List[TagAssignmentRequest] | Tags to assign to the volume.

    try:
        # Overwrites tags assigned for the volume.
        api_response = api_instance.storage_networks_storage_network_id_volumes_volume_id_tags_put(storage_id, volume_id, tag_assignment_request)
        print("The response of StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageNetworksApi->storage_networks_storage_network_id_volumes_volume_id_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_id** | **str**| ID of the storage. | 
 **volume_id** | **str**| ID of volume. | 
 **tag_assignment_request** | [**List[TagAssignmentRequest]**](TagAssignmentRequest.md)| Tags to assign to the volume. | 

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
**200** | Volume tags set. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The resource is in an incompatible state. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

