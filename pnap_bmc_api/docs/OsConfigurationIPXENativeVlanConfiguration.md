# OsConfigurationIPXENativeVlanConfiguration

Specifies the native VLAN configuration for the server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vlan_id** | **int** | The VLAN ID of the network to be used as the native VLAN. The value must reference a public network with IP V4 block(s) or a public IP V4 block network to which the server is (or will be) attached. If omitted during provisioning, the native VLAN is matched to the configured/auto-purchased public IP V4 block. If no public IP block is available, a VLAN ID must be provided. The VLAN ID must belong to one of the public networks for any of the specified servers. During post-provisioning, if Native VLAN is omitted, the server will be configured with no native VLAN. If provided, the VLAN ID must be specified and must belong to any of the existing server public networks or IP block networks attached to the server.  | [optional] 
**static_dhcp_address_v4** | **str** | The static IP V4 address assigned to the server within the native VLAN. This address is set as the DHCP reservation and used for the iPXE boot process.  Value must be an available/unused IP V4 address within the native network usable IP range. If omitted, the first available IP in the native network will be automatically assigned. Therefore, at least one IP must be available within the native network.  | [optional] 
**status** | **str** | (Read-only) The status of the native VLAN configuration. | [optional] [readonly] 

## Example

```python
from pnap_bmc_api.models.os_configuration_ipxe_native_vlan_configuration import OsConfigurationIPXENativeVlanConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationIPXENativeVlanConfiguration from a JSON string
os_configuration_ipxe_native_vlan_configuration_instance = OsConfigurationIPXENativeVlanConfiguration.from_json(json)
# print the JSON string representation of the object
print(OsConfigurationIPXENativeVlanConfiguration.to_json())

# convert the object into a dict
os_configuration_ipxe_native_vlan_configuration_dict = os_configuration_ipxe_native_vlan_configuration_instance.to_dict()
# create an instance of OsConfigurationIPXENativeVlanConfiguration from a dict
os_configuration_ipxe_native_vlan_configuration_from_dict = OsConfigurationIPXENativeVlanConfiguration.from_dict(os_configuration_ipxe_native_vlan_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


