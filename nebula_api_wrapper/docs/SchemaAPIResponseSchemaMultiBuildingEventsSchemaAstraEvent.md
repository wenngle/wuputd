# SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SchemaMultiBuildingEventsSchemaAstraEvent**](SchemaMultiBuildingEventsSchemaAstraEvent.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_astra_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent from a JSON string
schema_api_response_schema_multi_building_events_schema_astra_event_instance = SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent.to_json())

# convert the object into a dict
schema_api_response_schema_multi_building_events_schema_astra_event_dict = schema_api_response_schema_multi_building_events_schema_astra_event_instance.to_dict()
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent from a dict
schema_api_response_schema_multi_building_events_schema_astra_event_from_dict = SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent.from_dict(schema_api_response_schema_multi_building_events_schema_astra_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


