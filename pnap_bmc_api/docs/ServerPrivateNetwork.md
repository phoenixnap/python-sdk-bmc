# ServerPrivateNetwork

Private network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The network identifier. | 
**ips** | **[str]** | IPs to configure/configured on the server. Should be null or empty list if DHCP is true. IPs must be within the network&#39;s range. If no IPs are provided and DHCP is false, next available IP in network will be automatically allocated. If the network contains a membership of type &#39;storage&#39;, the first twelve IPs are already reserved by BMC and not usable. These will return a Bad Request (400) if selected. | [optional] 
**dhcp** | **bool** | Determines whether DHCP is enabled for this server. Should be false if ips is not an empty list. Not supported for proxmox OS. | [optional]  if omitted the server will use the default value of False
**status_description** | **str** | The status of the network. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


