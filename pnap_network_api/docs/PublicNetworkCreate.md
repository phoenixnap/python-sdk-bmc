# PublicNetworkCreate

Details of Public Network to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The friendly name of this public network. This name should be unique. | 
**description** | **str** | The description of this public network. | [optional] 
**location** | **str** | The location of this public network. Supported values are &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**vlan_id** | **int** | The VLAN that will be assigned to this network. | [optional] 
**ip_blocks** | [**List[PublicNetworkIpBlockCreate]**](PublicNetworkIpBlockCreate.md) | A list of IP Blocks that will be associated with this public network. Supported maximum of 10 IPv4 Blocks and 1 IPv6 Block. | [optional] 
**ra_enabled** | **bool** | Boolean indicating whether Router Advertisement is enabled. Only applicable for Network with IPv6 Blocks. | [optional] 

## Example

```python
from pnap_network_api.models.public_network_create import PublicNetworkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkCreate from a JSON string
public_network_create_instance = PublicNetworkCreate.from_json(json)
# print the JSON string representation of the object
print PublicNetworkCreate.to_json()

# convert the object into a dict
public_network_create_dict = public_network_create_instance.to_dict()
# create an instance of PublicNetworkCreate from a dict
public_network_create_form_dict = public_network_create.from_dict(public_network_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


