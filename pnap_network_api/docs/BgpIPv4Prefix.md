# BgpIPv4Prefix

The BGP IPv4 Prefix.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_allocation_id** | **str** | IPv4 allocation ID. | 
**cidr** | **str** | The IP block in CIDR format. | 
**status** | **str** | The BGP IPv4 Prefix status. Can have one of the following values: &#x60;PENDING&#x60;, &#x60;BUSY&#x60;, &#x60;READY&#x60;, &#x60;ERROR&#x60; and &#x60;DELETING&#x60;. | 
**is_bring_your_own_ip** | **bool** | Identifies IP as a &#x60;bring your own&#x60; IP block. | 
**in_use** | **bool** | The Boolean value of the BGP IPv4 Prefix is in use. | 

## Example

```python
from pnap_network_api.models.bgp_ipv4_prefix import BgpIPv4Prefix

# TODO update the JSON string below
json = "{}"
# create an instance of BgpIPv4Prefix from a JSON string
bgp_ipv4_prefix_instance = BgpIPv4Prefix.from_json(json)
# print the JSON string representation of the object
print BgpIPv4Prefix.to_json()

# convert the object into a dict
bgp_ipv4_prefix_dict = bgp_ipv4_prefix_instance.to_dict()
# create an instance of BgpIPv4Prefix from a dict
bgp_ipv4_prefix_form_dict = bgp_ipv4_prefix.from_dict(bgp_ipv4_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


