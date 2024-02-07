# PublicSubnetDetails

Details of public subnets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Public Subnet identifier as returned by the BMC API. | [optional] 
**cidr** | **str** | Classless Inter-Domain Routing | 
**size** | **str** | CIDR size | 

## Example

```python
from pnap_billing_api.models.public_subnet_details import PublicSubnetDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSubnetDetails from a JSON string
public_subnet_details_instance = PublicSubnetDetails.from_json(json)
# print the JSON string representation of the object
print PublicSubnetDetails.to_json()

# convert the object into a dict
public_subnet_details_dict = public_subnet_details_instance.to_dict()
# create an instance of PublicSubnetDetails from a dict
public_subnet_details_form_dict = public_subnet_details.from_dict(public_subnet_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


