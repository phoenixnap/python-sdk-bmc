# PublicNetwork

Public Network details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The public network identifier. | 
**vlan_id** | **int** | The VLAN of this public network. | 
**memberships** | [**List[NetworkMembership]**](NetworkMembership.md) | A list of resources that are members of this public network. | 
**name** | **str** | The friendly name of this public network. | 
**location** | **str** | The location of this public network. Supported values are &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**description** | **str** | The description of this public network. | [optional] 
**status** | **str** | The status of the public network. Can have one of the following values: &#x60;BUSY&#x60;, &#x60;READY&#x60;, &#x60;DELETING&#x60; or &#x60;ERROR&#x60;. | 
**created_on** | **datetime** | Date and time when this public network was created. | 
**ip_blocks** | [**List[PublicNetworkIpBlock]**](PublicNetworkIpBlock.md) | A list of IP Blocks that are associated with this public network. | 

## Example

```python
from pnap_network_api.models.public_network import PublicNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetwork from a JSON string
public_network_instance = PublicNetwork.from_json(json)
# print the JSON string representation of the object
print PublicNetwork.to_json()

# convert the object into a dict
public_network_dict = public_network_instance.to_dict()
# create an instance of PublicNetwork from a dict
public_network_form_dict = public_network.from_dict(public_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


