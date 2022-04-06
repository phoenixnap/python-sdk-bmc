# PrivateNetworkConfiguration

Private network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | The address of the gateway assigned / to assign to the server. It&#39;ll be null and won&#39;t be displayed as part of response body if server is a member of both public and private networks. When used as part of request body, it has to match one of the IP addresses used in the existing assigned private networks for the relevant location. Also, this field can be submitted only when provisioning a server without being a member of any public network. | [optional] 
**configuration_type** | **str** | Determines the approach for configuring private network(s) for the server being provisioned. Currently this field should be set to &#x60;USE_OR_CREATE_DEFAULT&#x60; or &#x60;USER_DEFINED&#x60;. | [optional]  if omitted the server will use the default value of "USE_OR_CREATE_DEFAULT"
**private_networks** | [**[ServerPrivateNetwork]**](ServerPrivateNetwork.md) | The list of private networks this server is member of. When this field is part of request body, it&#39;ll be used to specify the private networks to assign to this server upon provisioning. Used alongside the &#x60;USER_DEFINED&#x60; configurationType. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


