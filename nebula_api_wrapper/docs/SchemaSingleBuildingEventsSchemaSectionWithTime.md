# SchemaSingleBuildingEventsSchemaSectionWithTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** |  | [optional] 
**rooms** | [**List[SchemaRoomEventsSchemaSectionWithTime]**](SchemaRoomEventsSchemaSectionWithTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_single_building_events_schema_section_with_time import SchemaSingleBuildingEventsSchemaSectionWithTime

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSingleBuildingEventsSchemaSectionWithTime from a JSON string
schema_single_building_events_schema_section_with_time_instance = SchemaSingleBuildingEventsSchemaSectionWithTime.from_json(json)
# print the JSON string representation of the object
print(SchemaSingleBuildingEventsSchemaSectionWithTime.to_json())

# convert the object into a dict
schema_single_building_events_schema_section_with_time_dict = schema_single_building_events_schema_section_with_time_instance.to_dict()
# create an instance of SchemaSingleBuildingEventsSchemaSectionWithTime from a dict
schema_single_building_events_schema_section_with_time_from_dict = SchemaSingleBuildingEventsSchemaSectionWithTime.from_dict(schema_single_building_events_schema_section_with_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


