# SchemaGradeData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**grade_distribution** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.schema_grade_data import SchemaGradeData

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaGradeData from a JSON string
schema_grade_data_instance = SchemaGradeData.from_json(json)
# print the JSON string representation of the object
print(SchemaGradeData.to_json())

# convert the object into a dict
schema_grade_data_dict = schema_grade_data_instance.to_dict()
# create an instance of SchemaGradeData from a dict
schema_grade_data_from_dict = SchemaGradeData.from_dict(schema_grade_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


