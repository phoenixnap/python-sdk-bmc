# PublicNetwork

Public Network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The public network identifier. | 
**vlan_id** | **int** | The VLAN of this public network. | 
**memberships** | [**[NetworkMembership]**](NetworkMembership.md) | A list of resources that are members of this public network. | 
**name** | **str** | The friendly name of this public network. | 
**location** | **str** | The location of this public network. Supported values are &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**status** | **str** | The status of the public network. Can have one of the following values: &#x60;BUSY&#x60; or &#x60;READY&#x60;. | 
**created_on** | **datetime** | Date and time when this public network was created. | 
**ip_blocks** | [**[PublicNetworkIpBlock]**](PublicNetworkIpBlock.md) | A list of IP Blocks that are associated with this public network. | 
**description** | **str** | The description of this public network. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


