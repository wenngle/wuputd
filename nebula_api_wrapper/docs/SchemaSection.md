# SchemaSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**academic_session** | [**SchemaAcademicSession**](SchemaAcademicSession.md) |  | [optional] 
**attributes** | **object** |  | [optional] 
**core_flags** | **List[str]** |  | [optional] 
**course_reference** | **str** |  | [optional] 
**grade_distribution** | **List[int]** |  | [optional] 
**instruction_mode** | **str** |  | [optional] 
**internal_class_number** | **str** |  | [optional] 
**meetings** | [**List[SchemaMeeting]**](SchemaMeeting.md) |  | [optional] 
**professors** | **List[str]** |  | [optional] 
**section_corequisites** | [**SchemaCollectionRequirement**](SchemaCollectionRequirement.md) |  | [optional] 
**section_number** | **str** |  | [optional] 
**syllabus_uri** | **str** |  | [optional] 
**teaching_assistants** | [**List[SchemaAssistant]**](SchemaAssistant.md) |  | [optional] 

## Example

```python
from openapi_client.models.schema_section import SchemaSection

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSection from a JSON string
schema_section_instance = SchemaSection.from_json(json)
# print the JSON string representation of the object
print(SchemaSection.to_json())

# convert the object into a dict
schema_section_dict = schema_section_instance.to_dict()
# create an instance of SchemaSection from a dict
schema_section_from_dict = SchemaSection.from_dict(schema_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


