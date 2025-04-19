# SchemaAPIResponseArraySchemaGradeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaGradeData]**](SchemaGradeData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_grade_data import SchemaAPIResponseArraySchemaGradeData

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaGradeData from a JSON string
schema_api_response_array_schema_grade_data_instance = SchemaAPIResponseArraySchemaGradeData.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaGradeData.to_json())

# convert the object into a dict
schema_api_response_array_schema_grade_data_dict = schema_api_response_array_schema_grade_data_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaGradeData from a dict
schema_api_response_array_schema_grade_data_from_dict = SchemaAPIResponseArraySchemaGradeData.from_dict(schema_api_response_array_schema_grade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


