# OsConfiguration

OS specific configuration properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**netris_controller** | [**OsConfigurationNetrisController**](OsConfigurationNetrisController.md) |  | [optional] 
**netris_softgate** | [**OsConfigurationNetrisSoftgate**](OsConfigurationNetrisSoftgate.md) |  | [optional] 
**windows** | [**OsConfigurationWindows**](OsConfigurationWindows.md) |  | [optional] 
**root_password** | **str** | (Read-only) Auto-generated password set for user &#39;root&#39; on an ESXi or Proxmox server.&lt;br&gt;  The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference. | [optional] [readonly] 
**management_ui_url** | **str** | (Read-only) The URL of the management UI which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_access_allowed_ips** | **List[str]** | List of IPs allowed to access the Management UI. Supported in single IP, CIDR and range format. When undefined, Management UI is disabled. This will only be returned in response to provisioning a server. | [optional] 
**install_os_to_ram** | **bool** | If true, OS will be installed to and booted from the server&#39;s RAM. On restart RAM OS will be lost and the server will not be reachable unless a custom bootable OS has been deployed. Follow the &lt;a href&#x3D;&#39;https://phoenixnap.com/kb/bmc-custom-os&#39; target&#x3D;&#39;_blank&#39;&gt;instructions&lt;/a&gt; on how to install custom OS on BMC. Only supported for ubuntu/focal and ubuntu/jammy. | [optional] [default to False]
**esxi** | [**EsxiOsConfiguration**](EsxiOsConfiguration.md) |  | [optional] 
**cloud_init** | [**OsConfigurationCloudInit**](OsConfigurationCloudInit.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration import OsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfiguration from a JSON string
os_configuration_instance = OsConfiguration.from_json(json)
# print the JSON string representation of the object
print OsConfiguration.to_json()

# convert the object into a dict
os_configuration_dict = os_configuration_instance.to_dict()
# create an instance of OsConfiguration from a dict
os_configuration_form_dict = os_configuration.from_dict(os_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


