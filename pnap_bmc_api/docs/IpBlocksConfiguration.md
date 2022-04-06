# IpBlocksConfiguration

The IP blocks to assign to this server. <b>This is an exclusive allocation</b>, i.e. the IP blocks cannot be shared with other servers. If IpBlocksConfiguration is not defined, the purchase of a new IP block is determined by the networkType field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_type** | **str** | Determines the approach for configuring IP blocks for the server being provisioned. If PURCHASE_NEW is selected, the smallest supported range, depending on the operating system, is allocated to the server. | [optional]  if omitted the server will use the default value of "PURCHASE_NEW"
**ip_blocks** | [**[ServerIpBlock]**](ServerIpBlock.md) | Used to specify the previously purchased IP blocks to assign to this server upon provisioning. Used alongside the USER_DEFINED configurationType. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


