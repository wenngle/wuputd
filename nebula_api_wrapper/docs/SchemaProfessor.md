# SchemaProfessor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**image_uri** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**office** | [**SchemaLocation**](SchemaLocation.md) |  | [optional] 
**office_hours** | [**List[SchemaMeeting]**](SchemaMeeting.md) |  | [optional] 
**phone_number** | **str** |  | [optional] 
**profile_uri** | **str** |  | [optional] 
**sections** | **List[str]** |  | [optional] 
**titles** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.schema_professor import SchemaProfessor

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaProfessor from a JSON string
schema_professor_instance = SchemaProfessor.from_json(json)
# print the JSON string representation of the object
print(SchemaProfessor.to_json())

# convert the object into a dict
schema_professor_dict = schema_professor_instance.to_dict()
# create an instance of SchemaProfessor from a dict
schema_professor_from_dict = SchemaProfessor.from_dict(schema_professor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


