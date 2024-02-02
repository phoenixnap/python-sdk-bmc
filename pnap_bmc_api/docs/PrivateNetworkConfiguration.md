# PrivateNetworkConfiguration

Private network details of bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Deprecated in favour of a common gateway address across all networks available under NetworkConfiguration.&lt;br&gt; The address of the gateway assigned / to assign to the server.&lt;br&gt; When used as part of request body, IP address has to be part of private network assigned to this server.&lt;br&gt; Gateway address also has to be assigned on an already deployed resource unless the &#x60;force&#x60; query parameter is true. | [optional] 
**configuration_type** | **str** | (Write-only) Determines the approach for configuring private network(s) for the server being provisioned. Currently this field should be set to &#x60;USE_OR_CREATE_DEFAULT&#x60;, &#x60;USER_DEFINED&#x60; or &#x60;NONE&#x60;. | [optional] [default to 'USE_OR_CREATE_DEFAULT']
**private_networks** | [**List[ServerPrivateNetwork]**](ServerPrivateNetwork.md) | The list of private networks this server is member of. When this field is part of request body, it&#39;ll be used to specify the private networks to assign to this server upon provisioning. Used alongside the &#x60;USER_DEFINED&#x60; configurationType. | [optional] 

## Example

```python
from pnap_bmc_api.models.private_network_configuration import PrivateNetworkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkConfiguration from a JSON string
private_network_configuration_instance = PrivateNetworkConfiguration.from_json(json)
# print the JSON string representation of the object
print PrivateNetworkConfiguration.to_json()

# convert the object into a dict
private_network_configuration_dict = private_network_configuration_instance.to_dict()
# create an instance of PrivateNetworkConfiguration from a dict
private_network_configuration_form_dict = private_network_configuration.from_dict(private_network_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


