# openapi_client.DefaultApi

All URIs are relative to *http://api.utdnebula.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**astra_events**](DefaultApi.md#astra_events) | **GET** /astra/{date} | 
[**autocomplete_dag**](DefaultApi.md#autocomplete_dag) | **GET** /autocomplete/dag | 
[**bucket_info**](DefaultApi.md#bucket_info) | **GET** /storage/{bucket} | 
[**course_all**](DefaultApi.md#course_all) | **GET** /course/all | 
[**course_by_id**](DefaultApi.md#course_by_id) | **GET** /course/{id} | 
[**course_search**](DefaultApi.md#course_search) | **GET** /course | 
[**course_section_by_id**](DefaultApi.md#course_section_by_id) | **GET** /course/{id}/sections | 
[**course_section_search**](DefaultApi.md#course_section_search) | **GET** /course/sections | 
[**delete_bucket**](DefaultApi.md#delete_bucket) | **DELETE** /storage/{bucket} | 
[**delete_object**](DefaultApi.md#delete_object) | **DELETE** /storage/{bucket}/{objectID} | 
[**events**](DefaultApi.md#events) | **GET** /events/{date} | 
[**events_by_building**](DefaultApi.md#events_by_building) | **GET** /events/{date}/{building} | 
[**grade_aggregation_by_semester**](DefaultApi.md#grade_aggregation_by_semester) | **GET** /grades/semester | 
[**grade_aggregation_overall**](DefaultApi.md#grade_aggregation_overall) | **GET** /grades/overall | 
[**grade_aggregation_section_type**](DefaultApi.md#grade_aggregation_section_type) | **GET** /grades/semester/sectionType | 
[**grades_by_course_id**](DefaultApi.md#grades_by_course_id) | **GET** /course/{id}/grades | 
[**grades_by_professor_id**](DefaultApi.md#grades_by_professor_id) | **GET** /professor/{id}/grades | 
[**grades_by_section_id**](DefaultApi.md#grades_by_section_id) | **GET** /section/{id}/grades | 
[**mazevo_events**](DefaultApi.md#mazevo_events) | **GET** /mazevo/{date} | 
[**object_info**](DefaultApi.md#object_info) | **GET** /storage/{bucket}/{objectID} | 
[**post_object**](DefaultApi.md#post_object) | **POST** /storage/{bucket}/{objectID} | 
[**professor_all**](DefaultApi.md#professor_all) | **GET** /professor/all | 
[**professor_by_id**](DefaultApi.md#professor_by_id) | **GET** /professor/{id} | 
[**professor_course_by_id**](DefaultApi.md#professor_course_by_id) | **GET** /professor/{id}/courses | 
[**professor_course_search**](DefaultApi.md#professor_course_search) | **GET** /professor/courses | 
[**professor_search**](DefaultApi.md#professor_search) | **GET** /professor | 
[**professor_section_by_id**](DefaultApi.md#professor_section_by_id) | **GET** /professor/{id}/sections | 
[**professor_section_search**](DefaultApi.md#professor_section_search) | **GET** /professor/sections | 
[**rooms**](DefaultApi.md#rooms) | **GET** /rooms | 
[**section_by_id**](DefaultApi.md#section_by_id) | **GET** /section/{id} | 
[**section_search**](DefaultApi.md#section_search) | **GET** /section | 
[**swagger**](DefaultApi.md#swagger) | **GET** /swagger/{file} | 
[**trends_course_section_search**](DefaultApi.md#trends_course_section_search) | **GET** /course/sections/trends | 
[**trends_professor_section_search**](DefaultApi.md#trends_professor_section_search) | **GET** /professor/sections/trends | 


# **astra_events**
> SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent astra_events(var_date)

"Returns AstraEvent based on the input date"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_astra_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    var_date = 'var_date_example' # str | date (ISO format) to retrieve astra events

    try:
        api_response = api_instance.astra_events(var_date)
        print("The response of DefaultApi->astra_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->astra_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| date (ISO format) to retrieve astra events | 

### Return type

[**SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent**](SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All AstraEvents with events on the inputted date |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_dag**
> SchemaAPIResponseArraySchemaAutocomplete autocomplete_dag()

"Returns an aggregation of courses for use in generating autocomplete DAGs"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_autocomplete import SchemaAPIResponseArraySchemaAutocomplete
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.autocomplete_dag()
        print("The response of DefaultApi->autocomplete_dag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->autocomplete_dag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaAPIResponseArraySchemaAutocomplete**](SchemaAPIResponseArraySchemaAutocomplete.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An aggregation of courses for use in generating autocomplete DAGs |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bucket_info**
> SchemaAPIResponseSchemaBucketInfo bucket_info(bucket, x_storage_key)

"Get info on a bucket. This route is restricted to only Nebula Labs internal Projects."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_bucket_info import SchemaAPIResponseSchemaBucketInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Name of the bucket
    x_storage_key = 'x_storage_key_example' # str | The internal storage key

    try:
        api_response = api_instance.bucket_info(bucket, x_storage_key)
        print("The response of DefaultApi->bucket_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bucket_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Name of the bucket | 
 **x_storage_key** | **str**| The internal storage key | 

### Return type

[**SchemaAPIResponseSchemaBucketInfo**](SchemaAPIResponseSchemaBucketInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The bucket&#39;s info |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_all**
> SchemaAPIResponseArraySchemaCourse course_all()

"Returns all courses"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_course import SchemaAPIResponseArraySchemaCourse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.course_all()
        print("The response of DefaultApi->course_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->course_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaAPIResponseArraySchemaCourse**](SchemaAPIResponseArraySchemaCourse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All courses |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_by_id**
> SchemaAPIResponseSchemaCourse course_by_id(id)

"Returns the course with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_course import SchemaAPIResponseSchemaCourse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the course to get

    try:
        api_response = api_instance.course_by_id(id)
        print("The response of DefaultApi->course_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->course_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the course to get | 

### Return type

[**SchemaAPIResponseSchemaCourse**](SchemaAPIResponseSchemaCourse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A course |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_search**
> SchemaAPIResponseArraySchemaCourse course_search(offset=offset, course_number=course_number, subject_prefix=subject_prefix, title=title, description=description, school=school, credit_hours=credit_hours, class_level=class_level, activity_type=activity_type, grading=grading, internal_course_number=internal_course_number, lecture_contact_hours=lecture_contact_hours, offering_frequency=offering_frequency)

"Returns paginated list of courses matching the query's string-typed key-value pairs. See offset for more details on pagination."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_course import SchemaAPIResponseArraySchemaCourse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    offset = 3.4 # float | The starting position of the current page of courses (e.g. For starting at the 17th course, offset=16). (optional)
    course_number = 'course_number_example' # str | The course's official number (optional)
    subject_prefix = 'subject_prefix_example' # str | The course's subject prefix (optional)
    title = 'title_example' # str | The course's title (optional)
    description = 'description_example' # str | The course's description (optional)
    school = 'school_example' # str | The course's school (optional)
    credit_hours = 'credit_hours_example' # str | The number of credit hours awarded by successful completion of the course (optional)
    class_level = 'class_level_example' # str | The level of education that this course course corresponds to (optional)
    activity_type = 'activity_type_example' # str | The type of class this course corresponds to (optional)
    grading = 'grading_example' # str | The grading status of this course (optional)
    internal_course_number = 'internal_course_number_example' # str | The internal (university) number used to reference this course (optional)
    lecture_contact_hours = 'lecture_contact_hours_example' # str | The weekly contact hours in lecture for a course (optional)
    offering_frequency = 'offering_frequency_example' # str | The frequency of offering a course (optional)

    try:
        api_response = api_instance.course_search(offset=offset, course_number=course_number, subject_prefix=subject_prefix, title=title, description=description, school=school, credit_hours=credit_hours, class_level=class_level, activity_type=activity_type, grading=grading, internal_course_number=internal_course_number, lecture_contact_hours=lecture_contact_hours, offering_frequency=offering_frequency)
        print("The response of DefaultApi->course_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->course_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| The starting position of the current page of courses (e.g. For starting at the 17th course, offset&#x3D;16). | [optional] 
 **course_number** | **str**| The course&#39;s official number | [optional] 
 **subject_prefix** | **str**| The course&#39;s subject prefix | [optional] 
 **title** | **str**| The course&#39;s title | [optional] 
 **description** | **str**| The course&#39;s description | [optional] 
 **school** | **str**| The course&#39;s school | [optional] 
 **credit_hours** | **str**| The number of credit hours awarded by successful completion of the course | [optional] 
 **class_level** | **str**| The level of education that this course course corresponds to | [optional] 
 **activity_type** | **str**| The type of class this course corresponds to | [optional] 
 **grading** | **str**| The grading status of this course | [optional] 
 **internal_course_number** | **str**| The internal (university) number used to reference this course | [optional] 
 **lecture_contact_hours** | **str**| The weekly contact hours in lecture for a course | [optional] 
 **offering_frequency** | **str**| The frequency of offering a course | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaCourse**](SchemaAPIResponseArraySchemaCourse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of courses |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_section_by_id**
> SchemaAPIResponseArraySchemaSection course_section_by_id(id)

"Returns the all of the sections of the course with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the course to get

    try:
        api_response = api_instance.course_section_by_id(id)
        print("The response of DefaultApi->course_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->course_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the course to get | 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sections |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **course_section_search**
> SchemaAPIResponseArraySchemaSection course_section_search(former_offset=former_offset, latter_offset=latter_offset, course_number=course_number, subject_prefix=subject_prefix, title=title, description=description, school=school, credit_hours=credit_hours, class_level=class_level, activity_type=activity_type, grading=grading, internal_course_number=internal_course_number, lecture_contact_hours=lecture_contact_hours, offering_frequency=offering_frequency)

"Returns paginated list of sections of all the courses matching the query's string-typed key-value pairs. See former_offset and latter_offset for pagination details."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    former_offset = 3.4 # float | The starting position of the current page of courses (e.g. For starting at the 17th course, former_offset=16). (optional)
    latter_offset = 3.4 # float | The starting position of the current page of sections (e.g. For starting at the 4th section, latter_offset=3). (optional)
    course_number = 'course_number_example' # str | The course's official number (optional)
    subject_prefix = 'subject_prefix_example' # str | The course's subject prefix (optional)
    title = 'title_example' # str | The course's title (optional)
    description = 'description_example' # str | The course's description (optional)
    school = 'school_example' # str | The course's school (optional)
    credit_hours = 'credit_hours_example' # str | The number of credit hours awarded by successful completion of the course (optional)
    class_level = 'class_level_example' # str | The level of education that this course course corresponds to (optional)
    activity_type = 'activity_type_example' # str | The type of class this course corresponds to (optional)
    grading = 'grading_example' # str | The grading status of this course (optional)
    internal_course_number = 'internal_course_number_example' # str | The internal (university) number used to reference this course (optional)
    lecture_contact_hours = 'lecture_contact_hours_example' # str | The weekly contact hours in lecture for a course (optional)
    offering_frequency = 'offering_frequency_example' # str | The frequency of offering a course (optional)

    try:
        api_response = api_instance.course_section_search(former_offset=former_offset, latter_offset=latter_offset, course_number=course_number, subject_prefix=subject_prefix, title=title, description=description, school=school, credit_hours=credit_hours, class_level=class_level, activity_type=activity_type, grading=grading, internal_course_number=internal_course_number, lecture_contact_hours=lecture_contact_hours, offering_frequency=offering_frequency)
        print("The response of DefaultApi->course_section_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->course_section_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **former_offset** | **float**| The starting position of the current page of courses (e.g. For starting at the 17th course, former_offset&#x3D;16). | [optional] 
 **latter_offset** | **float**| The starting position of the current page of sections (e.g. For starting at the 4th section, latter_offset&#x3D;3). | [optional] 
 **course_number** | **str**| The course&#39;s official number | [optional] 
 **subject_prefix** | **str**| The course&#39;s subject prefix | [optional] 
 **title** | **str**| The course&#39;s title | [optional] 
 **description** | **str**| The course&#39;s description | [optional] 
 **school** | **str**| The course&#39;s school | [optional] 
 **credit_hours** | **str**| The number of credit hours awarded by successful completion of the course | [optional] 
 **class_level** | **str**| The level of education that this course course corresponds to | [optional] 
 **activity_type** | **str**| The type of class this course corresponds to | [optional] 
 **grading** | **str**| The grading status of this course | [optional] 
 **internal_course_number** | **str**| The internal (university) number used to reference this course | [optional] 
 **lecture_contact_hours** | **str**| The weekly contact hours in lecture for a course | [optional] 
 **offering_frequency** | **str**| The frequency of offering a course | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sections |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bucket**
> SchemaAPIResponseInt delete_bucket(bucket, x_storage_key)

"Delete a bucket. This route is restricted to only Nebula Labs internal Projects."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_int import SchemaAPIResponseInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Name of the bucket
    x_storage_key = 'x_storage_key_example' # str | The internal storage key

    try:
        api_response = api_instance.delete_bucket(bucket, x_storage_key)
        print("The response of DefaultApi->delete_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Name of the bucket | 
 **x_storage_key** | **str**| The internal storage key | 

### Return type

[**SchemaAPIResponseInt**](SchemaAPIResponseInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of objects that were in the deleted bucket |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_object**
> SchemaAPIResponseInt delete_object(bucket, object_id, x_storage_key)

"Delete an object from a bucket. This route is restricted to only Nebula Labs internal Projects."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_int import SchemaAPIResponseInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Name of the bucket
    object_id = 'object_id_example' # str | ID of the object
    x_storage_key = 'x_storage_key_example' # str | The internal storage key

    try:
        api_response = api_instance.delete_object(bucket, object_id, x_storage_key)
        print("The response of DefaultApi->delete_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Name of the bucket | 
 **object_id** | **str**| ID of the object | 
 **x_storage_key** | **str**| The internal storage key | 

### Return type

[**SchemaAPIResponseInt**](SchemaAPIResponseInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Placeholder response, always set to 1 |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events**
> SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime events(var_date)

"Returns all sections with meetings on the specified date"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_section_with_time import SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    var_date = 'var_date_example' # str | ISO date of the set of events to get

    try:
        api_response = api_instance.events(var_date)
        print("The response of DefaultApi->events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| ISO date of the set of events to get | 

### Return type

[**SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime**](SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sections with meetings on the specified date |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **events_by_building**
> SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime events_by_building(var_date, building)

"Returns all sections with meetings on the specified date in the specified building"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_single_building_events_schema_section_with_time import SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    var_date = 'var_date_example' # str | ISO date of the set of events to get
    building = 'building_example' # str | building abbreviation of event locations

    try:
        api_response = api_instance.events_by_building(var_date, building)
        print("The response of DefaultApi->events_by_building:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->events_by_building: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| ISO date of the set of events to get | 
 **building** | **str**| building abbreviation of event locations | 

### Return type

[**SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime**](SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All sections with meetings on the specified date in the specified building |  -  |
**404** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grade_aggregation_by_semester**
> SchemaAPIResponseArraySchemaGradeData grade_aggregation_by_semester(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)

"Returns grade distributions aggregated by semester"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_grade_data import SchemaAPIResponseArraySchemaGradeData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    prefix = 'prefix_example' # str | The course's subject prefix (optional)
    number = 'number_example' # str | The course's official number (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professors's last name (optional)
    section_number = 'section_number_example' # str | The number of the section (optional)

    try:
        api_response = api_instance.grade_aggregation_by_semester(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)
        print("The response of DefaultApi->grade_aggregation_by_semester:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grade_aggregation_by_semester: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The course&#39;s subject prefix | [optional] 
 **number** | **str**| The course&#39;s official number | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professors&#39;s last name | [optional] 
 **section_number** | **str**| The number of the section | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaGradeData**](SchemaAPIResponseArraySchemaGradeData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of grade distributions for each semester included |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grade_aggregation_overall**
> SchemaAPIResponseArrayInt grade_aggregation_overall(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)

"Returns the overall grade distribution"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    prefix = 'prefix_example' # str | The course's subject prefix (optional)
    number = 'number_example' # str | The course's official number (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professors's last name (optional)
    section_number = 'section_number_example' # str | The number of the section (optional)

    try:
        api_response = api_instance.grade_aggregation_overall(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)
        print("The response of DefaultApi->grade_aggregation_overall:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grade_aggregation_overall: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The course&#39;s subject prefix | [optional] 
 **number** | **str**| The course&#39;s official number | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professors&#39;s last name | [optional] 
 **section_number** | **str**| The number of the section | [optional] 

### Return type

[**SchemaAPIResponseArrayInt**](SchemaAPIResponseArrayInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A grade distribution array |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grade_aggregation_section_type**
> SchemaAPIResponseArraySchemaTypedGradeData grade_aggregation_section_type(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)

"Returns the grade distributions aggregated by semester and broken down into section type"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_typed_grade_data import SchemaAPIResponseArraySchemaTypedGradeData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    prefix = 'prefix_example' # str | The course's subject prefix (optional)
    number = 'number_example' # str | The course's official number (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professors's last name (optional)
    section_number = 'section_number_example' # str | The number of the section (optional)

    try:
        api_response = api_instance.grade_aggregation_section_type(prefix=prefix, number=number, first_name=first_name, last_name=last_name, section_number=section_number)
        print("The response of DefaultApi->grade_aggregation_section_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grade_aggregation_section_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The course&#39;s subject prefix | [optional] 
 **number** | **str**| The course&#39;s official number | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professors&#39;s last name | [optional] 
 **section_number** | **str**| The number of the section | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaTypedGradeData**](SchemaAPIResponseArraySchemaTypedGradeData.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of grade distributions for each section type for each semester included |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grades_by_course_id**
> SchemaAPIResponseArrayInt grades_by_course_id(id)

"Returns the overall grade distribution for a course"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of course to get grades for

    try:
        api_response = api_instance.grades_by_course_id(id)
        print("The response of DefaultApi->grades_by_course_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grades_by_course_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of course to get grades for | 

### Return type

[**SchemaAPIResponseArrayInt**](SchemaAPIResponseArrayInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A grade distribution array for the course |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grades_by_professor_id**
> SchemaAPIResponseArrayInt grades_by_professor_id(id)

"Returns the overall grade distribution for a professor"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of professor to get grades for

    try:
        api_response = api_instance.grades_by_professor_id(id)
        print("The response of DefaultApi->grades_by_professor_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grades_by_professor_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of professor to get grades for | 

### Return type

[**SchemaAPIResponseArrayInt**](SchemaAPIResponseArrayInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A grade distribution array for the professor |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grades_by_section_id**
> SchemaAPIResponseArrayInt grades_by_section_id(id)

"Returns the overall grade distribution for a section"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of section to get grades for

    try:
        api_response = api_instance.grades_by_section_id(id)
        print("The response of DefaultApi->grades_by_section_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->grades_by_section_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of section to get grades for | 

### Return type

[**SchemaAPIResponseArrayInt**](SchemaAPIResponseArrayInt.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A grade distribution array for the section |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mazevo_events**
> SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent mazevo_events(var_date)

"Returns MazevoEvent based on the input date"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_mazevo_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    var_date = 'var_date_example' # str | date (ISO format) to retrieve mazevo events

    try:
        api_response = api_instance.mazevo_events(var_date)
        print("The response of DefaultApi->mazevo_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->mazevo_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_date** | **str**| date (ISO format) to retrieve mazevo events | 

### Return type

[**SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent**](SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All MazevoEvents with events on the inputted date |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **object_info**
> SchemaAPIResponseSchemaObjectInfo object_info(bucket, object_id, x_storage_key)

"Get info on an object in a bucket. This route is restricted to only Nebula Labs internal Projects."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_object_info import SchemaAPIResponseSchemaObjectInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Name of the bucket
    object_id = 'object_id_example' # str | ID of the object
    x_storage_key = 'x_storage_key_example' # str | The internal storage key

    try:
        api_response = api_instance.object_info(bucket, object_id, x_storage_key)
        print("The response of DefaultApi->object_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->object_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Name of the bucket | 
 **object_id** | **str**| ID of the object | 
 **x_storage_key** | **str**| The internal storage key | 

### Return type

[**SchemaAPIResponseSchemaObjectInfo**](SchemaAPIResponseSchemaObjectInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The object&#39;s info |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_object**
> SchemaAPIResponseSchemaObjectInfo post_object(bucket, object_id, x_storage_key, data)

"Upload an object to a bucket. This route is restricted to only Nebula Labs internal Projects."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_object_info import SchemaAPIResponseSchemaObjectInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    bucket = 'bucket_example' # str | Name of the bucket
    object_id = 'object_id_example' # str | ID of the object
    x_storage_key = 'x_storage_key_example' # str | The internal storage key
    data = 'data_example' # str | The data to upload

    try:
        api_response = api_instance.post_object(bucket, object_id, x_storage_key, data)
        print("The response of DefaultApi->post_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->post_object: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket** | **str**| Name of the bucket | 
 **object_id** | **str**| ID of the object | 
 **x_storage_key** | **str**| The internal storage key | 
 **data** | **str**| The data to upload | 

### Return type

[**SchemaAPIResponseSchemaObjectInfo**](SchemaAPIResponseSchemaObjectInfo.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The object&#39;s info |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_all**
> SchemaAPIResponseArraySchemaProfessor professor_all()

"Returns all professors"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_professor import SchemaAPIResponseArraySchemaProfessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.professor_all()
        print("The response of DefaultApi->professor_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaAPIResponseArraySchemaProfessor**](SchemaAPIResponseArraySchemaProfessor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All professors |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_by_id**
> SchemaAPIResponseSchemaProfessor professor_by_id(id)

"Returns the professor with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_professor import SchemaAPIResponseSchemaProfessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the professor to get

    try:
        api_response = api_instance.professor_by_id(id)
        print("The response of DefaultApi->professor_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the professor to get | 

### Return type

[**SchemaAPIResponseSchemaProfessor**](SchemaAPIResponseSchemaProfessor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A professor |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_course_by_id**
> SchemaAPIResponseArraySchemaCourse professor_course_by_id(id)

"Returns all the courses taught by the professor with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_course import SchemaAPIResponseArraySchemaCourse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the professor to get

    try:
        api_response = api_instance.professor_course_by_id(id)
        print("The response of DefaultApi->professor_course_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_course_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the professor to get | 

### Return type

[**SchemaAPIResponseArraySchemaCourse**](SchemaAPIResponseArraySchemaCourse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of courses |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_course_search**
> SchemaAPIResponseArraySchemaProfessor professor_course_search(former_offset=former_offset, latter_offset=latter_offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)

"Returns paginated list of the courses of all the professors matching the query's string-typed key-value pairs. See former_offset and latter_offset for pagination details."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_professor import SchemaAPIResponseArraySchemaProfessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    former_offset = 3.4 # float | The starting position of the current page of professors (e.g. For starting at the 17th professor, former_offset=16). (optional)
    latter_offset = 3.4 # float | The starting position of the current page of courses (e.g. For starting at the 4th course, latter_offset=3). (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professor's last name (optional)
    titles = 'titles_example' # str | One of the professor's title (optional)
    email = 'email_example' # str | The professor's email address (optional)
    phone_number = 'phone_number_example' # str | The professor's phone number (optional)
    office_building = 'office_building_example' # str | The building of the location of the professor's office (optional)
    office_room = 'office_room_example' # str | The room of the location of the professor's office (optional)
    office_map_uri = 'office_map_uri_example' # str | A hyperlink to the UTD room locator of the professor's office (optional)
    profile_uri = 'profile_uri_example' # str | A hyperlink pointing to the professor's official university profile (optional)
    image_uri = 'image_uri_example' # str | A link to the image used for the professor on the professor's official university profile (optional)
    office_hours_start_date = 'office_hours_start_date_example' # str | The start date of one of the office hours meetings of the professor (optional)
    office_hours_end_date = 'office_hours_end_date_example' # str | The end date of one of the office hours meetings of the professor (optional)
    office_hours_meeting_days = 'office_hours_meeting_days_example' # str | One of the days that one of the office hours meetings of the professor (optional)
    office_hours_start_time = 'office_hours_start_time_example' # str | The time one of the office hours meetings of the professor starts (optional)
    office_hours_end_time = 'office_hours_end_time_example' # str | The time one of the office hours meetings of the professor ends (optional)
    office_hours_modality = 'office_hours_modality_example' # str | The modality of one of the office hours meetings of the professor (optional)
    office_hours_location_building = 'office_hours_location_building_example' # str | The building of one of the office hours meetings of the professor (optional)
    office_hours_location_room = 'office_hours_location_room_example' # str | The room of one of the office hours meetings of the professor (optional)
    office_hours_location_map_uri = 'office_hours_location_map_uri_example' # str | A hyperlink to the UTD room locator of one of the office hours meetings of the professor (optional)

    try:
        api_response = api_instance.professor_course_search(former_offset=former_offset, latter_offset=latter_offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)
        print("The response of DefaultApi->professor_course_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_course_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **former_offset** | **float**| The starting position of the current page of professors (e.g. For starting at the 17th professor, former_offset&#x3D;16). | [optional] 
 **latter_offset** | **float**| The starting position of the current page of courses (e.g. For starting at the 4th course, latter_offset&#x3D;3). | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professor&#39;s last name | [optional] 
 **titles** | **str**| One of the professor&#39;s title | [optional] 
 **email** | **str**| The professor&#39;s email address | [optional] 
 **phone_number** | **str**| The professor&#39;s phone number | [optional] 
 **office_building** | **str**| The building of the location of the professor&#39;s office | [optional] 
 **office_room** | **str**| The room of the location of the professor&#39;s office | [optional] 
 **office_map_uri** | **str**| A hyperlink to the UTD room locator of the professor&#39;s office | [optional] 
 **profile_uri** | **str**| A hyperlink pointing to the professor&#39;s official university profile | [optional] 
 **image_uri** | **str**| A link to the image used for the professor on the professor&#39;s official university profile | [optional] 
 **office_hours_start_date** | **str**| The start date of one of the office hours meetings of the professor | [optional] 
 **office_hours_end_date** | **str**| The end date of one of the office hours meetings of the professor | [optional] 
 **office_hours_meeting_days** | **str**| One of the days that one of the office hours meetings of the professor | [optional] 
 **office_hours_start_time** | **str**| The time one of the office hours meetings of the professor starts | [optional] 
 **office_hours_end_time** | **str**| The time one of the office hours meetings of the professor ends | [optional] 
 **office_hours_modality** | **str**| The modality of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_building** | **str**| The building of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_room** | **str**| The room of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_map_uri** | **str**| A hyperlink to the UTD room locator of one of the office hours meetings of the professor | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaProfessor**](SchemaAPIResponseArraySchemaProfessor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of courses |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_search**
> SchemaAPIResponseArraySchemaProfessor professor_search(offset=offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)

"Returns paginated list of professors matching the query's string-typed key-value pairs. See offset for more details on pagination."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_professor import SchemaAPIResponseArraySchemaProfessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    offset = 3.4 # float | The starting position of the current page of professors (e.g. For starting at the 17th professor, offset=16). (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professor's last name (optional)
    titles = 'titles_example' # str | One of the professor's title (optional)
    email = 'email_example' # str | The professor's email address (optional)
    phone_number = 'phone_number_example' # str | The professor's phone number (optional)
    office_building = 'office_building_example' # str | The building of the location of the professor's office (optional)
    office_room = 'office_room_example' # str | The room of the location of the professor's office (optional)
    office_map_uri = 'office_map_uri_example' # str | A hyperlink to the UTD room locator of the professor's office (optional)
    profile_uri = 'profile_uri_example' # str | A hyperlink pointing to the professor's official university profile (optional)
    image_uri = 'image_uri_example' # str | A link to the image used for the professor on the professor's official university profile (optional)
    office_hours_start_date = 'office_hours_start_date_example' # str | The start date of one of the office hours meetings of the professor (optional)
    office_hours_end_date = 'office_hours_end_date_example' # str | The end date of one of the office hours meetings of the professor (optional)
    office_hours_meeting_days = 'office_hours_meeting_days_example' # str | One of the days that one of the office hours meetings of the professor (optional)
    office_hours_start_time = 'office_hours_start_time_example' # str | The time one of the office hours meetings of the professor starts (optional)
    office_hours_end_time = 'office_hours_end_time_example' # str | The time one of the office hours meetings of the professor ends (optional)
    office_hours_modality = 'office_hours_modality_example' # str | The modality of one of the office hours meetings of the professor (optional)
    office_hours_location_building = 'office_hours_location_building_example' # str | The building of one of the office hours meetings of the professor (optional)
    office_hours_location_room = 'office_hours_location_room_example' # str | The room of one of the office hours meetings of the professor (optional)
    office_hours_location_map_uri = 'office_hours_location_map_uri_example' # str | A hyperlink to the UTD room locator of one of the office hours meetings of the professor (optional)

    try:
        api_response = api_instance.professor_search(offset=offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)
        print("The response of DefaultApi->professor_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| The starting position of the current page of professors (e.g. For starting at the 17th professor, offset&#x3D;16). | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professor&#39;s last name | [optional] 
 **titles** | **str**| One of the professor&#39;s title | [optional] 
 **email** | **str**| The professor&#39;s email address | [optional] 
 **phone_number** | **str**| The professor&#39;s phone number | [optional] 
 **office_building** | **str**| The building of the location of the professor&#39;s office | [optional] 
 **office_room** | **str**| The room of the location of the professor&#39;s office | [optional] 
 **office_map_uri** | **str**| A hyperlink to the UTD room locator of the professor&#39;s office | [optional] 
 **profile_uri** | **str**| A hyperlink pointing to the professor&#39;s official university profile | [optional] 
 **image_uri** | **str**| A link to the image used for the professor on the professor&#39;s official university profile | [optional] 
 **office_hours_start_date** | **str**| The start date of one of the office hours meetings of the professor | [optional] 
 **office_hours_end_date** | **str**| The end date of one of the office hours meetings of the professor | [optional] 
 **office_hours_meeting_days** | **str**| One of the days that one of the office hours meetings of the professor | [optional] 
 **office_hours_start_time** | **str**| The time one of the office hours meetings of the professor starts | [optional] 
 **office_hours_end_time** | **str**| The time one of the office hours meetings of the professor ends | [optional] 
 **office_hours_modality** | **str**| The modality of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_building** | **str**| The building of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_room** | **str**| The room of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_map_uri** | **str**| A hyperlink to the UTD room locator of one of the office hours meetings of the professor | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaProfessor**](SchemaAPIResponseArraySchemaProfessor.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of professors |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_section_by_id**
> SchemaAPIResponseArraySchemaSection professor_section_by_id(id)

"Returns all the sections taught by the professor with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the professor to get

    try:
        api_response = api_instance.professor_section_by_id(id)
        print("The response of DefaultApi->professor_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the professor to get | 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sections |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **professor_section_search**
> SchemaAPIResponseArraySchemaSection professor_section_search(former_offset=former_offset, latter_offset=latter_offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)

"Returns paginated list of the sections of all the professors matching the query's string-typed key-value pairs. See former_offset and latter_offset for pagination details."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    former_offset = 3.4 # float | The starting position of the current page of professors (e.g. For starting at the 17th professor, former_offset=16). (optional)
    latter_offset = 3.4 # float | The starting position of the current page of sections (e.g. For starting at the 4th section, latter_offset=3). (optional)
    first_name = 'first_name_example' # str | The professor's first name (optional)
    last_name = 'last_name_example' # str | The professor's last name (optional)
    titles = 'titles_example' # str | One of the professor's title (optional)
    email = 'email_example' # str | The professor's email address (optional)
    phone_number = 'phone_number_example' # str | The professor's phone number (optional)
    office_building = 'office_building_example' # str | The building of the location of the professor's office (optional)
    office_room = 'office_room_example' # str | The room of the location of the professor's office (optional)
    office_map_uri = 'office_map_uri_example' # str | A hyperlink to the UTD room locator of the professor's office (optional)
    profile_uri = 'profile_uri_example' # str | A hyperlink pointing to the professor's official university profile (optional)
    image_uri = 'image_uri_example' # str | A link to the image used for the professor on the professor's official university profile (optional)
    office_hours_start_date = 'office_hours_start_date_example' # str | The start date of one of the office hours meetings of the professor (optional)
    office_hours_end_date = 'office_hours_end_date_example' # str | The end date of one of the office hours meetings of the professor (optional)
    office_hours_meeting_days = 'office_hours_meeting_days_example' # str | One of the days that one of the office hours meetings of the professor (optional)
    office_hours_start_time = 'office_hours_start_time_example' # str | The time one of the office hours meetings of the professor starts (optional)
    office_hours_end_time = 'office_hours_end_time_example' # str | The time one of the office hours meetings of the professor ends (optional)
    office_hours_modality = 'office_hours_modality_example' # str | The modality of one of the office hours meetings of the professor (optional)
    office_hours_location_building = 'office_hours_location_building_example' # str | The building of one of the office hours meetings of the professor (optional)
    office_hours_location_room = 'office_hours_location_room_example' # str | The room of one of the office hours meetings of the professor (optional)
    office_hours_location_map_uri = 'office_hours_location_map_uri_example' # str | A hyperlink to the UTD room locator of one of the office hours meetings of the professor (optional)

    try:
        api_response = api_instance.professor_section_search(former_offset=former_offset, latter_offset=latter_offset, first_name=first_name, last_name=last_name, titles=titles, email=email, phone_number=phone_number, office_building=office_building, office_room=office_room, office_map_uri=office_map_uri, profile_uri=profile_uri, image_uri=image_uri, office_hours_start_date=office_hours_start_date, office_hours_end_date=office_hours_end_date, office_hours_meeting_days=office_hours_meeting_days, office_hours_start_time=office_hours_start_time, office_hours_end_time=office_hours_end_time, office_hours_modality=office_hours_modality, office_hours_location_building=office_hours_location_building, office_hours_location_room=office_hours_location_room, office_hours_location_map_uri=office_hours_location_map_uri)
        print("The response of DefaultApi->professor_section_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->professor_section_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **former_offset** | **float**| The starting position of the current page of professors (e.g. For starting at the 17th professor, former_offset&#x3D;16). | [optional] 
 **latter_offset** | **float**| The starting position of the current page of sections (e.g. For starting at the 4th section, latter_offset&#x3D;3). | [optional] 
 **first_name** | **str**| The professor&#39;s first name | [optional] 
 **last_name** | **str**| The professor&#39;s last name | [optional] 
 **titles** | **str**| One of the professor&#39;s title | [optional] 
 **email** | **str**| The professor&#39;s email address | [optional] 
 **phone_number** | **str**| The professor&#39;s phone number | [optional] 
 **office_building** | **str**| The building of the location of the professor&#39;s office | [optional] 
 **office_room** | **str**| The room of the location of the professor&#39;s office | [optional] 
 **office_map_uri** | **str**| A hyperlink to the UTD room locator of the professor&#39;s office | [optional] 
 **profile_uri** | **str**| A hyperlink pointing to the professor&#39;s official university profile | [optional] 
 **image_uri** | **str**| A link to the image used for the professor on the professor&#39;s official university profile | [optional] 
 **office_hours_start_date** | **str**| The start date of one of the office hours meetings of the professor | [optional] 
 **office_hours_end_date** | **str**| The end date of one of the office hours meetings of the professor | [optional] 
 **office_hours_meeting_days** | **str**| One of the days that one of the office hours meetings of the professor | [optional] 
 **office_hours_start_time** | **str**| The time one of the office hours meetings of the professor starts | [optional] 
 **office_hours_end_time** | **str**| The time one of the office hours meetings of the professor ends | [optional] 
 **office_hours_modality** | **str**| The modality of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_building** | **str**| The building of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_room** | **str**| The room of one of the office hours meetings of the professor | [optional] 
 **office_hours_location_map_uri** | **str**| A hyperlink to the UTD room locator of one of the office hours meetings of the professor | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sections |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rooms**
> SchemaAPIResponseArraySchemaBuildingRooms rooms()

"Returns all schedulable rooms being used in the current and futures semesters from CourseBook, Astra, and Mazevo"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_building_rooms import SchemaAPIResponseArraySchemaBuildingRooms
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)

    try:
        api_response = api_instance.rooms()
        print("The response of DefaultApi->rooms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rooms: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaAPIResponseArraySchemaBuildingRooms**](SchemaAPIResponseArraySchemaBuildingRooms.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All schedulable rooms being used in the current and futures semesters from CourseBook, Astra, and Mazevo |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **section_by_id**
> SchemaAPIResponseSchemaSection section_by_id(id)

"Returns the section with given ID"

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_schema_section import SchemaAPIResponseSchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    id = 'id_example' # str | ID of the section to get

    try:
        api_response = api_instance.section_by_id(id)
        print("The response of DefaultApi->section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the section to get | 

### Return type

[**SchemaAPIResponseSchemaSection**](SchemaAPIResponseSchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A section |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **section_search**
> SchemaAPIResponseArraySchemaSection section_search(offset=offset, section_number=section_number, academic_session_name=academic_session_name, academic_session_start_date=academic_session_start_date, academic_session_end_date=academic_session_end_date, teaching_assistants_first_name=teaching_assistants_first_name, teaching_assistants_last_name=teaching_assistants_last_name, teaching_assistants_role=teaching_assistants_role, teaching_assistants_email=teaching_assistants_email, internal_class_number=internal_class_number, instruction_mode=instruction_mode, meetings_start_date=meetings_start_date, meetings_end_date=meetings_end_date, meetings_meeting_days=meetings_meeting_days, meetings_start_time=meetings_start_time, meetings_end_time=meetings_end_time, meetings_modality=meetings_modality, meetings_location_building=meetings_location_building, meetings_location_room=meetings_location_room, meetings_location_map_uri=meetings_location_map_uri, core_flags=core_flags, syllabus_uri=syllabus_uri)

"Returns paginated list of sections matching the query's string-typed key-value pairs. See offset for more details on pagination."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    offset = 3.4 # float | The starting position of the current page of sections (e.g. For starting at the 17th professor, offset=16). (optional)
    section_number = 'section_number_example' # str | The section's official number (optional)
    academic_session_name = 'academic_session_name_example' # str | The name of the academic session of the section (optional)
    academic_session_start_date = 'academic_session_start_date_example' # str | The date of classes starting for the section (optional)
    academic_session_end_date = 'academic_session_end_date_example' # str | The date of classes ending for the section (optional)
    teaching_assistants_first_name = 'teaching_assistants_first_name_example' # str | The first name of one of the teaching assistants of the section (optional)
    teaching_assistants_last_name = 'teaching_assistants_last_name_example' # str | The last name of one of the teaching assistants of the section (optional)
    teaching_assistants_role = 'teaching_assistants_role_example' # str | The role of one of the teaching assistants of the section (optional)
    teaching_assistants_email = 'teaching_assistants_email_example' # str | The email of one of the teaching assistants of the section (optional)
    internal_class_number = 'internal_class_number_example' # str | The internal (university) number used to reference this section (optional)
    instruction_mode = 'instruction_mode_example' # str | The instruction modality for this section (optional)
    meetings_start_date = 'meetings_start_date_example' # str | The start date of one of the section's meetings (optional)
    meetings_end_date = 'meetings_end_date_example' # str | The end date of one of the section's meetings (optional)
    meetings_meeting_days = 'meetings_meeting_days_example' # str | One of the days that one of the section's meetings (optional)
    meetings_start_time = 'meetings_start_time_example' # str | The time one of the section's meetings starts (optional)
    meetings_end_time = 'meetings_end_time_example' # str | The time one of the section's meetings ends (optional)
    meetings_modality = 'meetings_modality_example' # str | The modality of one of the section's meetings (optional)
    meetings_location_building = 'meetings_location_building_example' # str | The building of one of the section's meetings (optional)
    meetings_location_room = 'meetings_location_room_example' # str | The room of one of the section's meetings (optional)
    meetings_location_map_uri = 'meetings_location_map_uri_example' # str | A hyperlink to the UTD room locator of one of the section's meetings (optional)
    core_flags = 'core_flags_example' # str | One of core requirement codes this section fulfills (optional)
    syllabus_uri = 'syllabus_uri_example' # str | A link to the syllabus on the web (optional)

    try:
        api_response = api_instance.section_search(offset=offset, section_number=section_number, academic_session_name=academic_session_name, academic_session_start_date=academic_session_start_date, academic_session_end_date=academic_session_end_date, teaching_assistants_first_name=teaching_assistants_first_name, teaching_assistants_last_name=teaching_assistants_last_name, teaching_assistants_role=teaching_assistants_role, teaching_assistants_email=teaching_assistants_email, internal_class_number=internal_class_number, instruction_mode=instruction_mode, meetings_start_date=meetings_start_date, meetings_end_date=meetings_end_date, meetings_meeting_days=meetings_meeting_days, meetings_start_time=meetings_start_time, meetings_end_time=meetings_end_time, meetings_modality=meetings_modality, meetings_location_building=meetings_location_building, meetings_location_room=meetings_location_room, meetings_location_map_uri=meetings_location_map_uri, core_flags=core_flags, syllabus_uri=syllabus_uri)
        print("The response of DefaultApi->section_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->section_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **float**| The starting position of the current page of sections (e.g. For starting at the 17th professor, offset&#x3D;16). | [optional] 
 **section_number** | **str**| The section&#39;s official number | [optional] 
 **academic_session_name** | **str**| The name of the academic session of the section | [optional] 
 **academic_session_start_date** | **str**| The date of classes starting for the section | [optional] 
 **academic_session_end_date** | **str**| The date of classes ending for the section | [optional] 
 **teaching_assistants_first_name** | **str**| The first name of one of the teaching assistants of the section | [optional] 
 **teaching_assistants_last_name** | **str**| The last name of one of the teaching assistants of the section | [optional] 
 **teaching_assistants_role** | **str**| The role of one of the teaching assistants of the section | [optional] 
 **teaching_assistants_email** | **str**| The email of one of the teaching assistants of the section | [optional] 
 **internal_class_number** | **str**| The internal (university) number used to reference this section | [optional] 
 **instruction_mode** | **str**| The instruction modality for this section | [optional] 
 **meetings_start_date** | **str**| The start date of one of the section&#39;s meetings | [optional] 
 **meetings_end_date** | **str**| The end date of one of the section&#39;s meetings | [optional] 
 **meetings_meeting_days** | **str**| One of the days that one of the section&#39;s meetings | [optional] 
 **meetings_start_time** | **str**| The time one of the section&#39;s meetings starts | [optional] 
 **meetings_end_time** | **str**| The time one of the section&#39;s meetings ends | [optional] 
 **meetings_modality** | **str**| The modality of one of the section&#39;s meetings | [optional] 
 **meetings_location_building** | **str**| The building of one of the section&#39;s meetings | [optional] 
 **meetings_location_room** | **str**| The room of one of the section&#39;s meetings | [optional] 
 **meetings_location_map_uri** | **str**| A hyperlink to the UTD room locator of one of the section&#39;s meetings | [optional] 
 **core_flags** | **str**| One of core requirement codes this section fulfills | [optional] 
 **syllabus_uri** | **str**| A link to the syllabus on the web | [optional] 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of sections |  -  |
**400** | A string describing the error |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **swagger**
> swagger(file)

Returns the OpenAPI/swagger spec for the API

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    file = 'file_example' # str | The swagger file to retrieve

    try:
        api_instance.swagger(file)
    except Exception as e:
        print("Exception when calling DefaultApi->swagger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**| The swagger file to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trends_course_section_search**
> SchemaAPIResponseArraySchemaSection trends_course_section_search(course_number, subject_prefix)

"Returns all of the given course's sections. Specialized high-speed convenience endpoint for UTD Trends internal use; limited query flexibility."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    course_number = 'course_number_example' # str | The course's official number
    subject_prefix = 'subject_prefix_example' # str | The course's subject prefix

    try:
        api_response = api_instance.trends_course_section_search(course_number, subject_prefix)
        print("The response of DefaultApi->trends_course_section_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trends_course_section_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_number** | **str**| The course&#39;s official number | 
 **subject_prefix** | **str**| The course&#39;s subject prefix | 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Sections |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trends_professor_section_search**
> SchemaAPIResponseArraySchemaSection trends_professor_section_search(first_name, last_name)

"Returns all of the given professor's sections. Specialized high-speed convenience endpoint for UTD Trends internal use; limited query flexibility."

### Example

* Api Key Authentication (api_key):

```python
import openapi_client
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://api.utdnebula.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    first_name = 'first_name_example' # str | The professor's first name
    last_name = 'last_name_example' # str | The professor's last name

    try:
        api_response = api_instance.trends_professor_section_search(first_name, last_name)
        print("The response of DefaultApi->trends_professor_section_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->trends_professor_section_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **first_name** | **str**| The professor&#39;s first name | 
 **last_name** | **str**| The professor&#39;s last name | 

### Return type

[**SchemaAPIResponseArraySchemaSection**](SchemaAPIResponseArraySchemaSection.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Sections |  -  |
**500** | A string describing the error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

