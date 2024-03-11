# EsxiDatastoreConfiguration

Esxi data storage configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore_name** | **str** | Datastore name | 

## Example

```python
from pnap_bmc_api.models.esxi_datastore_configuration import EsxiDatastoreConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of EsxiDatastoreConfiguration from a JSON string
esxi_datastore_configuration_instance = EsxiDatastoreConfiguration.from_json(json)
# print the JSON string representation of the object
print EsxiDatastoreConfiguration.to_json()

# convert the object into a dict
esxi_datastore_configuration_dict = esxi_datastore_configuration_instance.to_dict()
# create an instance of EsxiDatastoreConfiguration from a dict
esxi_datastore_configuration_form_dict = esxi_datastore_configuration.from_dict(esxi_datastore_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


