# SchemaAPIResponseArrayInt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[int]** |  | [optional] 
**message** | **str** |  | [optional] 
**status** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAPIResponseArrayInt from a JSON string
schema_api_response_array_int_instance = SchemaAPIResponseArrayInt.from_json(json)
# print the JSON string representation of the object
print(SchemaAPIResponseArrayInt.to_json())

# convert the object into a dict
schema_api_response_array_int_dict = schema_api_response_array_int_instance.to_dict()
# create an instance of SchemaAPIResponseArrayInt from a dict
schema_api_response_array_int_from_dict = SchemaAPIResponseArrayInt.from_dict(schema_api_response_array_int_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


