# StorageNetworkCreate

Create Storage Network.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Storage network friendly name. | 
**location** | **str** | Location of storage network. Currently this field should be set to &#x60;PHX&#x60;. | 
**volumes** | [**[VolumeCreate]**](VolumeCreate.md) | Volume to be created alongside storage. Currently only 1 volume is supported. | 
**description** | **str** | Storage network description. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


