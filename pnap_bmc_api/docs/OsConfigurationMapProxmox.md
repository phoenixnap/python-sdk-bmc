# OsConfigurationMapProxmox

Proxmox VE configuration properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_password** | **str** | (Read-only) Password set for user root on a Proxmox server which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_ui_url** | **str** | (Read-only) The URL of the management UI which will only be returned in response to provisioning a server. | [optional] [readonly] 
**management_access_allowed_ips** | **List[str]** | List of IPs allowed to access the Management UI. Supported in single IP, CIDR and range format. When undefined, Management UI is disabled. This will only be returned in response to provisioning a server. | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration_map_proxmox import OsConfigurationMapProxmox

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationMapProxmox from a JSON string
os_configuration_map_proxmox_instance = OsConfigurationMapProxmox.from_json(json)
# print the JSON string representation of the object
print OsConfigurationMapProxmox.to_json()

# convert the object into a dict
os_configuration_map_proxmox_dict = os_configuration_map_proxmox_instance.to_dict()
# create an instance of OsConfigurationMapProxmox from a dict
os_configuration_map_proxmox_form_dict = os_configuration_map_proxmox.from_dict(os_configuration_map_proxmox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


