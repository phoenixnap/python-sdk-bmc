# AsnDetails

BGP Peer Group ASN details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | **int** | The BGP Peer Group ASN. | 
**is_bring_your_own** | **bool** | True if the BGP Peer Group ASN is a &#x60;bring your own&#x60; ASN. | 
**verification_status** | **str** | The BGP Peer Group ASN verification status. Can have one of the following values: &#x60;PENDING_VERIFICATION&#x60;, &#x60;FAILED_VERIFICATION&#x60; and &#x60;VERIFIED&#x60;. | 
**verification_reason** | **str** | The BGP Peer Group ASN verification reason for the respective status. | [optional] 

## Example

```python
from pnap_network_api.models.asn_details import AsnDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AsnDetails from a JSON string
asn_details_instance = AsnDetails.from_json(json)
# print the JSON string representation of the object
print AsnDetails.to_json()

# convert the object into a dict
asn_details_dict = asn_details_instance.to_dict()
# create an instance of AsnDetails from a dict
asn_details_form_dict = asn_details.from_dict(asn_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


