# SchemaAutocomplete


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_numbers** | [**List[SchemaCourseNumberAcademicSessions]**](SchemaCourseNumberAcademicSessions.md) |  | [optional] 
**subject_prefix** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_autocomplete import SchemaAutocomplete

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAutocomplete from a JSON string
schema_autocomplete_instance = SchemaAutocomplete.from_json(json)
# print the JSON string representation of the object
print(SchemaAutocomplete.to_json())

# convert the object into a dict
schema_autocomplete_dict = schema_autocomplete_instance.to_dict()
# create an instance of SchemaAutocomplete from a dict
schema_autocomplete_from_dict = SchemaAutocomplete.from_dict(schema_autocomplete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


