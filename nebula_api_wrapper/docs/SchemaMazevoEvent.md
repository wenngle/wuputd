# SchemaMazevoEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_name** | **str** |  | [optional] 
**date_time_end** | **str** |  | [optional] 
**date_time_start** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**organization_name** | **str** |  | [optional] 
**setup_minutes** | **float** |  | [optional] 
**status_color** | **str** |  | [optional] 
**status_description** | **str** |  | [optional] 
**teardown_minutes** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.schema_mazevo_event import SchemaMazevoEvent

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaMazevoEvent from a JSON string
schema_mazevo_event_instance = SchemaMazevoEvent.from_json(json)
# print the JSON string representation of the object
print(SchemaMazevoEvent.to_json())

# convert the object into a dict
schema_mazevo_event_dict = schema_mazevo_event_instance.to_dict()
# create an instance of SchemaMazevoEvent from a dict
schema_mazevo_event_from_dict = SchemaMazevoEvent.from_dict(schema_mazevo_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


