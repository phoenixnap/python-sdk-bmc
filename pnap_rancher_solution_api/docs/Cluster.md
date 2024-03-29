# Cluster

Cluster details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (Read-only) The Cluster identifier. | [optional] [readonly] 
**name** | **str** | Cluster name. This field is autogenerated if not provided. | [optional] 
**description** | **str** | Cluster description. | [optional] 
**location** | **str** | Deployment location. Cannot be changed once a cluster is created. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | 
**initial_cluster_version** | **str** | (Read-only) The Rancher version that was installed on the cluster during the first creation process. | [optional] [readonly] 
**node_pools** | [**List[NodePool]**](NodePool.md) | The node pools associated with the cluster. | [optional] 
**configuration** | [**RancherClusterConfig**](RancherClusterConfig.md) |  | [optional] 
**metadata** | [**RancherServerMetadata**](RancherServerMetadata.md) |  | [optional] [readonly] 
**workload_configuration** | [**WorkloadClusterConfig**](WorkloadClusterConfig.md) |  | [optional] 
**status_description** | **str** | (Read-Only) The cluster status | [optional] [readonly] 

## Example

```python
from pnap_rancher_solution_api.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print Cluster.to_json()

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_form_dict = cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


