# pnap_tag_api.TagsApi

All URIs are relative to *https://api.phoenixnap.com/tag-manager/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tags_get**](TagsApi.md#tags_get) | **GET** /tags | List tags.
[**tags_post**](TagsApi.md#tags_post) | **POST** /tags | Create a Tag.
[**tags_tag_id_delete**](TagsApi.md#tags_tag_id_delete) | **DELETE** /tags/{tagId} | Delete a Tag.
[**tags_tag_id_get**](TagsApi.md#tags_tag_id_get) | **GET** /tags/{tagId} | Get a Tag.
[**tags_tag_id_patch**](TagsApi.md#tags_tag_id_patch) | **PATCH** /tags/{tagId} | Modify a Tag.


# **tags_get**
> List[Tag] tags_get(name=name)

List tags.

Retrieve all tags belonging to the BMC Account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_tag_api
from pnap_tag_api.models.tag import Tag
from pnap_tag_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/tag-manager/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_tag_api.Configuration(
    host = "https://api.phoenixnap.com/tag-manager/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_tag_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_tag_api.TagsApi(api_client)
    name = 'env' # str | Query a tag by its name. (optional)

    try:
        # List tags.
        api_response = api_instance.tags_get(name=name)
        print("The response of TagsApi->tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Query a tag by its name. | [optional] 

### Return type

[**List[Tag]**](Tag.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tags list. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_post**
> Tag tags_post(tag_create)

Create a Tag.

Create a tag with the provided information.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_tag_api
from pnap_tag_api.models.tag import Tag
from pnap_tag_api.models.tag_create import TagCreate
from pnap_tag_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/tag-manager/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_tag_api.Configuration(
    host = "https://api.phoenixnap.com/tag-manager/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_tag_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_tag_api.TagsApi(api_client)
    tag_create = pnap_tag_api.TagCreate() # TagCreate | The body containing the tag details.

    try:
        # Create a Tag.
        api_response = api_instance.tags_post(tag_create)
        print("The response of TagsApi->tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_create** | [**TagCreate**](TagCreate.md)| The body containing the tag details. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag created. |  -  |
**400** | The request failed due to wrong data. Please check the provided parameters and try again. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The request failed since a tag with the given name already exists. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_delete**
> DeleteResult tags_tag_id_delete(tag_id)

Delete a Tag.

Delete the tag with the given ID.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_tag_api
from pnap_tag_api.models.delete_result import DeleteResult
from pnap_tag_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/tag-manager/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_tag_api.Configuration(
    host = "https://api.phoenixnap.com/tag-manager/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_tag_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_tag_api.TagsApi(api_client)
    tag_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The tag's ID.

    try:
        # Delete a Tag.
        api_response = api_instance.tags_tag_id_delete(tag_id)
        print("The response of TagsApi->tags_tag_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_tag_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The tag&#39;s ID. | 

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
**200** | Tag deleted. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_get**
> Tag tags_tag_id_get(tag_id)

Get a Tag.

Retrieve the tag with the given ID

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_tag_api
from pnap_tag_api.models.tag import Tag
from pnap_tag_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/tag-manager/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_tag_api.Configuration(
    host = "https://api.phoenixnap.com/tag-manager/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_tag_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_tag_api.TagsApi(api_client)
    tag_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The tag's ID.

    try:
        # Get a Tag.
        api_response = api_instance.tags_tag_id_get(tag_id)
        print("The response of TagsApi->tags_tag_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_tag_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The tag&#39;s ID. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Specific Tag details. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_tag_id_patch**
> Tag tags_tag_id_patch(tag_id, tag_update)

Modify a Tag.

Updates the tag with the given ID.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import os
import pnap_tag_api
from pnap_tag_api.models.tag import Tag
from pnap_tag_api.models.tag_update import TagUpdate
from pnap_tag_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.phoenixnap.com/tag-manager/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = pnap_tag_api.Configuration(
    host = "https://api.phoenixnap.com/tag-manager/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pnap_tag_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pnap_tag_api.TagsApi(api_client)
    tag_id = 'e6afba51-7de8-4080-83ab-0f915570659c' # str | The tag's ID.
    tag_update = pnap_tag_api.TagUpdate() # TagUpdate | The body containing the tag changes.

    try:
        # Modify a Tag.
        api_response = api_instance.tags_tag_id_patch(tag_id, tag_update)
        print("The response of TagsApi->tags_tag_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->tags_tag_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The tag&#39;s ID. | 
 **tag_update** | [**TagUpdate**](TagUpdate.md)| The body containing the tag changes. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tag partially updated. |  -  |
**401** | The request failed due to invalid credentials. Please check the provided credentials and try again. |  -  |
**403** | The request failed since this resource cannot be accessed by the provided credentials. |  -  |
**409** | The request failed since a tag with the given name already exists. |  -  |
**500** | The server encountered an unexpected condition that prevented it from fulfilling the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

