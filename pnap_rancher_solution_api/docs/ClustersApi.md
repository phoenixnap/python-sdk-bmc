# pnap_rancher_solution_api.ClustersApi

All URIs are relative to *https://api.phoenixnap.com/solutions/rancher/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clusters_get**](ClustersApi.md#clusters_get) | **GET** /clusters | Cluster list.
[**clusters_id_delete**](ClustersApi.md#clusters_id_delete) | **DELETE** /clusters/{id} | Delete a cluster.
[**clusters_id_get**](ClustersApi.md#clusters_id_get) | **GET** /clusters/{id} | Retrieve a Cluster
[**clusters_post**](ClustersApi.md#clusters_post) | **POST** /clusters | Create a Rancher Server Deployment.


# **clusters_get**
> [Cluster] clusters_get()

Cluster list.

Cluster list.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_rancher_solution_api
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.model.cluster import Cluster
from pnap_rancher_solution_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/solutions/rancher/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_rancher_solution_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Cluster list.
        api_response = api_instance.clusters_get()
        pprint(api_response)
    except pnap_rancher_solution_api.ApiException as e:
        print("Exception when calling ClustersApi->clusters_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Cluster]**](Cluster.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster list. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_delete**
> DeleteResult clusters_id_delete(id)

Delete a cluster.

Delete a cluster.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_rancher_solution_api
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.model.delete_result import DeleteResult
from pnap_rancher_solution_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/solutions/rancher/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_rancher_solution_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)
    id = "123" # str | The Cluster identifier.

    # example passing only required values which don't have defaults set
    try:
        # Delete a cluster.
        api_response = api_instance.clusters_id_delete(id)
        pprint(api_response)
    except pnap_rancher_solution_api.ApiException as e:
        print("Exception when calling ClustersApi->clusters_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Cluster identifier. |

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
**200** | Cluster is being deleted. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_id_get**
> Cluster clusters_id_get(id)

Retrieve a Cluster

Retrieve a Cluster

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_rancher_solution_api
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.model.cluster import Cluster
from pnap_rancher_solution_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/solutions/rancher/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_rancher_solution_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)
    id = "123" # str | The Cluster identifier.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Cluster
        api_response = api_instance.clusters_id_get(id)
        pprint(api_response)
    except pnap_rancher_solution_api.ApiException as e:
        print("Exception when calling ClustersApi->clusters_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Cluster identifier. |

### Return type

[**Cluster**](Cluster.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cluster details |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clusters_post**
> Cluster clusters_post()

Create a Rancher Server Deployment.

Create a Rancher Server Deployment as described in <a href='https://rancher.com/docs/rancher/v2.5/en/overview/architecture/#rancher-server-architecture' target='_blank'>Rancher Docs Architecture</a>. Rancher Server allows the creation, import and management of multiple Downstream User Kubernetes Clusters. <b>This is not a Downstream User Cluster</b>. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/bmc-rancher-workload-cluster#ftoc-heading-5' target='_blank'>here</a>. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_rancher_solution_api
from pnap_rancher_solution_api.api import clusters_api
from pnap_rancher_solution_api.model.cluster import Cluster
from pnap_rancher_solution_api.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/solutions/rancher/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_rancher_solution_api.Configuration(
    host = "https://api.phoenixnap.com/solutions/rancher/v1beta"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_rancher_solution_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)
    cluster = Cluster(
        name="Rancher Management Cluster",
        description="My first Rancher Server Cluster.",
        location="PHX",
        node_pools=[
            NodePool(
                name="Rancher Server node pool.",
                node_count=1,
                server_type="s0.d1.small",
                ssh_config=None,
            ),
        ],
        configuration=None,
        workload_configuration=None,
    ) # Cluster |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Rancher Server Deployment.
        api_response = api_instance.clusters_post(cluster=cluster)
        pprint(api_response)
    except pnap_rancher_solution_api.ApiException as e:
        print("Exception when calling ClustersApi->clusters_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster** | [**Cluster**](Cluster.md)|  | [optional]

### Return type

[**Cluster**](Cluster.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Cluster is being created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

