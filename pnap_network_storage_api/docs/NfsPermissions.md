# NfsPermissions

NFS specific permissions on a volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read_write** | **List[str]** | Read/Write access. | [optional] 
**read_only** | **List[str]** | Read only access. | [optional] 
**root_squash** | **List[str]** | Root squash permission. | [optional] 
**no_squash** | **List[str]** | No squash permission. | [optional] 
**all_squash** | **List[str]** | All squash permission. | [optional] 

## Example

```python
from pnap_network_storage_api.models.nfs_permissions import NfsPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of NfsPermissions from a JSON string
nfs_permissions_instance = NfsPermissions.from_json(json)
# print the JSON string representation of the object
print NfsPermissions.to_json()

# convert the object into a dict
nfs_permissions_dict = nfs_permissions_instance.to_dict()
# create an instance of NfsPermissions from a dict
nfs_permissions_form_dict = nfs_permissions.from_dict(nfs_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


