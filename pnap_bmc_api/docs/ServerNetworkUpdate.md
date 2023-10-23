# ServerNetworkUpdate

Update network details of bare metal server.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **[str]** | List of IPs to be associated to the server.&lt;br&gt; Valid IP formats are single IPv4 addresses or IPv4 ranges. IPs must be within the network&#39;s range.&lt;br&gt; Setting the &#x60;force&#x60; query parameter to &#x60;true&#x60; allows you to:&lt;ul&gt; &lt;li&gt; Assign no specific IP addresses by designating an empty array of IPs. &lt;li&gt; Assign one or more IP addresses which are already configured on other resource(s) in network. &lt;li&gt; Assign IP addresses which are considered as reserved in network.&lt;/ul&gt; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


