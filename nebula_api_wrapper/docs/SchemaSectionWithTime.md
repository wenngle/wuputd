# SchemaSectionWithTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** |  | [optional] 
**section** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_section_with_time import SchemaSectionWithTime

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSectionWithTime from a JSON string
schema_section_with_time_instance = SchemaSectionWithTime.from_json(json)
# print the JSON string representation of the object
print(SchemaSectionWithTime.to_json())

# convert the object into a dict
schema_section_with_time_dict = schema_section_with_time_instance.to_dict()
# create an instance of SchemaSectionWithTime from a dict
schema_section_with_time_from_dict = SchemaSectionWithTime.from_dict(schema_section_with_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


