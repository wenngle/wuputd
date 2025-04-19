# SchemaSimpleProfessor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_simple_professor import SchemaSimpleProfessor

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaSimpleProfessor from a JSON string
schema_simple_professor_instance = SchemaSimpleProfessor.from_json(json)
# print the JSON string representation of the object
print(SchemaSimpleProfessor.to_json())

# convert the object into a dict
schema_simple_professor_dict = schema_simple_professor_instance.to_dict()
# create an instance of SchemaSimpleProfessor from a dict
schema_simple_professor_from_dict = SchemaSimpleProfessor.from_dict(schema_simple_professor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


