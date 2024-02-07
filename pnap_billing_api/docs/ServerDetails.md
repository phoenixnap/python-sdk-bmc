# ServerDetails

Details of the server associated with this rated usage record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The server identifier as returned by the BMC API. | 
**hostname** | **str** | The server hostname. | 

## Example

```python
from pnap_billing_api.models.server_details import ServerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ServerDetails from a JSON string
server_details_instance = ServerDetails.from_json(json)
# print the JSON string representation of the object
print ServerDetails.to_json()

# convert the object into a dict
server_details_dict = server_details_instance.to_dict()
# create an instance of ServerDetails from a dict
server_details_form_dict = server_details.from_dict(server_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


