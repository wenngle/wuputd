# SchemaAssistant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**role** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_assistant import SchemaAssistant

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAssistant from a JSON string
schema_assistant_instance = SchemaAssistant.from_json(json)
# print the JSON string representation of the object
print(SchemaAssistant.to_json())

# convert the object into a dict
schema_assistant_dict = schema_assistant_instance.to_dict()
# create an instance of SchemaAssistant from a dict
schema_assistant_from_dict = SchemaAssistant.from_dict(schema_assistant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


