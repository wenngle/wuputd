# SchemaCourseNumberAcademicSessions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**academic_sessions** | [**List[SchemaAcademicSessionSections]**](SchemaAcademicSessionSections.md) |  | [optional] 
**course_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_course_number_academic_sessions import SchemaCourseNumberAcademicSessions

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaCourseNumberAcademicSessions from a JSON string
schema_course_number_academic_sessions_instance = SchemaCourseNumberAcademicSessions.from_json(json)
# print the JSON string representation of the object
print(SchemaCourseNumberAcademicSessions.to_json())

# convert the object into a dict
schema_course_number_academic_sessions_dict = schema_course_number_academic_sessions_instance.to_dict()
# create an instance of SchemaCourseNumberAcademicSessions from a dict
schema_course_number_academic_sessions_from_dict = SchemaCourseNumberAcademicSessions.from_dict(schema_course_number_academic_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


