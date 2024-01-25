# OsConfigurationNetrisSoftgate

Netris Softgate configuration properties. Follow <a href='https://phoenixnap.com/kb/netris-bare-metal-cloud#deploy-netris-softgate' target='_blank'>instructions</a> for retrieving the required details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_os** | **str** | (Read-only) Host OS on which the Netris Softgate is installed. | [optional] [readonly] 
**controller_address** | **str** | (Write-only) IP address or hostname through which to reach the Netris Controller. | [optional] 
**controller_version** | **str** | (Write-only) The version of the Netris Controller to connect to. | [optional] 
**controller_auth_key** | **str** | (Write-only) The authentication key of the Netris Controller to connect to. Required for the softgate agent to be able to interact with the Netris Controller. | [optional] 

## Example

```python
from pnap_bmc_api.models.os_configuration_netris_softgate import OsConfigurationNetrisSoftgate

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationNetrisSoftgate from a JSON string
os_configuration_netris_softgate_instance = OsConfigurationNetrisSoftgate.from_json(json)
# print the JSON string representation of the object
print OsConfigurationNetrisSoftgate.to_json()

# convert the object into a dict
os_configuration_netris_softgate_dict = os_configuration_netris_softgate_instance.to_dict()
# create an instance of OsConfigurationNetrisSoftgate from a dict
os_configuration_netris_softgate_form_dict = os_configuration_netris_softgate.from_dict(os_configuration_netris_softgate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


