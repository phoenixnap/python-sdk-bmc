# SshKeyUpdate

SSH key modification model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Keys marked as default are always included on server creation and reset unless toggled off in creation/reset request. | 
**name** | **str** | SSH key name that can represent the key as an alternative to its ID. | 

## Example

```python
from pnap_bmc_api.models.ssh_key_update import SshKeyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyUpdate from a JSON string
ssh_key_update_instance = SshKeyUpdate.from_json(json)
# print the JSON string representation of the object
print SshKeyUpdate.to_json()

# convert the object into a dict
ssh_key_update_dict = ssh_key_update_instance.to_dict()
# create an instance of SshKeyUpdate from a dict
ssh_key_update_form_dict = ssh_key_update.from_dict(ssh_key_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


