# StorageRecord


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the rated usage record. | 
**product_category** | **str** | The category of the product associated with this usage record. | 
**product_code** | **str** | The code identifying the product associated to this usage record. | 
**location** | [**LocationEnum**](LocationEnum.md) |  | 
**year_month** | **str** | Year and month of the usage record. | [optional] 
**start_date_time** | **datetime** | The point in time (in UTC) when usage has started. | 
**end_date_time** | **datetime** | The point in time (in UTC) until usage has been rated. | 
**cost** | **int** | The rated usage in cents. | 
**cost_before_discount** | **int** | The cost in cents before discount. | [optional] 
**cost_description** | **str** | The rated usage cost description. | [optional] 
**price_model** | **str** | The price model applied to this usage record. | 
**unit_price** | **float** | The unit price. | 
**unit_price_description** | **str** | User friendly description of the unit price. | 
**quantity** | **float** | The number of units being charged. | 
**active** | **bool** | A flag indicating whether the rated usage record is still active. | 
**usage_session_id** | **str** | The usage session ID is used to correlate rated usage records across periods of time. For example, a server used for over a month will generate multiple rated usage records. The entire usage session cost can be computed by aggregating the records having the same usage session ID. It is usual to have one rated usage record per month or invoice. | 
**correlation_id** | **str** | Holds usage record id | 
**reservation_id** | **str** | Reservation id associated with this rated usage record. | [optional] 
**discount_details** | [**DiscountDetails**](DiscountDetails.md) |  | [optional] 
**metadata** | [**StorageDetails**](StorageDetails.md) |  | 

## Example

```python
from pnap_billing_api.models.storage_record import StorageRecord

# TODO update the JSON string below
json = "{}"
# create an instance of StorageRecord from a JSON string
storage_record_instance = StorageRecord.from_json(json)
# print the JSON string representation of the object
print StorageRecord.to_json()

# convert the object into a dict
storage_record_dict = storage_record_instance.to_dict()
# create an instance of StorageRecord from a dict
storage_record_form_dict = storage_record.from_dict(storage_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


