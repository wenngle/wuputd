# SchemaAPIResponseArraySchemaTypedGradeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaTypedGradeData]**](SchemaTypedGradeData.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_typed_grade_data import SchemaAPIResponseArraySchemaTypedGradeData

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaTypedGradeData from a JSON string
schema_api_response_array_schema_typed_grade_data_instance = SchemaAPIResponseArraySchemaTypedGradeData.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaTypedGradeData.to_json())

# convert the object into a dict
schema_api_response_array_schema_typed_grade_data_dict = schema_api_response_array_schema_typed_grade_data_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaTypedGradeData from a dict
schema_api_response_array_schema_typed_grade_data_from_dict = SchemaAPIResponseArraySchemaTypedGradeData.from_dict(schema_api_response_array_schema_typed_grade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


