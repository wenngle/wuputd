# SchemaTypedGradeDataDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grade_distribution** | **List[int]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_typed_grade_data_data_inner import SchemaTypedGradeDataDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaTypedGradeDataDataInner from a JSON string
schema_typed_grade_data_data_inner_instance = SchemaTypedGradeDataDataInner.from_json(json)
# print the JSON string representation of the object
print(SchemaTypedGradeDataDataInner.to_json())

# convert the object into a dict
schema_typed_grade_data_data_inner_dict = schema_typed_grade_data_data_inner_instance.to_dict()
# create an instance of SchemaTypedGradeDataDataInner from a dict
schema_typed_grade_data_data_inner_from_dict = SchemaTypedGradeDataDataInner.from_dict(schema_typed_grade_data_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


