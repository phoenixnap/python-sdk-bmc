# BgpPeerGroupCreate

Create a BGP Peer Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The BGP Peer Group location. Can have one of the following values: &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**asn** | **int** | The BGP Peer Group ASN. | [default to 65401]
**password** | **str** | The BGP Peer Group password. | [optional] 
**advertised_routes** | **str** | The Advertised routes for the BGP Peer Group. Can have one of the following values: &#x60;DEFAULT&#x60; and &#x60;NONE&#x60;. | [default to 'NONE']

## Example

```python
from pnap_network_api.models.bgp_peer_group_create import BgpPeerGroupCreate

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerGroupCreate from a JSON string
bgp_peer_group_create_instance = BgpPeerGroupCreate.from_json(json)
# print the JSON string representation of the object
print BgpPeerGroupCreate.to_json()

# convert the object into a dict
bgp_peer_group_create_dict = bgp_peer_group_create_instance.to_dict()
# create an instance of BgpPeerGroupCreate from a dict
bgp_peer_group_create_form_dict = bgp_peer_group_create.from_dict(bgp_peer_group_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


