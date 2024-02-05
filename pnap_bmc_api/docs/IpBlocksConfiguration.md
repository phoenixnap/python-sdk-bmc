# IpBlocksConfiguration

The IP blocks to assign to this server. <b>This is an exclusive allocation</b>, i.e. the IP blocks cannot be shared with other servers. If IpBlocksConfiguration is not defined, the purchase of a new IP block is determined by the networkType field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_type** | **str** | (Write-only) Determines the approach for configuring IP blocks for the server being provisioned. If PURCHASE_NEW is selected, the smallest supported range, depending on the operating system, is allocated to the server. | [optional] [default to 'PURCHASE_NEW']
**ip_blocks** | [**List[ServerIpBlock]**](ServerIpBlock.md) | Used to specify the previously purchased IP blocks to assign to this server upon provisioning. Used alongside the USER_DEFINED configurationType. | [optional] 

## Example

```python
from pnap_bmc_api.models.ip_blocks_configuration import IpBlocksConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlocksConfiguration from a JSON string
ip_blocks_configuration_instance = IpBlocksConfiguration.from_json(json)
# print the JSON string representation of the object
print IpBlocksConfiguration.to_json()

# convert the object into a dict
ip_blocks_configuration_dict = ip_blocks_configuration_instance.to_dict()
# create an instance of IpBlocksConfiguration from a dict
ip_blocks_configuration_form_dict = ip_blocks_configuration.from_dict(ip_blocks_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


