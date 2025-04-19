# SchemaRoomEventsSchemaAstraEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[SchemaAstraEvent]**](SchemaAstraEvent.md) |  | [optional] 
**room** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_room_events_schema_astra_event import SchemaRoomEventsSchemaAstraEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaRoomEventsSchemaAstraEvent from a JSON string
schema_room_events_schema_astra_event_instance = SchemaRoomEventsSchemaAstraEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaRoomEventsSchemaAstraEvent.to_json())

# convert the object into a dict
schema_room_events_schema_astra_event_dict = schema_room_events_schema_astra_event_instance.to_dict()
# create an instance of SchemaRoomEventsSchemaAstraEvent from a dict
schema_room_events_schema_astra_event_from_dict = SchemaRoomEventsSchemaAstraEvent.from_dict(schema_room_events_schema_astra_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


