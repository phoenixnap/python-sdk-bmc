# ServerPrivateNetwork

Private network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The network identifier. | 
**ips** | **[str]** | IPs to configure/configured on the server.&lt;br&gt; Valid IP formats are single IPv4 addresses or IPv4 ranges. IPs must be within the network&#39;s range. Should be null or empty list if DHCP is true. &lt;br&gt; If field is undefined and DHCP is false, next available IP in network will be automatically allocated.&lt;br&gt; If the network contains a membership of type &#39;storage&#39;, the first twelve IPs are already reserved by BMC and not usable.&lt;br&gt; Setting the &#x60;force&#x60; query parameter to &#x60;true&#x60; allows you to:&lt;ul&gt; &lt;li&gt; Assign no specific IP addresses by designating an empty array of IPs. Note that at least one IP is required for the gateway address to be selected from this network. &lt;li&gt; Assign one or more IP addresses which are already configured on other resource(s) in network. &lt;li&gt; Assign IP addresses which are considered as reserved in network.&lt;/ul&gt; | [optional] 
**dhcp** | **bool** | Determines whether DHCP is enabled for this server. Should be false if any IPs are provided. Not supported for Proxmox OS. | [optional]  if omitted the server will use the default value of False
**status_description** | **str** | (Read-only) The status of the network. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


