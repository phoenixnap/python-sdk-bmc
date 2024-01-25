# ServerIpBlock

IP block assigned to server

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The IP block&#39;s ID. | 
**vlan_id** | **int** | (Read-only) The VLAN on which this IP block has been configured within the network switch. | [optional] [readonly] 

## Example

```python
from pnap_bmc_api.models.server_ip_block import ServerIpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of ServerIpBlock from a JSON string
server_ip_block_instance = ServerIpBlock.from_json(json)
# print the JSON string representation of the object
print ServerIpBlock.to_json()

# convert the object into a dict
server_ip_block_dict = server_ip_block_instance.to_dict()
# create an instance of ServerIpBlock from a dict
server_ip_block_form_dict = server_ip_block.from_dict(server_ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


