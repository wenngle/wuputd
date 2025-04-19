# SchemaBuildingRooms


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**building** | **str** |  | [optional] 
**rooms** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.schema_building_rooms import SchemaBuildingRooms

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaBuildingRooms from a JSON string
schema_building_rooms_instance = SchemaBuildingRooms.from_json(json)
# print the JSON string representation of the object
print(SchemaBuildingRooms.to_json())

# convert the object into a dict
schema_building_rooms_dict = schema_building_rooms_instance.to_dict()
# create an instance of SchemaBuildingRooms from a dict
schema_building_rooms_from_dict = SchemaBuildingRooms.from_dict(schema_building_rooms_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


