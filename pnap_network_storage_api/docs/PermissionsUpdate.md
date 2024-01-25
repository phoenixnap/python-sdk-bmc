# PermissionsUpdate

Update permissions for a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nfs** | [**NfsPermissionsUpdate**](NfsPermissionsUpdate.md) |  | [optional] 

## Example

```python
from pnap_network_storage_api.models.permissions_update import PermissionsUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsUpdate from a JSON string
permissions_update_instance = PermissionsUpdate.from_json(json)
# print the JSON string representation of the object
print PermissionsUpdate.to_json()

# convert the object into a dict
permissions_update_dict = permissions_update_instance.to_dict()
# create an instance of PermissionsUpdate from a dict
permissions_update_form_dict = permissions_update.from_dict(permissions_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


