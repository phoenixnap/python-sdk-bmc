# BgpIpPrefix

The BGP IP Prefix.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_allocation_id** | **str** | IP allocation ID. | 
**cidr** | **str** | The IP block in CIDR format, dependent on IP version. | 
**ip_version** | **str** | The IP block version. | 
**status** | **str** | The BGP IP Prefix status. Can have one of the following values: &#x60;PENDING&#x60;, &#x60;BUSY&#x60;, &#x60;READY&#x60;, &#x60;ERROR&#x60; and &#x60;DELETING&#x60;. | 

## Example

```python
from pnap_network_api.models.bgp_ip_prefix import BgpIpPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of BgpIpPrefix from a JSON string
bgp_ip_prefix_instance = BgpIpPrefix.from_json(json)
# print the JSON string representation of the object
print(BgpIpPrefix.to_json())

# convert the object into a dict
bgp_ip_prefix_dict = bgp_ip_prefix_instance.to_dict()
# create an instance of BgpIpPrefix from a dict
bgp_ip_prefix_from_dict = BgpIpPrefix.from_dict(bgp_ip_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


