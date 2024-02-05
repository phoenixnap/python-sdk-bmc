# PublicNetworkConfiguration

Public network details of bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_networks** | [**List[ServerPublicNetwork]**](ServerPublicNetwork.md) | The list of public networks this server is member of. When this field is part of request body, it&#39;ll be used to specify the public networks to assign to this server upon provisioning. | [optional] 

## Example

```python
from pnap_bmc_api.models.public_network_configuration import PublicNetworkConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PublicNetworkConfiguration from a JSON string
public_network_configuration_instance = PublicNetworkConfiguration.from_json(json)
# print the JSON string representation of the object
print PublicNetworkConfiguration.to_json()

# convert the object into a dict
public_network_configuration_dict = public_network_configuration_instance.to_dict()
# create an instance of PublicNetworkConfiguration from a dict
public_network_configuration_form_dict = public_network_configuration.from_dict(public_network_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


