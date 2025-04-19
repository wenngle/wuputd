# SchemaAPIResponseSchemaObjectInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SchemaObjectInfo**](SchemaObjectInfo.md) |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_schema_object_info import SchemaAPIResponseSchemaObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseSchemaObjectInfo from a JSON string
schema_api_response_schema_object_info_instance = SchemaAPIResponseSchemaObjectInfo.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseSchemaObjectInfo.to_json())

# convert the object into a dict
schema_api_response_schema_object_info_dict = schema_api_response_schema_object_info_instance.to_dict()
# create an instance of SchemaAPIResponseSchemaObjectInfo from a dict
schema_api_response_schema_object_info_from_dict = SchemaAPIResponseSchemaObjectInfo.from_dict(schema_api_response_schema_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


