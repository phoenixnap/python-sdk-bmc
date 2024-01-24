# ServerPatch

Patch bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of server. | [optional] 
**hostname** | **str** | Hostname of server | [optional] 

## Example

```python
from pnap_bmc_api.models.server_patch import ServerPatch

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPatch from a JSON string
server_patch_instance = ServerPatch.from_json(json)
# print the JSON string representation of the object
print ServerPatch.to_json()

# convert the object into a dict
server_patch_dict = server_patch_instance.to_dict()
# create an instance of ServerPatch from a dict
server_patch_form_dict = server_patch.from_dict(server_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


