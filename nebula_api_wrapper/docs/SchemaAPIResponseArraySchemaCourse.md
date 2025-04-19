# SchemaAPIResponseArraySchemaCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaCourse]**](SchemaCourse.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_course import SchemaAPIResponseArraySchemaCourse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaCourse from a JSON string
schema_api_response_array_schema_course_instance = SchemaAPIResponseArraySchemaCourse.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaCourse.to_json())

# convert the object into a dict
schema_api_response_array_schema_course_dict = schema_api_response_array_schema_course_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaCourse from a dict
schema_api_response_array_schema_course_from_dict = SchemaAPIResponseArraySchemaCourse.from_dict(schema_api_response_array_schema_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


