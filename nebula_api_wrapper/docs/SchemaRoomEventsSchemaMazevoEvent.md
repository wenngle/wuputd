# SchemaRoomEventsSchemaMazevoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[SchemaMazevoEvent]**](SchemaMazevoEvent.md) |  | [optional] 
**room** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_room_events_schema_mazevo_event import SchemaRoomEventsSchemaMazevoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRoomEventsSchemaMazevoEvent from a JSON string
schema_room_events_schema_mazevo_event_instance = SchemaRoomEventsSchemaMazevoEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaRoomEventsSchemaMazevoEvent.to_json())

# convert the object into a dict
schema_room_events_schema_mazevo_event_dict = schema_room_events_schema_mazevo_event_instance.to_dict()
# create an instance of SchemaRoomEventsSchemaMazevoEvent from a dict
schema_room_events_schema_mazevo_event_from_dict = SchemaRoomEventsSchemaMazevoEvent.from_dict(schema_room_events_schema_mazevo_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


