# OsConfigurationMapEsxi

VMWare ESXi configuration properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_password** | **str** | (Read-only) Password set for user root on an ESXi server which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_ui_url** | **str** | (Read-only) The URL of the management UI which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_access_allowed_ips** | **[str]** | List of IPs allowed to access the Management UI. Supported in single IP, CIDR and range format. When undefined, Management UI is disabled. This will only be returned in response to provisioning a server. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


