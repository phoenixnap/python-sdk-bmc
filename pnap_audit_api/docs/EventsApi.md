# pnap_audit_api.EventsApi

All URIs are relative to *https://api.phoenixnap.com/audit/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_get**](EventsApi.md#events_get) | **GET** /events | List event logs.


# **events_get**
> [Event] events_get()

List event logs.

Retrieves the event logs for given time period. All date & times are in UTC.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import pnap_audit_api
from pnap_audit_api.api import events_api
from pnap_audit_api.model.error import Error
from pnap_audit_api.model.event import Event
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/audit/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_audit_api.Configuration(
    host = "https://api.phoenixnap.com/audit/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = pnap_audit_api.Configuration(
    host = "https://api.phoenixnap.com/audit/v1"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pnap_audit_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = events_api.EventsApi(api_client)
    _from = dateutil_parser('2021-04-27T16:24:57.123Z') # datetime | From the date and time (inclusive) to filter event log records by. (optional)
    to = dateutil_parser('2021-04-29T16:24:57.123Z') # datetime | To the date and time (inclusive) to filter event log records by. (optional)
    limit = 10 # int | Limit the number of records returned. (optional)
    order = "ASC" # str | Ordering of the event's time. SortBy can be introduced later on. (optional) if omitted the server will use the default value of "ASC"
    username = "johnd@phoenixnap.com" # str | The username that did the actions. (optional)
    verb = "POST" # str | The HTTP verb corresponding to the action. (optional)
    uri = "/ams/v1/clients/12345" # str | The request uri. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List event logs.
        api_response = api_instance.events_get(_from=_from, to=to, limit=limit, order=order, username=username, verb=verb, uri=uri)
        pprint(api_response)
    except pnap_audit_api.ApiException as e:
        print("Exception when calling EventsApi->events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| From the date and time (inclusive) to filter event log records by. | [optional]
 **to** | **datetime**| To the date and time (inclusive) to filter event log records by. | [optional]
 **limit** | **int**| Limit the number of records returned. | [optional]
 **order** | **str**| Ordering of the event&#39;s time. SortBy can be introduced later on. | [optional] if omitted the server will use the default value of "ASC"
 **username** | **str**| The username that did the actions. | [optional]
 **verb** | **str**| The HTTP verb corresponding to the action. | [optional]
 **uri** | **str**| The request uri. | [optional]

### Return type

[**[Event]**](Event.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of events recorded. |  -  |
**206** | The truncated list of events recorded. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

