# OsConfigurationMap

OS specific configuration properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**windows** | [**OsConfigurationWindows**](OsConfigurationWindows.md) |  | [optional] 
**esxi** | [**OsConfigurationMapEsxi**](OsConfigurationMapEsxi.md) |  | [optional] 
**proxmox** | [**OsConfigurationMapProxmox**](OsConfigurationMapProxmox.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration_map import OsConfigurationMap

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationMap from a JSON string
os_configuration_map_instance = OsConfigurationMap.from_json(json)
# print the JSON string representation of the object
print OsConfigurationMap.to_json()

# convert the object into a dict
os_configuration_map_dict = os_configuration_map_instance.to_dict()
# create an instance of OsConfigurationMap from a dict
os_configuration_map_form_dict = os_configuration_map.from_dict(os_configuration_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


