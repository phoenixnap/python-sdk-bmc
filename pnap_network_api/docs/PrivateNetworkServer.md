# PrivateNetworkServer

Server details linked to the Private Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The server identifier. | 
**ips** | **List[str]** | List of private IPs associated to the server. | 

## Example

```python
from pnap_network_api.models.private_network_server import PrivateNetworkServer

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateNetworkServer from a JSON string
private_network_server_instance = PrivateNetworkServer.from_json(json)
# print the JSON string representation of the object
print PrivateNetworkServer.to_json()

# convert the object into a dict
private_network_server_dict = private_network_server_instance.to_dict()
# create an instance of PrivateNetworkServer from a dict
private_network_server_form_dict = private_network_server.from_dict(private_network_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


