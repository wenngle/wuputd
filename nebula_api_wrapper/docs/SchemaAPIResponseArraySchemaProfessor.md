# SchemaAPIResponseArraySchemaProfessor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaProfessor]**](SchemaProfessor.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_professor import SchemaAPIResponseArraySchemaProfessor

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaProfessor from a JSON string
schema_api_response_array_schema_professor_instance = SchemaAPIResponseArraySchemaProfessor.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaProfessor.to_json())

# convert the object into a dict
schema_api_response_array_schema_professor_dict = schema_api_response_array_schema_professor_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaProfessor from a dict
schema_api_response_array_schema_professor_from_dict = SchemaAPIResponseArraySchemaProfessor.from_dict(schema_api_response_array_schema_professor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


