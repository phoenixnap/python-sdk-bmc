# GpuConfiguration

The GPU configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_name** | **str** | The long name of the GPU. | [optional] 
**count** | **int** | The number of GPUs. | [optional] 

## Example

```python
from pnap_bmc_api.models.gpu_configuration import GpuConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GpuConfiguration from a JSON string
gpu_configuration_instance = GpuConfiguration.from_json(json)
# print the JSON string representation of the object
print GpuConfiguration.to_json()

# convert the object into a dict
gpu_configuration_dict = gpu_configuration_instance.to_dict()
# create an instance of GpuConfiguration from a dict
gpu_configuration_form_dict = gpu_configuration.from_dict(gpu_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


