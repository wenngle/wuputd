# SchemaAcademicSessionSections


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**academic_session** | [**SchemaSimpleAcademicSession**](SchemaSimpleAcademicSession.md) |  | [optional] 
**sections** | [**List[SchemaSectionNumberProfessors]**](SchemaSectionNumberProfessors.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_academic_session_sections import SchemaAcademicSessionSections

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAcademicSessionSections from a JSON string
schema_academic_session_sections_instance = SchemaAcademicSessionSections.from_json(json)
# print the JSON string representation of the object
print(SchemaAcademicSessionSections.to_json())

# convert the object into a dict
schema_academic_session_sections_dict = schema_academic_session_sections_instance.to_dict()
# create an instance of SchemaAcademicSessionSections from a dict
schema_academic_session_sections_from_dict = SchemaAcademicSessionSections.from_dict(schema_academic_session_sections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


