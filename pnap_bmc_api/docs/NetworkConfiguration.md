# NetworkConfiguration

Entire network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | The address of the gateway assigned / to assign to the server.&lt;br&gt; When used as part of request body, IP address has to be part of a private/public network or an IP block assigned to this server.&lt;br&gt; Gateway address also has to be assigned on an already deployed resource unless the address matches the BMC gateway address in a public network/IP block or the &#x60;force&#x60; query parameter is true. | [optional] 
**private_network_configuration** | [**PrivateNetworkConfiguration**](PrivateNetworkConfiguration.md) |  | [optional] 
**ip_blocks_configuration** | [**IpBlocksConfiguration**](IpBlocksConfiguration.md) |  | [optional] 
**public_network_configuration** | [**PublicNetworkConfiguration**](PublicNetworkConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


