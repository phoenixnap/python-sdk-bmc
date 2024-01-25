# PermissionsCreate

Update permissions for a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs** | [**NfsPermissionsCreate**](NfsPermissionsCreate.md) |  | [optional] 

## Example

```python
from pnap_network_storage_api.models.permissions_create import PermissionsCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsCreate from a JSON string
permissions_create_instance = PermissionsCreate.from_json(json)
# print the JSON string representation of the object
print PermissionsCreate.to_json()

# convert the object into a dict
permissions_create_dict = permissions_create_instance.to_dict()
# create an instance of PermissionsCreate from a dict
permissions_create_form_dict = permissions_create.from_dict(permissions_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


