# RancherServerMetadata

(Read Only) Connection parameters to use to connect to the Rancher Server Administrative GUI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The Rancher Server URL. | [optional] 
**username** | **str** | The username to use to login to the Rancher Server. This field is returned only as a response to the create cluster request. Make sure to take note or you will not be able to access the server. | [optional] 
**password** | **str** | This is the password to be used to login to the Rancher Server. This field is returned only as a response to the create cluster request. Make sure to take note or you will not be able to access the server. | [optional] 

## Example

```python
from pnap_rancher_solution_api.models.rancher_server_metadata import RancherServerMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of RancherServerMetadata from a JSON string
rancher_server_metadata_instance = RancherServerMetadata.from_json(json)
# print the JSON string representation of the object
print RancherServerMetadata.to_json()

# convert the object into a dict
rancher_server_metadata_dict = rancher_server_metadata_instance.to_dict()
# create an instance of RancherServerMetadata from a dict
rancher_server_metadata_form_dict = rancher_server_metadata.from_dict(rancher_server_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


