# SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SchemaMultiBuildingEventsSchemaMazevoEvent**](SchemaMultiBuildingEventsSchemaMazevoEvent.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_mazevo_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent from a JSON string
schema_api_response_schema_multi_building_events_schema_mazevo_event_instance = SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent.to_json())

# convert the object into a dict
schema_api_response_schema_multi_building_events_schema_mazevo_event_dict = schema_api_response_schema_multi_building_events_schema_mazevo_event_instance.to_dict()
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent from a dict
schema_api_response_schema_multi_building_events_schema_mazevo_event_from_dict = SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent.from_dict(schema_api_response_schema_multi_building_events_schema_mazevo_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


