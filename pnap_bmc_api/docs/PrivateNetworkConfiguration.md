# PrivateNetworkConfiguration

Private network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_address** | **str** | Deprecated in favour of a common gateway address across all networks available under NetworkConfiguration.&lt;br&gt; The address of the gateway assigned / to assign to the server.&lt;br&gt; When used as part of request body, IP address has to be part of private network assigned to this server.&lt;br&gt; Gateway address also has to be assigned on an already deployed resource unless the &#x60;force&#x60; query parameter is true. | [optional] 
**configuration_type** | **str** | Determines the approach for configuring private network(s) for the server being provisioned. Currently this field should be set to &#x60;USE_OR_CREATE_DEFAULT&#x60; or &#x60;USER_DEFINED&#x60;. | [optional]  if omitted the server will use the default value of "USE_OR_CREATE_DEFAULT"
**private_networks** | [**[ServerPrivateNetwork]**](ServerPrivateNetwork.md) | The list of private networks this server is member of. When this field is part of request body, it&#39;ll be used to specify the private networks to assign to this server upon provisioning. Used alongside the &#x60;USER_DEFINED&#x60; configurationType. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


