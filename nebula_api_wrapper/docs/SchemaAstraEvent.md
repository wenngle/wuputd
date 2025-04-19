# SchemaAstraEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_name** | **str** |  | [optional] 
**capacity** | **float** |  | [optional] 
**current_state** | **str** |  | [optional] 
**end_date** | **str** |  | [optional] 
**meeting_type** | **str** |  | [optional] 
**not_allowed_usage_mask** | **float** |  | [optional] 
**start_date** | **str** |  | [optional] 
**usage_color** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_astra_event import SchemaAstraEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaAstraEvent from a JSON string
schema_astra_event_instance = SchemaAstraEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaAstraEvent.to_json())

# convert the object into a dict
schema_astra_event_dict = schema_astra_event_instance.to_dict()
# create an instance of SchemaAstraEvent from a dict
schema_astra_event_from_dict = SchemaAstraEvent.from_dict(schema_astra_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


