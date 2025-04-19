# SchemaObjectInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | [optional] 
**content_encoding** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**md5** | **List[int]** |  | [optional] 
**media_link** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **int** |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_object_info import SchemaObjectInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaObjectInfo from a JSON string
schema_object_info_instance = SchemaObjectInfo.from_json(json)
# print the JSON string representation of the object
print(SchemaObjectInfo.to_json())

# convert the object into a dict
schema_object_info_dict = schema_object_info_instance.to_dict()
# create an instance of SchemaObjectInfo from a dict
schema_object_info_from_dict = SchemaObjectInfo.from_dict(schema_object_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


