# SchemaAPIResponseString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_string import SchemaAPIResponseString

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseString from a JSON string
schema_api_response_string_instance = SchemaAPIResponseString.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseString.to_json())

# convert the object into a dict
schema_api_response_string_dict = schema_api_response_string_instance.to_dict()
# create an instance of SchemaAPIResponseString from a dict
schema_api_response_string_from_dict = SchemaAPIResponseString.from_dict(schema_api_response_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


