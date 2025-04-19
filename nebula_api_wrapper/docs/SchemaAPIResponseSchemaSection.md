# SchemaAPIResponseSchemaSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SchemaSection**](SchemaSection.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_schema_section import SchemaAPIResponseSchemaSection

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseSchemaSection from a JSON string
schema_api_response_schema_section_instance = SchemaAPIResponseSchemaSection.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseSchemaSection.to_json())

# convert the object into a dict
schema_api_response_schema_section_dict = schema_api_response_schema_section_instance.to_dict()
# create an instance of SchemaAPIResponseSchemaSection from a dict
schema_api_response_schema_section_from_dict = SchemaAPIResponseSchemaSection.from_dict(schema_api_response_schema_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


