# SchemaTypedGradeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**data** | [**List[SchemaTypedGradeDataDataInner]**](SchemaTypedGradeDataDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_typed_grade_data import SchemaTypedGradeData

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaTypedGradeData from a JSON string
schema_typed_grade_data_instance = SchemaTypedGradeData.from_json(json)
# print the JSON string representation of the object
print(SchemaTypedGradeData.to_json())

# convert the object into a dict
schema_typed_grade_data_dict = schema_typed_grade_data_instance.to_dict()
# create an instance of SchemaTypedGradeData from a dict
schema_typed_grade_data_from_dict = SchemaTypedGradeData.from_dict(schema_typed_grade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


