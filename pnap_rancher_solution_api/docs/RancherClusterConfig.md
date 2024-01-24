# RancherClusterConfig

(Write-only) Rancher configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | Shared secret used to join a server or agent to a cluster. | [optional] 
**tls_san** | **str** | This maps to ranchers &#x60;tls-san&#x60;. Add additional hostname or IP as a Subject Alternative Name in the TLS cert. | [optional] 
**etcd_snapshot_schedule_cron** | **str** | This maps to ranchers &#x60;etcd-snapshot-schedule-cron&#x60;. Snapshot interval time in cron spec. eg. every 5 hours ‘0 */5 * * *’. Default: at 12 am/pm | [optional] [default to '0 0,12 * * *']
**etcd_snapshot_retention** | **int** | This maps to ranchers &#x60;etcd-snapshot-retention&#x60;. Number of snapshots to retain. | [optional] [default to 5]
**node_taint** | **str** | This maps to ranchers &#x60;node-taint&#x60;. Registering kubelet with set of taints. By default, server nodes will be schedulable and thus your workloads can get launched on them. If you wish to have a dedicated control plane where no user workloads will run, you can use taints. | [optional] 
**cluster_domain** | **str** | This maps to ranchers &#x60;cluster-domain&#x60;. Cluster Domain. | [optional] 
**certificates** | [**RancherClusterCertificates**](RancherClusterCertificates.md) |  | [optional] 

## Example

```python
from pnap_rancher_solution_api.models.rancher_cluster_config import RancherClusterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RancherClusterConfig from a JSON string
rancher_cluster_config_instance = RancherClusterConfig.from_json(json)
# print the JSON string representation of the object
print RancherClusterConfig.to_json()

# convert the object into a dict
rancher_cluster_config_dict = rancher_cluster_config_instance.to_dict()
# create an instance of RancherClusterConfig from a dict
rancher_cluster_config_form_dict = rancher_cluster_config.from_dict(rancher_cluster_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


