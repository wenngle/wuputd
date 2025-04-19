# SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SchemaMultiBuildingEventsSchemaSectionWithTime**](SchemaMultiBuildingEventsSchemaSectionWithTime.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_section_with_time import SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime from a JSON string
schema_api_response_schema_multi_building_events_schema_section_with_time_instance = SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime.to_json())

# convert the object into a dict
schema_api_response_schema_multi_building_events_schema_section_with_time_dict = schema_api_response_schema_multi_building_events_schema_section_with_time_instance.to_dict()
# create an instance of SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime from a dict
schema_api_response_schema_multi_building_events_schema_section_with_time_from_dict = SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime.from_dict(schema_api_response_schema_multi_building_events_schema_section_with_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


