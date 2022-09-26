# PrivateNetwork

Private Network details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The private network identifier. | 
**name** | **str** | The friendly name of this private network. | 
**vlan_id** | **int** | The VLAN of this private network. | 
**type** | **str** | The type of the private network. | 
**location** | **str** | The location of this private network. | 
**location_default** | **bool** | Identifies network as the default private network for the specified location. | 
**cidr** | **str** | IP range associated with this private network in CIDR notation. | 
**servers** | [**[PrivateNetworkServer]**](PrivateNetworkServer.md) |  | 
**memberships** | [**[NetworkMembership]**](NetworkMembership.md) | A list of resources that are members of this private network. | 
**status** | **str** | The status of the private network. Can have one of the following values: &#x60;BUSY&#x60; or &#x60;READY&#x60;. | 
**created_on** | **datetime** | Date and time when this private network was created. | 
**description** | **str** | The description of this private network. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


