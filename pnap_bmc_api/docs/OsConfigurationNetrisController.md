# OsConfigurationNetrisController

Netris Controller configuration properties. Knowledge base article to help you can be found <a href='https://phoenixnap.com/kb/netris-bare-metal-cloud#deploy-netris-controller' target='_blank'>here</a>.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_os** | **str** | (Read-only) Host OS on which the Netris Controller is installed. | [optional] [readonly] 
**netris_web_console_url** | **str** | (Read-only) The URL for the Netris Controller web console. It will only be returned in response to provisioning a server. | [optional] [readonly] 
**netris_user_password** | **str** | (Read-only) Auto-generated password set for user &#39;netris&#39; in the web console.&lt;br&gt;  The password is not stored and therefore will only be returned in response to provisioning a server. Copy and save it for future reference. | [optional] [readonly] 

## Example

```python
from pnap_bmc_api.models.os_configuration_netris_controller import OsConfigurationNetrisController

# TODO update the JSON string below
json = "{}"
# create an instance of OsConfigurationNetrisController from a JSON string
os_configuration_netris_controller_instance = OsConfigurationNetrisController.from_json(json)
# print the JSON string representation of the object
print OsConfigurationNetrisController.to_json()

# convert the object into a dict
os_configuration_netris_controller_dict = os_configuration_netris_controller_instance.to_dict()
# create an instance of OsConfigurationNetrisController from a dict
os_configuration_netris_controller_form_dict = os_configuration_netris_controller.from_dict(os_configuration_netris_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


