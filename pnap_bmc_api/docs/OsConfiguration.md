# OsConfiguration

OS specific configuration properties.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windows** | [**OsConfigurationWindows**](OsConfigurationWindows.md) |  | [optional] 
**root_password** | **str** | Password set for user root on an ESXi server which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_ui_url** | **str** | The URL of the management UI which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_access_allowed_ips** | **[str]** | List of IPs allowed to access the Management UI. Supported in single IP, CIDR and range format. When undefined, Management UI is disabled. This will only be returned in response to provisioning a server. | [optional] 
**install_os_to_ram** | **bool** | If true, OS will be installed to and booted from the server&#39;s RAM. On restart RAM OS will be lost and the server will not be reachable unless a custom bootable OS has been deployed. Only supported for ubuntu/focal and ubuntu/jammy. | [optional]  if omitted the server will use the default value of False
**cloud_init** | [**OsConfigurationCloudInit**](OsConfigurationCloudInit.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


