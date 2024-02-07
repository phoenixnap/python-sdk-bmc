# pnap_billing_api.BillingConfigurationsApi

All URIs are relative to *https://api.phoenixnap.com/billing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_billing_configuration_me_get**](BillingConfigurationsApi.md#account_billing_configuration_me_get) | **GET** /account-billing-configurations/me | Retrieves billing configuration associated with the authenticated account.


# **account_billing_configuration_me_get**
> ConfigurationDetails account_billing_configuration_me_get()

Retrieves billing configuration associated with the authenticated account.

Retrieves billing configuration associated with the authenticated account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_billing_api
from pnap_billing_api.models.configuration_details import ConfigurationDetails
from pnap_billing_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/billing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_billing_api.Configuration(
    host = "https://api.phoenixnap.com/billing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_billing_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_billing_api.BillingConfigurationsApi(api_client)

    try:
        # Retrieves billing configuration associated with the authenticated account.
        api_response = api_instance.account_billing_configuration_me_get()
        print("The response of BillingConfigurationsApi->account_billing_configuration_me_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingConfigurationsApi->account_billing_configuration_me_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConfigurationDetails**](ConfigurationDetails.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Billing configuration details for the account |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

