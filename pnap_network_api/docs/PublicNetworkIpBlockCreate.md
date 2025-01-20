# PublicNetworkIpBlockCreate

Details of IP block to be assigned to Public Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The IP Block identifier. | 

## Example

```python
from pnap_network_api.models.public_network_ip_block_create import PublicNetworkIpBlockCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkIpBlockCreate from a JSON string
public_network_ip_block_create_instance = PublicNetworkIpBlockCreate.from_json(json)
# print the JSON string representation of the object
print PublicNetworkIpBlockCreate.to_json()

# convert the object into a dict
public_network_ip_block_create_dict = public_network_ip_block_create_instance.to_dict()
# create an instance of PublicNetworkIpBlockCreate from a dict
public_network_ip_block_create_form_dict = public_network_ip_block_create.from_dict(public_network_ip_block_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


