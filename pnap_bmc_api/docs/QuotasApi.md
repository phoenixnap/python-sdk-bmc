# pnap_bmc_api.QuotasApi

All URIs are relative to *https://api.phoenixnap.com/bmc/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quotas_get**](QuotasApi.md#quotas_get) | **GET** /quotas | List quotas
[**quotas_quota_id_actions_request_edit_post**](QuotasApi.md#quotas_quota_id_actions_request_edit_post) | **POST** /quotas/{quotaId}/actions/request-edit | Request quota limit change.
[**quotas_quota_id_get**](QuotasApi.md#quotas_quota_id_get) | **GET** /quotas/{quotaId} | Get a quota.


# **quotas_get**
> [Quota] quotas_get()

List quotas

Get account quota details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import quotas_api
from pnap_bmc_api.model.quota import Quota
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
    api_instance = quotas_api.QuotasApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List quotas
        api_response = api_instance.quotas_get()
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling QuotasApi->quotas_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Quota]**](Quota.md)

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
> quotas_quota_id_actions_request_edit_post(quota_id)

Request quota limit change.

Sends a request to edit the limit of a quota.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_bmc_api
from pnap_bmc_api.api import quotas_api
from pnap_bmc_api.model.quota_edit_limit_request import QuotaEditLimitRequest
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
    api_instance = quotas_api.QuotasApi(api_client)
    quota_id = "bmc.servers.max_count" # str | The ID of the Quota.
    quota_edit_limit_request = QuotaEditLimitRequest(
        limit=10,
        reason="I need more servers for my cluster.",
    ) # QuotaEditLimitRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request quota limit change.
        api_instance.quotas_quota_id_actions_request_edit_post(quota_id)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling QuotasApi->quotas_quota_id_actions_request_edit_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request quota limit change.
        api_instance.quotas_quota_id_actions_request_edit_post(quota_id, quota_edit_limit_request=quota_edit_limit_request)
    except pnap_bmc_api.ApiException as e:
        print("Exception when calling QuotasApi->quotas_quota_id_actions_request_edit_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quota_id** | **str**| The ID of the Quota. |
 **quota_edit_limit_request** | [**QuotaEditLimitRequest**](QuotaEditLimitRequest.md)|  | [optional]

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
import pnap_bmc_api
from pnap_bmc_api.api import quotas_api
from pnap_bmc_api.model.quota import Quota
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
    api_instance = quotas_api.QuotasApi(api_client)
    quota_id = "bmc.servers.max_count" # str | The ID of the Quota.

    # example passing only required values which don't have defaults set
    try:
        # Get a quota.
        api_response = api_instance.quotas_quota_id_get(quota_id)
        pprint(api_response)
    except pnap_bmc_api.ApiException as e:
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

