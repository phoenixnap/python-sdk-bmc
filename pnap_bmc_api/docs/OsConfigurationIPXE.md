# OsConfigurationIPXE

iPXE configuration details. Configures the server to boot using the iPXE network boot firmware with a custom boot script. Only applicable when osName is 'ipxe' and must not be provided for any other OS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the iPXE boot script used to start the server. | 
**native_vlan_configuration** | [**OsConfigurationIPXENativeVlanConfiguration**](OsConfigurationIPXENativeVlanConfiguration.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration_ipxe import OsConfigurationIPXE

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationIPXE from a JSON string
os_configuration_ipxe_instance = OsConfigurationIPXE.from_json(json)
# print the JSON string representation of the object
print(OsConfigurationIPXE.to_json())

# convert the object into a dict
os_configuration_ipxe_dict = os_configuration_ipxe_instance.to_dict()
# create an instance of OsConfigurationIPXE from a dict
os_configuration_ipxe_from_dict = OsConfigurationIPXE.from_dict(os_configuration_ipxe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


