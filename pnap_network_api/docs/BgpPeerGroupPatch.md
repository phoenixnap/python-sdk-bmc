# BgpPeerGroupPatch

Update a BGP Peer Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | The BGP Peer Group ASN. | [optional] 
**password** | **str** | The BGP Peer Group password. | [optional] 
**advertised_routes** | **str** | The Advertised routes for the BGP Peer Group. Can have one of the following values: &#x60;DEFAULT&#x60; and &#x60;NONE&#x60;. | [optional] 

## Example

```python
from pnap_network_api.models.bgp_peer_group_patch import BgpPeerGroupPatch

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerGroupPatch from a JSON string
bgp_peer_group_patch_instance = BgpPeerGroupPatch.from_json(json)
# print the JSON string representation of the object
print BgpPeerGroupPatch.to_json()

# convert the object into a dict
bgp_peer_group_patch_dict = bgp_peer_group_patch_instance.to_dict()
# create an instance of BgpPeerGroupPatch from a dict
bgp_peer_group_patch_form_dict = bgp_peer_group_patch.from_dict(bgp_peer_group_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


