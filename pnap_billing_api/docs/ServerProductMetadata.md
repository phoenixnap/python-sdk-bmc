# ServerProductMetadata

Details of the server product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ram_in_gb** | **float** | RAM in GB. | 
**cpu** | **str** | CPU name. | 
**cpu_count** | **float** | Number of CPUs. | 
**cores_per_cpu** | **float** | The number of physical cores present on each CPU. | 
**cpu_frequency** | **float** | CPU frequency in GHz. | 
**network** | **str** | Server network. | 
**storage** | **str** | Server storage. | 

## Example

```python
from pnap_billing_api.models.server_product_metadata import ServerProductMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ServerProductMetadata from a JSON string
server_product_metadata_instance = ServerProductMetadata.from_json(json)
# print the JSON string representation of the object
print ServerProductMetadata.to_json()

# convert the object into a dict
server_product_metadata_dict = server_product_metadata_instance.to_dict()
# create an instance of ServerProductMetadata from a dict
server_product_metadata_form_dict = server_product_metadata.from_dict(server_product_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


