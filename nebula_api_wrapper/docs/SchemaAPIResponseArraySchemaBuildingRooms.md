# SchemaAPIResponseArraySchemaBuildingRooms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaBuildingRooms]**](SchemaBuildingRooms.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_building_rooms import SchemaAPIResponseArraySchemaBuildingRooms

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaBuildingRooms from a JSON string
schema_api_response_array_schema_building_rooms_instance = SchemaAPIResponseArraySchemaBuildingRooms.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaBuildingRooms.to_json())

# convert the object into a dict
schema_api_response_array_schema_building_rooms_dict = schema_api_response_array_schema_building_rooms_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaBuildingRooms from a dict
schema_api_response_array_schema_building_rooms_from_dict = SchemaAPIResponseArraySchemaBuildingRooms.from_dict(schema_api_response_array_schema_building_rooms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


