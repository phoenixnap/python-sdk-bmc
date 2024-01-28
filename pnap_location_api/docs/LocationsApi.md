# pnap_location_api.LocationsApi

All URIs are relative to *https://api.phoenixnap.com/location-api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | Get All Locations


# **get_locations**
> List[Location] get_locations(location=location, product_category=product_category)

Get All Locations

Retrieve the locations info.

### Example


```python
import time
import os
import pnap_location_api
from pnap_location_api.models.location import Location
from pnap_location_api.models.location_enum import LocationEnum
from pnap_location_api.models.product_category_enum import ProductCategoryEnum
from pnap_location_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/location-api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_location_api.Configuration(
    host = "https://api.phoenixnap.com/location-api/v1"
)


# Enter a context with an instance of the API client
with pnap_location_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_location_api.LocationsApi(api_client)
    location = pnap_location_api.LocationEnum() # LocationEnum | Location of interest (optional)
    product_category = pnap_location_api.ProductCategoryEnum() # ProductCategoryEnum | Product category of interest (optional)

    try:
        # Get All Locations
        api_response = api_instance.get_locations(location=location, product_category=product_category)
        print("The response of LocationsApi->get_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**LocationEnum**](.md)| Location of interest | [optional] 
 **product_category** | [**ProductCategoryEnum**](.md)| Product category of interest | [optional] 

### Return type

[**List[Location]**](Location.md)

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

