# SchemaMeeting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**location** | [**SchemaLocation**](SchemaLocation.md) |  | [optional] 
**meeting_days** | **List[str]** |  | [optional] 
**modality** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_meeting import SchemaMeeting

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaMeeting from a JSON string
schema_meeting_instance = SchemaMeeting.from_json(json)
# print the JSON string representation of the object
print(SchemaMeeting.to_json())

# convert the object into a dict
schema_meeting_dict = schema_meeting_instance.to_dict()
# create an instance of SchemaMeeting from a dict
schema_meeting_from_dict = SchemaMeeting.from_dict(schema_meeting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


