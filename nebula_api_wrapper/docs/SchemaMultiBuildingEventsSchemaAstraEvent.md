# SchemaMultiBuildingEventsSchemaAstraEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildings** | [**List[SchemaSingleBuildingEventsSchemaAstraEvent]**](SchemaSingleBuildingEventsSchemaAstraEvent.md) |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_multi_building_events_schema_astra_event import SchemaMultiBuildingEventsSchemaAstraEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaMultiBuildingEventsSchemaAstraEvent from a JSON string
schema_multi_building_events_schema_astra_event_instance = SchemaMultiBuildingEventsSchemaAstraEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaMultiBuildingEventsSchemaAstraEvent.to_json())

# convert the object into a dict
schema_multi_building_events_schema_astra_event_dict = schema_multi_building_events_schema_astra_event_instance.to_dict()
# create an instance of SchemaMultiBuildingEventsSchemaAstraEvent from a dict
schema_multi_building_events_schema_astra_event_from_dict = SchemaMultiBuildingEventsSchemaAstraEvent.from_dict(schema_multi_building_events_schema_astra_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


