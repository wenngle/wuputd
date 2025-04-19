# SchemaSectionNumberProfessors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**professors** | [**List[SchemaSimpleProfessor]**](SchemaSimpleProfessor.md) |  | [optional] 
**section_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_section_number_professors import SchemaSectionNumberProfessors

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSectionNumberProfessors from a JSON string
schema_section_number_professors_instance = SchemaSectionNumberProfessors.from_json(json)
# print the JSON string representation of the object
print(SchemaSectionNumberProfessors.to_json())

# convert the object into a dict
schema_section_number_professors_dict = schema_section_number_professors_instance.to_dict()
# create an instance of SchemaSectionNumberProfessors from a dict
schema_section_number_professors_from_dict = SchemaSectionNumberProfessors.from_dict(schema_section_number_professors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


