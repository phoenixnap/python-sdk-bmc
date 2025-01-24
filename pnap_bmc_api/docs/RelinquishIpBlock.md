# RelinquishIpBlock

Object used to determine whether to relinquish ownership of the IP block upon unassignment from server or server deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_ip_blocks** | **bool** | Determines whether the IP blocks assigned to the server should be deleted or not. | [optional] [default to False]

## Example

```python
from pnap_bmc_api.models.relinquish_ip_block import RelinquishIpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of RelinquishIpBlock from a JSON string
relinquish_ip_block_instance = RelinquishIpBlock.from_json(json)
# print the JSON string representation of the object
print RelinquishIpBlock.to_json()

# convert the object into a dict
relinquish_ip_block_dict = relinquish_ip_block_instance.to_dict()
# create an instance of RelinquishIpBlock from a dict
relinquish_ip_block_form_dict = relinquish_ip_block.from_dict(relinquish_ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


