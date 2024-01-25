# NetworkConfiguration

Entire network details of bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | The address of the gateway assigned / to assign to the server.&lt;br&gt; When used as part of request body, IP address has to be part of a private/public network or an IP block assigned to this server.&lt;br&gt; Gateway address also has to be assigned on an already deployed resource unless the address matches the BMC gateway address in a public network/IP block or the &#x60;force&#x60; query parameter is true. | [optional] 
**private_network_configuration** | [**PrivateNetworkConfiguration**](PrivateNetworkConfiguration.md) |  | [optional] 
**ip_blocks_configuration** | [**IpBlocksConfiguration**](IpBlocksConfiguration.md) |  | [optional] 
**public_network_configuration** | [**PublicNetworkConfiguration**](PublicNetworkConfiguration.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.network_configuration import NetworkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkConfiguration from a JSON string
network_configuration_instance = NetworkConfiguration.from_json(json)
# print the JSON string representation of the object
print NetworkConfiguration.to_json()

# convert the object into a dict
network_configuration_dict = network_configuration_instance.to_dict()
# create an instance of NetworkConfiguration from a dict
network_configuration_form_dict = network_configuration.from_dict(network_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


