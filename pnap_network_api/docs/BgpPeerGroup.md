# BgpPeerGroup

The Border Gateway Protocol (BGP) Peer Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the BGP Peer Group. | 
**status** | **str** | The BGP Peer Group status. Can have one of the following values: &#x60;PENDING&#x60;, &#x60;ON_HOLD&#x60;, &#x60;BUSY&#x60;, &#x60;READY&#x60;, &#x60;ERROR&#x60;, &#x60;PENDING_DELETION&#x60; and &#x60;DELETING&#x60;. | 
**location** | **str** | The BGP Peer Group location. Can have one of the following values: &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; and &#x60;AUS&#x60;. | 
**ipv4_prefixes** | [**List[BgpIPv4Prefix]**](BgpIPv4Prefix.md) | The List of the BGP Peer Group IPv4 prefixes. | 
**target_asn_details** | [**AsnDetails**](AsnDetails.md) |  | 
**active_asn_details** | [**AsnDetails**](AsnDetails.md) |  | [optional] 
**password** | **str** | The BGP Peer Group password. | 
**advertised_routes** | **str** | The Advertised routes for the BGP Peer Group. Can have one of the following values: &#x60;DEFAULT&#x60; and &#x60;NONE&#x60;. | 
**rpki_roa_origin_asn** | **int** | The RPKI ROA Origin ASN of the BGP Peer Group based on location. | 
**e_bgp_multi_hop** | **int** | The eBGP Multi-hop of the BGP Peer Group. | 
**peering_loopbacks_v4** | **List[str]** | The IPv4 Peering Loopback addresses of the BGP Peer Group. Valid IP formats are IPv4 addresses. | 
**keep_alive_timer_seconds** | **int** | The Keep Alive Timer in seconds of the BGP Peer Group. | 
**hold_timer_seconds** | **int** | The Hold Timer in seconds of the BGP Peer Group. | 
**created_on** | **str** | Date and time of creation. | [optional] 
**last_updated_on** | **str** | Date and time of last update. | [optional] 

## Example

```python
from pnap_network_api.models.bgp_peer_group import BgpPeerGroup

# TODO update the JSON string below
json = "{}"
# create an instance of BgpPeerGroup from a JSON string
bgp_peer_group_instance = BgpPeerGroup.from_json(json)
# print the JSON string representation of the object
print BgpPeerGroup.to_json()

# convert the object into a dict
bgp_peer_group_dict = bgp_peer_group_instance.to_dict()
# create an instance of BgpPeerGroup from a dict
bgp_peer_group_form_dict = bgp_peer_group.from_dict(bgp_peer_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


