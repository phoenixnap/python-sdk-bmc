# PrivateNetworkCreate

Details of Private Network to be created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The friendly name of this private network. This name should be unique. | 
**description** | **str** | The description of this private network. | [optional] 
**location** | **str** | The location of this private network. Supported values are &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**location_default** | **bool** | Identifies network as the default private network for the specified location. | [optional] [default to False]
**vlan_id** | **int** | The VLAN that will be assigned to this network. | [optional] 
**cidr** | **str** | IP range associated with this private network in CIDR notation.&lt;br&gt; Setting the &#x60;force&#x60; query parameter to &#x60;true&#x60; allows you to skip assigning a specific IP range to network. | [optional] 

## Example

```python
from pnap_network_api.models.private_network_create import PrivateNetworkCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkCreate from a JSON string
private_network_create_instance = PrivateNetworkCreate.from_json(json)
# print the JSON string representation of the object
print PrivateNetworkCreate.to_json()

# convert the object into a dict
private_network_create_dict = private_network_create_instance.to_dict()
# create an instance of PrivateNetworkCreate from a dict
private_network_create_form_dict = private_network_create.from_dict(private_network_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


