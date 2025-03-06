# PublicNetworkModify

Public Network Modifiable Details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A friendly name given to the network. This name should be unique. | [optional] 
**description** | **str** | The description of this public network | [optional] 
**ra_enabled** | **bool** | Boolean indicating whether Router Advertisement is enabled. Only applicable for Network with IPv6 Blocks. | [optional] 

## Example

```python
from pnap_network_api.models.public_network_modify import PublicNetworkModify

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkModify from a JSON string
public_network_modify_instance = PublicNetworkModify.from_json(json)
# print the JSON string representation of the object
print PublicNetworkModify.to_json()

# convert the object into a dict
public_network_modify_dict = public_network_modify_instance.to_dict()
# create an instance of PublicNetworkModify from a dict
public_network_modify_form_dict = public_network_modify.from_dict(public_network_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


