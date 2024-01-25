# SshKeyCreate

SSH key creation model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Keys marked as default are always included on server creation and reset unless toggled off in creation/reset request. | 
**name** | **str** | Friendly SSH key name to represent an SSH key. | 
**key** | **str** | SSH key actual key value. | 

## Example

```python
from pnap_bmc_api.models.ssh_key_create import SshKeyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of SshKeyCreate from a JSON string
ssh_key_create_instance = SshKeyCreate.from_json(json)
# print the JSON string representation of the object
print SshKeyCreate.to_json()

# convert the object into a dict
ssh_key_create_dict = ssh_key_create_instance.to_dict()
# create an instance of SshKeyCreate from a dict
ssh_key_create_form_dict = ssh_key_create.from_dict(ssh_key_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


