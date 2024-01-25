# NetworkMembership

Resource details linked to the Network.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource identifier. | 
**resource_type** | **str** | The resource&#39;s type. | 
**ips** | **List[str]** | List of IPs associated to the resource. | 

## Example

```python
from pnap_network_api.models.network_membership import NetworkMembership

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMembership from a JSON string
network_membership_instance = NetworkMembership.from_json(json)
# print the JSON string representation of the object
print NetworkMembership.to_json()

# convert the object into a dict
network_membership_dict = network_membership_instance.to_dict()
# create an instance of NetworkMembership from a dict
network_membership_form_dict = network_membership.from_dict(network_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


