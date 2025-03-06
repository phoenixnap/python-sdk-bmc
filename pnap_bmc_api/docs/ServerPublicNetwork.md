# ServerPublicNetwork

Public network details of bare metal server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The network identifier. | 
**ips** | **List[str]** | Configurable/configured IPs on the server.&lt;br&gt; At least 1 IP address is required. Valid IP format is single IP addresses. All IPs must be within the network&#39;s range.&lt;br&gt; Setting the &#x60;computeSlaacIp&#x60; field to &#x60;true&#x60; allows you to provide an empty array of IPs.&lt;br&gt; Additionally, setting the &#x60;force&#x60; query parameter to &#x60;true&#x60; allows you to:&lt;ul&gt; &lt;li&gt; Assign no specific IP addresses by designating an empty array of IPs. Note that at least one IP is required for the gateway address to be selected from this network. &lt;li&gt; Assign one or more IP addresses which are already configured on other resource(s) in network.&lt;/ul&gt; | [optional] 
**status_description** | **str** | (Read-only) The status of the assignment to the network. | [optional] [readonly] 
**compute_slaac_ip** | **bool** | (Write-only) Requests Stateless Address Autoconfiguration (SLAAC). Applicable for Network which contains IPv6 block(s). | [optional] 

## Example

```python
from pnap_bmc_api.models.server_public_network import ServerPublicNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ServerPublicNetwork from a JSON string
server_public_network_instance = ServerPublicNetwork.from_json(json)
# print the JSON string representation of the object
print ServerPublicNetwork.to_json()

# convert the object into a dict
server_public_network_dict = server_public_network_instance.to_dict()
# create an instance of ServerPublicNetwork from a dict
server_public_network_form_dict = server_public_network.from_dict(server_public_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


