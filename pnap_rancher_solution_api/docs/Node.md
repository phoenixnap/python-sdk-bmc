# Node

Node details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_id** | **str** | The server identifier. | [optional] 

## Example

```python
from pnap_rancher_solution_api.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print Node.to_json()

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_form_dict = node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


