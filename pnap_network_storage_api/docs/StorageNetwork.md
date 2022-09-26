# StorageNetwork

Storage network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Storage network ID. | [optional] 
**name** | **str** | Storage network friendly name. | [optional] 
**description** | **str** | Storage network description. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**location** | **str** | Location of storage network. Currently this field should be set to &#x60;PHX&#x60; or &#x60;ASH&#x60;. | [optional] 
**network_id** | **str** | Id of network the storage belongs to. | [optional] 
**ips** | **[str]** | IP of the storage network. | [optional] 
**created_on** | **datetime** | Date and time when this storage network was created. | [optional] 
**volumes** | [**[Volume]**](Volume.md) | Volume for a storage network. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


