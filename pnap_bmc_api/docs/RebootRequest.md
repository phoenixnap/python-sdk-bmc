# RebootRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boot_type** | **str** | Specifies whether to boot via &#x60;IPXE&#x60; (requires script) or &#x60;STANDARD&#x60; (default mechanism, incompatible with &#x60;ipxeUrl&#x60;). | [optional] [default to 'STANDARD']
**ipxe_url** | **str** | The URL for the iPXE script, used only with &#x60;IPXE&#x60; boot type. If provided, it updates and replaces the existing stored URL; if not provided, the existing URL will be used. | [optional] 

## Example

```python
from pnap_bmc_api.models.reboot_request import RebootRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RebootRequest from a JSON string
reboot_request_instance = RebootRequest.from_json(json)
# print the JSON string representation of the object
print(RebootRequest.to_json())

# convert the object into a dict
reboot_request_dict = reboot_request_instance.to_dict()
# create an instance of RebootRequest from a dict
reboot_request_from_dict = RebootRequest.from_dict(reboot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


