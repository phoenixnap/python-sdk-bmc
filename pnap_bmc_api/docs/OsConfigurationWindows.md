# OsConfigurationWindows

Windows OS configuration properties.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rdp_allowed_ips** | **List[str]** | List of IPs allowed for RDP access to Windows OS. Supported in single IP, CIDR and range format. When undefined, RDP is disabled. To allow RDP access from any IP use 0.0.0.0/0. This will only be returned in response to provisioning a server. | [optional] 
**bring_your_own_license** | **bool** | Use a Bring Your Own (BYO) Windows license.  If true, the server is provisioned in trial mode, and you must activate your own license.  If false (default), the server includes a managed Windows license billed by the platform.  | [optional] [default to False]

## Example

```python
from pnap_bmc_api.models.os_configuration_windows import OsConfigurationWindows

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationWindows from a JSON string
os_configuration_windows_instance = OsConfigurationWindows.from_json(json)
# print the JSON string representation of the object
print(OsConfigurationWindows.to_json())

# convert the object into a dict
os_configuration_windows_dict = os_configuration_windows_instance.to_dict()
# create an instance of OsConfigurationWindows from a dict
os_configuration_windows_from_dict = OsConfigurationWindows.from_dict(os_configuration_windows_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


