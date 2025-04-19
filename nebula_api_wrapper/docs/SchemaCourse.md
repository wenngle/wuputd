# SchemaCourse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**activity_type** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 
**catalog_year** | **str** |  | [optional] 
**class_level** | **str** |  | [optional] 
**co_or_pre_requisites** | [**SchemaCollectionRequirement**](SchemaCollectionRequirement.md) |  | [optional] 
**corequisites** | [**SchemaCollectionRequirement**](SchemaCollectionRequirement.md) |  | [optional] 
**course_number** | **str** |  | [optional] 
**credit_hours** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_reqs** | **str** |  | [optional] 
**grading** | **str** |  | [optional] 
**internal_course_number** | **str** |  | [optional] 
**laboratory_contact_hours** | **str** |  | [optional] 
**lecture_contact_hours** | **str** |  | [optional] 
**offering_frequency** | **str** |  | [optional] 
**prerequisites** | [**SchemaCollectionRequirement**](SchemaCollectionRequirement.md) |  | [optional] 
**school** | **str** |  | [optional] 
**sections** | **List[str]** |  | [optional] 
**subject_prefix** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_course import SchemaCourse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaCourse from a JSON string
schema_course_instance = SchemaCourse.from_json(json)
# print the JSON string representation of the object
print(SchemaCourse.to_json())

# convert the object into a dict
schema_course_dict = schema_course_instance.to_dict()
# create an instance of SchemaCourse from a dict
schema_course_from_dict = SchemaCourse.from_dict(schema_course_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


