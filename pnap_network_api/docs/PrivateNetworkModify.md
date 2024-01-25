# PrivateNetworkModify

Object including details to be modified in the Private Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A friendly name given to the private network. This name should be unique. | 
**description** | **str** | A description of this private network | [optional] 
**location_default** | **bool** | Identifies network as the default private network for the specified location. | 

## Example

```python
from pnap_network_api.models.private_network_modify import PrivateNetworkModify

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkModify from a JSON string
private_network_modify_instance = PrivateNetworkModify.from_json(json)
# print the JSON string representation of the object
print PrivateNetworkModify.to_json()

# convert the object into a dict
private_network_modify_dict = private_network_modify_instance.to_dict()
# create an instance of PrivateNetworkModify from a dict
private_network_modify_form_dict = private_network_modify.from_dict(private_network_modify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


