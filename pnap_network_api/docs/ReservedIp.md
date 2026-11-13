# ReservedIp

Reserved IP addresses which are not available for regular assignment. Some may be assigned when explicitly forced, as indicated by assignableWithForce.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** | A list containing reserved IP addresses or inclusive IP ranges. | 
**assignable_with_force** | **bool** | Indicates whether the reserved IP addresses can be assigned to a resource when the assignment request is made with &#x60;force&#x60; query parameter set to &#x60;true&#x60;. | 

## Example

```python
from pnap_network_api.models.reserved_ip import ReservedIp

# TODO update the JSON string below
json = "{}"
# create an instance of ReservedIp from a JSON string
reserved_ip_instance = ReservedIp.from_json(json)
# print the JSON string representation of the object
print(ReservedIp.to_json())

# convert the object into a dict
reserved_ip_dict = reserved_ip_instance.to_dict()
# create an instance of ReservedIp from a dict
reserved_ip_from_dict = ReservedIp.from_dict(reserved_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


