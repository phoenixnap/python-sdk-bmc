# NetworkConfiguration

Entire network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | The address of the gateway assigned / to assign to the server. When used as part of request body, IP address has to be part of private/public network assigned to this server. | [optional] 
**private_network_configuration** | [**PrivateNetworkConfiguration**](PrivateNetworkConfiguration.md) |  | [optional] 
**ip_blocks_configuration** | [**IpBlocksConfiguration**](IpBlocksConfiguration.md) |  | [optional] 
**public_network_configuration** | [**PublicNetworkConfiguration**](PublicNetworkConfiguration.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


