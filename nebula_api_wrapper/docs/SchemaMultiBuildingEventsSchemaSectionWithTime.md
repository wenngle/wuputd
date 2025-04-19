# SchemaMultiBuildingEventsSchemaSectionWithTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildings** | [**List[SchemaSingleBuildingEventsSchemaSectionWithTime]**](SchemaSingleBuildingEventsSchemaSectionWithTime.md) |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_multi_building_events_schema_section_with_time import SchemaMultiBuildingEventsSchemaSectionWithTime

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaMultiBuildingEventsSchemaSectionWithTime from a JSON string
schema_multi_building_events_schema_section_with_time_instance = SchemaMultiBuildingEventsSchemaSectionWithTime.from_json(json)
# print the JSON string representation of the object
print(SchemaMultiBuildingEventsSchemaSectionWithTime.to_json())

# convert the object into a dict
schema_multi_building_events_schema_section_with_time_dict = schema_multi_building_events_schema_section_with_time_instance.to_dict()
# create an instance of SchemaMultiBuildingEventsSchemaSectionWithTime from a dict
schema_multi_building_events_schema_section_with_time_from_dict = SchemaMultiBuildingEventsSchemaSectionWithTime.from_dict(schema_multi_building_events_schema_section_with_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


