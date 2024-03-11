# EsxiOsConfiguration

Esxi OS configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_configuration** | [**EsxiDatastoreConfiguration**](EsxiDatastoreConfiguration.md) |  | [optional] 

## Example

```python
from pnap_bmc_api.models.esxi_os_configuration import EsxiOsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of EsxiOsConfiguration from a JSON string
esxi_os_configuration_instance = EsxiOsConfiguration.from_json(json)
# print the JSON string representation of the object
print EsxiOsConfiguration.to_json()

# convert the object into a dict
esxi_os_configuration_dict = esxi_os_configuration_instance.to_dict()
# create an instance of EsxiOsConfiguration from a dict
esxi_os_configuration_form_dict = esxi_os_configuration.from_dict(esxi_os_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


