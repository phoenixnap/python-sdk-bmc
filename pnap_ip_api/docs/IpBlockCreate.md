# IpBlockCreate

IP Block Request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | IP Block location ID. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | 
**cidr_block_size** | **str** | CIDR IP Block Size. Currently this field should be set to either &#x60;/31&#x60;, &#x60;/30&#x60;, &#x60;/29&#x60; or &#x60;/28&#x60;. For a larger Block Size contact support. | 
**description** | **str** | The description of the IP Block. | [optional] 
**tags** | [**List[TagAssignmentRequest]**](TagAssignmentRequest.md) | Tags to set to the ip-block. To create a new tag or list all the existing tags that you can use, refer to [Tags API](https://developers.phoenixnap.com/docs/tags/1/overview). | [optional] 

## Example

```python
from pnap_ip_api.models.ip_block_create import IpBlockCreate

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlockCreate from a JSON string
ip_block_create_instance = IpBlockCreate.from_json(json)
# print the JSON string representation of the object
print IpBlockCreate.to_json()

# convert the object into a dict
ip_block_create_dict = ip_block_create_instance.to_dict()
# create an instance of IpBlockCreate from a dict
ip_block_create_form_dict = ip_block_create.from_dict(ip_block_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


