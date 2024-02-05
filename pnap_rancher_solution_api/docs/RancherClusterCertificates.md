# RancherClusterCertificates

(Write-only) Define the custom SSL certificates to be used instead of defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | The SSL CA certificate to be used for rancher admin. | [optional] 
**certificate** | **str** | The SSL certificate to be used for rancher admin. | [optional] 
**certificate_key** | **str** | The SSL certificate key to be used for rancher admin. | [optional] 

## Example

```python
from pnap_rancher_solution_api.models.rancher_cluster_certificates import RancherClusterCertificates

# TODO update the JSON string below
json = "{}"
# create an instance of RancherClusterCertificates from a JSON string
rancher_cluster_certificates_instance = RancherClusterCertificates.from_json(json)
# print the JSON string representation of the object
print RancherClusterCertificates.to_json()

# convert the object into a dict
rancher_cluster_certificates_dict = rancher_cluster_certificates_instance.to_dict()
# create an instance of RancherClusterCertificates from a dict
rancher_cluster_certificates_form_dict = rancher_cluster_certificates.from_dict(rancher_cluster_certificates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


