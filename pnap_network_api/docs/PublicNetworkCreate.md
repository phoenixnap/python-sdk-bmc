# PublicNetworkCreate

Details of Public Network to be created.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The friendly name of this public network. This name should be unique. | 
**location** | **str** | The location of this public network. Supported values are &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**description** | **str** | The description of this public network. | [optional] 
**ip_blocks** | [**[PublicNetworkIpBlock]**](PublicNetworkIpBlock.md) | A list of IP Blocks that will be associated with this public network. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


