# SchemaSingleBuildingEventsSchemaMazevoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** |  | [optional] 
**rooms** | [**List[SchemaRoomEventsSchemaMazevoEvent]**](SchemaRoomEventsSchemaMazevoEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_single_building_events_schema_mazevo_event import SchemaSingleBuildingEventsSchemaMazevoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSingleBuildingEventsSchemaMazevoEvent from a JSON string
schema_single_building_events_schema_mazevo_event_instance = SchemaSingleBuildingEventsSchemaMazevoEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaSingleBuildingEventsSchemaMazevoEvent.to_json())

# convert the object into a dict
schema_single_building_events_schema_mazevo_event_dict = schema_single_building_events_schema_mazevo_event_instance.to_dict()
# create an instance of SchemaSingleBuildingEventsSchemaMazevoEvent from a dict
schema_single_building_events_schema_mazevo_event_from_dict = SchemaSingleBuildingEventsSchemaMazevoEvent.from_dict(schema_single_building_events_schema_mazevo_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


