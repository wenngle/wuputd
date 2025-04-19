# SchemaAcademicSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**start_date** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_academic_session import SchemaAcademicSession

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAcademicSession from a JSON string
schema_academic_session_instance = SchemaAcademicSession.from_json(json)
# print the JSON string representation of the object
print(SchemaAcademicSession.to_json())

# convert the object into a dict
schema_academic_session_dict = schema_academic_session_instance.to_dict()
# create an instance of SchemaAcademicSession from a dict
schema_academic_session_from_dict = SchemaAcademicSession.from_dict(schema_academic_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


