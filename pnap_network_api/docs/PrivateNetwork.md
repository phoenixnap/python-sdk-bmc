# PrivateNetwork

Private Network details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The private network identifier. | 
**name** | **str** | The friendly name of this private network. | 
**description** | **str** | The description of this private network. | [optional] 
**vlan_id** | **int** | The VLAN of this private network. | 
**type** | **str** | The type of the private network. | 
**location** | **str** | The location of this private network. | 
**location_default** | **bool** | Identifies network as the default private network for the specified location. | 
**cidr** | **str** | IP range associated with this private network in CIDR notation. | [optional] 
**servers** | [**List[PrivateNetworkServer]**](PrivateNetworkServer.md) |  | 
**memberships** | [**List[NetworkMembership]**](NetworkMembership.md) | A list of resources that are members of this private network. | 
**status** | **str** | The status of the private network. Can have one of the following values: &#x60;BUSY&#x60;, &#x60;READY&#x60;, &#x60;DELETING&#x60; or &#x60;ERROR&#x60;. | 
**created_on** | **datetime** | Date and time when this private network was created. | 

## Example

```python
from pnap_network_api.models.private_network import PrivateNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetwork from a JSON string
private_network_instance = PrivateNetwork.from_json(json)
# print the JSON string representation of the object
print PrivateNetwork.to_json()

# convert the object into a dict
private_network_dict = private_network_instance.to_dict()
# create an instance of PrivateNetwork from a dict
private_network_form_dict = private_network.from_dict(private_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


