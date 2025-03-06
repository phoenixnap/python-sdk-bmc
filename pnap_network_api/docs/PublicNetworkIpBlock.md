# PublicNetworkIpBlock

The assigned IP block to the Public Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The IP Block identifier. | 
**cidr** | **str** | The CIDR notation of the IP block. | 
**used_ips_count** | **str** | The number of IPs used in the IP block. | 

## Example

```python
from pnap_network_api.models.public_network_ip_block import PublicNetworkIpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkIpBlock from a JSON string
public_network_ip_block_instance = PublicNetworkIpBlock.from_json(json)
# print the JSON string representation of the object
print PublicNetworkIpBlock.to_json()

# convert the object into a dict
public_network_ip_block_dict = public_network_ip_block_instance.to_dict()
# create an instance of PublicNetworkIpBlock from a dict
public_network_ip_block_form_dict = public_network_ip_block.from_dict(public_network_ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


