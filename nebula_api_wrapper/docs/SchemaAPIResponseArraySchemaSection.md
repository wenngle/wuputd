# SchemaAPIResponseArraySchemaSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SchemaSection]**](SchemaSection.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArraySchemaSection from a JSON string
schema_api_response_array_schema_section_instance = SchemaAPIResponseArraySchemaSection.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArraySchemaSection.to_json())

# convert the object into a dict
schema_api_response_array_schema_section_dict = schema_api_response_array_schema_section_instance.to_dict()
# create an instance of SchemaAPIResponseArraySchemaSection from a dict
schema_api_response_array_schema_section_from_dict = SchemaAPIResponseArraySchemaSection.from_dict(schema_api_response_array_schema_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


