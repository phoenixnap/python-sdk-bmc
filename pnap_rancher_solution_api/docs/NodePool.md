# NodePool

Node Pool Configuration. A node pool contains the name and configuration for a cluster's node pool. Node pools are set of nodes with a common configuration and specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the node pool. | [optional] 
**node_count** | **int** | Number of configured nodes, currently only node counts of 1 and 3 are possible. | [optional] 
**server_type** | **str** | Node server type. Cannot be changed once a server is created. Currently this field should be set to either &#x60;s0.d1.small&#x60;, &#x60;s0.d1.medium&#x60;, &#x60;s1.c1.small&#x60;, &#x60;s1.c1.medium&#x60;, &#x60;s1.c2.medium&#x60;, &#x60;s1.c2.large&#x60;, &#x60;s2.c1.small&#x60;, &#x60;s2.c1.medium&#x60;, &#x60;s2.c1.large&#x60;, &#x60;s2.c2.small&#x60;, &#x60;s2.c2.medium&#x60;, &#x60;s2.c2.large&#x60;, &#x60;s1.e1.small&#x60;, &#x60;s1.e1.medium&#x60;, &#x60;s1.e1.large&#x60;. | [optional] [default to 's0.d1.small']
**ssh_config** | [**SshConfig**](SshConfig.md) |  | [optional] 
**nodes** | [**List[Node]**](Node.md) | (Read-only) The nodes associated with this node pool. | [optional] [readonly] 

## Example

```python
from pnap_rancher_solution_api.models.node_pool import NodePool

# TODO update the JSON string below
json = "{}"
# create an instance of NodePool from a JSON string
node_pool_instance = NodePool.from_json(json)
# print the JSON string representation of the object
print NodePool.to_json()

# convert the object into a dict
node_pool_dict = node_pool_instance.to_dict()
# create an instance of NodePool from a dict
node_pool_form_dict = node_pool.from_dict(node_pool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


