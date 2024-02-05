# pnap_bmc_api.QuotasApi

All URIs are relative to *https://api.phoenixnap.com/bmc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotas_get**](QuotasApi.md#quotas_get) | **GET** /quotas | List quotas
[**quotas_quota_id_actions_request_edit_post**](QuotasApi.md#quotas_quota_id_actions_request_edit_post) | **POST** /quotas/{quotaId}/actions/request-edit | Request quota limit change.
[**quotas_quota_id_get**](QuotasApi.md#quotas_quota_id_get) | **GET** /quotas/{quotaId} | Get a quota.


# **quotas_get**
> List[Quota] quotas_get()

List quotas

Get account quota details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.quota import Quota
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
    api_instance = pnap_bmc_api.QuotasApi(api_client)

    try:
        # List quotas
        api_response = api_instance.quotas_get()
        print("The response of QuotasApi->quotas_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->quotas_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Quota]**](Quota.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific account quota details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_quota_id_actions_request_edit_post**
> quotas_quota_id_actions_request_edit_post(quota_id, quota_edit_limit_request)

Request quota limit change.

Sends a request to edit the limit of a quota.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.quota_edit_limit_request import QuotaEditLimitRequest
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
    api_instance = pnap_bmc_api.QuotasApi(api_client)
    quota_id = 'bmc.servers.max_count' # str | The ID of the Quota.
    quota_edit_limit_request = pnap_bmc_api.QuotaEditLimitRequest() # QuotaEditLimitRequest | 

    try:
        # Request quota limit change.
        api_instance.quotas_quota_id_actions_request_edit_post(quota_id, quota_edit_limit_request)
    except Exception as e:
        print("Exception when calling QuotasApi->quotas_quota_id_actions_request_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_id** | **str**| The ID of the Quota. | 
 **quota_edit_limit_request** | [**QuotaEditLimitRequest**](QuotaEditLimitRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted request for editing the limit. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quotas_quota_id_get**
> Quota quotas_quota_id_get(quota_id)

Get a quota.

Get account quota details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_bmc_api
from pnap_bmc_api.models.quota import Quota
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
    api_instance = pnap_bmc_api.QuotasApi(api_client)
    quota_id = 'bmc.servers.max_count' # str | The ID of the Quota.

    try:
        # Get a quota.
        api_response = api_instance.quotas_quota_id_get(quota_id)
        print("The response of QuotasApi->quotas_quota_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotasApi->quotas_quota_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_id** | **str**| The ID of the Quota. | 

### Return type

[**Quota**](Quota.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific account quota details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

