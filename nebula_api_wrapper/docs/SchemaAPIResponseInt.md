# SchemaAPIResponseInt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_int import SchemaAPIResponseInt

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseInt from a JSON string
schema_api_response_int_instance = SchemaAPIResponseInt.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseInt.to_json())

# convert the object into a dict
schema_api_response_int_dict = schema_api_response_int_instance.to_dict()
# create an instance of SchemaAPIResponseInt from a dict
schema_api_response_int_from_dict = SchemaAPIResponseInt.from_dict(schema_api_response_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


