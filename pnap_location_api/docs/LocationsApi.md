# pnap_location_api.LocationsApi

All URIs are relative to *https://api.phoenixnap.com/location-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | Get All Locations


# **get_locations**
> [Location] get_locations()

Get All Locations

Retrieve the locations info.

### Example


```python
import time
import pnap_location_api
from pnap_location_api.api import locations_api
from pnap_location_api.model.error import Error
from pnap_location_api.model.location_enum import LocationEnum
from pnap_location_api.model.location import Location
from pnap_location_api.model.product_category_enum import ProductCategoryEnum
from pprint import pprint
# Defining the host is optional and defaults to https://api.phoenixnap.com/location-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_location_api.Configuration(
    host = "https://api.phoenixnap.com/location-api/v1"
)


# Enter a context with an instance of the API client
with pnap_location_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = locations_api.LocationsApi(api_client)
    location = LocationEnum("ASH") # LocationEnum | Location of interest (optional)
    product_category = ProductCategoryEnum("SERVER") # ProductCategoryEnum | Product category of interest (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get All Locations
        api_response = api_instance.get_locations(location=location, product_category=product_category)
        pprint(api_response)
    except pnap_location_api.ApiException as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **LocationEnum**| Location of interest | [optional]
 **product_category** | **ProductCategoryEnum**| Product category of interest | [optional]

### Return type

[**[Location]**](Location.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Locations found |  -  |
**404** | The request failed since the resource could not been found. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

