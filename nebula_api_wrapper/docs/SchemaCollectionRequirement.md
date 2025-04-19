# SchemaCollectionRequirement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**options** | **List[object]** |  | [optional] 
**required** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_collection_requirement import SchemaCollectionRequirement

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaCollectionRequirement from a JSON string
schema_collection_requirement_instance = SchemaCollectionRequirement.from_json(json)
# print the JSON string representation of the object
print(SchemaCollectionRequirement.to_json())

# convert the object into a dict
schema_collection_requirement_dict = schema_collection_requirement_instance.to_dict()
# create an instance of SchemaCollectionRequirement from a dict
schema_collection_requirement_from_dict = SchemaCollectionRequirement.from_dict(schema_collection_requirement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


