# SshKey

SSH Key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the SSH Key. | 
**default** | **bool** | Keys marked as default are always included on server creation and reset unless toggled off in creation/reset request. | 
**name** | **str** | Friendly SSH key name to represent an SSH key. | 
**key** | **str** | SSH Key value. | 
**fingerprint** | **str** | SSH key auto-generated SHA-256 fingerprint. | 
**created_on** | **datetime** | Date and time of creation. | 
**last_updated_on** | **datetime** | Date and time of last update. | 

## Example

```python
from pnap_bmc_api.models.ssh_key import SshKey

# TODO update the JSON string below
json = "{}"
# create an instance of SshKey from a JSON string
ssh_key_instance = SshKey.from_json(json)
# print the JSON string representation of the object
print SshKey.to_json()

# convert the object into a dict
ssh_key_dict = ssh_key_instance.to_dict()
# create an instance of SshKey from a dict
ssh_key_form_dict = ssh_key.from_dict(ssh_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


