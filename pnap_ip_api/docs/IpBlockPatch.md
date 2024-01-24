# IpBlockPatch

IP Block patch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the Ip Block. | [optional] 

## Example

```python
from pnap_ip_api.models.ip_block_patch import IpBlockPatch

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockPatch from a JSON string
ip_block_patch_instance = IpBlockPatch.from_json(json)
# print the JSON string representation of the object
print IpBlockPatch.to_json()

# convert the object into a dict
ip_block_patch_dict = ip_block_patch_instance.to_dict()
# create an instance of IpBlockPatch from a dict
ip_block_patch_form_dict = ip_block_patch.from_dict(ip_block_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


