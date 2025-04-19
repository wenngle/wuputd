# SchemaBucketInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **List[str]** |  | [optional] 
**created** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**updated** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.schema_bucket_info import SchemaBucketInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaBucketInfo from a JSON string
schema_bucket_info_instance = SchemaBucketInfo.from_json(json)
# print the JSON string representation of the object
print(SchemaBucketInfo.to_json())

# convert the object into a dict
schema_bucket_info_dict = schema_bucket_info_instance.to_dict()
# create an instance of SchemaBucketInfo from a dict
schema_bucket_info_from_dict = SchemaBucketInfo.from_dict(schema_bucket_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


