# NodePool

Node Pool Configuration. A node pool contains the name and configuration for a cluster's node pool. Node pools are set of nodes with a common configuration and specification.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the node pool. | [optional] 
**node_count** | **int** | Number of configured nodes, currently only node counts of 1 and 3 are possible. | [optional] 
**server_type** | **str** | Node server type. Cannot be changed once a server is created. Currently this field should be set to either &#x60;s0.d1.small&#x60;, &#x60;s0.d1.medium&#x60;, &#x60;s1.c1.small&#x60;, &#x60;s1.c1.medium&#x60;, &#x60;s1.c2.medium&#x60;, &#x60;s1.c2.large&#x60;, &#x60;s2.c1.small&#x60;, &#x60;s2.c1.medium&#x60;, &#x60;s2.c1.large&#x60;, &#x60;s2.c2.small&#x60;, &#x60;s2.c2.medium&#x60;, &#x60;s2.c2.large&#x60;, &#x60;s1.e1.small&#x60;, &#x60;s1.e1.medium&#x60;, &#x60;s1.e1.large&#x60;. | [optional]  if omitted the server will use the default value of "s0.d1.small"
**ssh_config** | [**NodePoolSshConfig**](NodePoolSshConfig.md) |  | [optional] 
**nodes** | [**[Node]**](Node.md) | (Read-only) The nodes associated with this node pool. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


