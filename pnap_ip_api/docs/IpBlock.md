# IpBlock

IP Block Details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | IP Block identifier. | [optional] 
**location** | **str** | IP Block location ID. Currently this field should be set to &#x60;PHX&#x60;, &#x60;ASH&#x60;, &#x60;SGP&#x60;, &#x60;NLD&#x60;, &#x60;CHI&#x60;, &#x60;SEA&#x60; or &#x60;AUS&#x60;. | [optional] 
**cidr_block_size** | **str** | CIDR IP Block Size. Currently this field should be set to either &#x60;/31&#x60;, &#x60;/30&#x60;, &#x60;/29&#x60;, &#x60;/28&#x60;, &#x60;/27&#x60;, &#x60;/26&#x60;, &#x60;/25&#x60;, &#x60;/24&#x60;, &#x60;/23&#x60; or &#x60;/22&#x60;. | [optional] 
**cidr** | **str** | The IP Block in CIDR notation. | [optional] 
**ip_version** | **str** | The IP Version of the block. | [optional] 
**status** | **str** | The status of the IP Block. Can have one of the following values: &#x60;creating&#x60; , &#x60;assigning&#x60; , &#x60;error assigning&#x60; , &#x60;assigned&#x60; , &#x60;unassigning&#x60; , &#x60;error unassigning&#x60; or &#x60;unassigned&#x60;. | [optional] 
**assigned_resource_id** | **str** | ID of the resource assigned to the IP Block. | [optional] 
**assigned_resource_type** | **str** | Type of the resource assigned to the IP Block. | [optional] 
**description** | **str** | The description of the IP Block. | [optional] 
**tags** | [**List[TagAssignment]**](TagAssignment.md) | The tags assigned if any. | [optional] 
**is_bring_your_own** | **bool** | True if the IP block is a &#x60;bring your own&#x60; block. | [optional] 
**created_on** | **datetime** | Date and time when the IP block was created. | [optional] 

## Example

```python
from pnap_ip_api.models.ip_block import IpBlock

# TODO update the JSON string below
json = "{}"
# create an instance of IpBlock from a JSON string
ip_block_instance = IpBlock.from_json(json)
# print the JSON string representation of the object
print IpBlock.to_json()

# convert the object into a dict
ip_block_dict = ip_block_instance.to_dict()
# create an instance of IpBlock from a dict
ip_block_form_dict = ip_block.from_dict(ip_block_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


