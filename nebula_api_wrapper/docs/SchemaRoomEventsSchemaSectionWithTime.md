# SchemaRoomEventsSchemaSectionWithTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[SchemaSectionWithTime]**](SchemaSectionWithTime.md) |  | [optional] 
**room** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_room_events_schema_section_with_time import SchemaRoomEventsSchemaSectionWithTime

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRoomEventsSchemaSectionWithTime from a JSON string
schema_room_events_schema_section_with_time_instance = SchemaRoomEventsSchemaSectionWithTime.from_json(json)
# print the JSON string representation of the object
print(SchemaRoomEventsSchemaSectionWithTime.to_json())

# convert the object into a dict
schema_room_events_schema_section_with_time_dict = schema_room_events_schema_section_with_time_instance.to_dict()
# create an instance of SchemaRoomEventsSchemaSectionWithTime from a dict
schema_room_events_schema_section_with_time_from_dict = SchemaRoomEventsSchemaSectionWithTime.from_dict(schema_room_events_schema_section_with_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


