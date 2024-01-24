# UserInfo

Details related to the user / application performing this request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The BMC account ID | 
**client_id** | **str** | The client ID of the application | [optional] 
**username** | **str** | The logged in user or owner of the client application | 

## Example

```python
from pnap_audit_api.models.user_info import UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfo from a JSON string
user_info_instance = UserInfo.from_json(json)
# print the JSON string representation of the object
print UserInfo.to_json()

# convert the object into a dict
user_info_dict = user_info_instance.to_dict()
# create an instance of UserInfo from a dict
user_info_form_dict = user_info.from_dict(user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


