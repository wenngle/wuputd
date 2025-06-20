# openapi-client

The public Nebula Labs API for access to pertinent UT Dallas data

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.1.0
- Package version: 1.0.0
- Generator version: 7.12.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.8+

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```

(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:

```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```

(or `sudo python setup.py install` to install the package for all users)

Then import the package:

```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.utdnebula.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host="http://api.utdnebula.com"
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
    var_date = 'var_date_example'  # str | date (ISO format) to retrieve astra events

    try:
        api_response = api_instance.astra_events(var_date)
        print("The response of DefaultApi->astra_events:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->astra_events: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://api.utdnebula.com*

 Class        | Method                                                                                    | HTTP request                            | Description 
--------------|-------------------------------------------------------------------------------------------|-----------------------------------------|-------------
 *DefaultApi* | [**astra_events**](docs/DefaultApi.md#astra_events)                                       | **GET** /astra/{date}                   |
 *DefaultApi* | [**autocomplete_dag**](docs/DefaultApi.md#autocomplete_dag)                               | **GET** /autocomplete/dag               |
 *DefaultApi* | [**bucket_info**](docs/DefaultApi.md#bucket_info)                                         | **GET** /storage/{bucket}               |
 *DefaultApi* | [**course_all**](docs/DefaultApi.md#course_all)                                           | **GET** /course/all                     |
 *DefaultApi* | [**course_by_id**](docs/DefaultApi.md#course_by_id)                                       | **GET** /course/{id}                    |
 *DefaultApi* | [**course_search**](docs/DefaultApi.md#course_search)                                     | **GET** /course                         |
 *DefaultApi* | [**course_section_by_id**](docs/DefaultApi.md#course_section_by_id)                       | **GET** /course/{id}/sections           |
 *DefaultApi* | [**course_section_search**](docs/DefaultApi.md#course_section_search)                     | **GET** /course/sections                |
 *DefaultApi* | [**delete_bucket**](docs/DefaultApi.md#delete_bucket)                                     | **DELETE** /storage/{bucket}            |
 *DefaultApi* | [**delete_object**](docs/DefaultApi.md#delete_object)                                     | **DELETE** /storage/{bucket}/{objectID} |
 *DefaultApi* | [**events**](docs/DefaultApi.md#events)                                                   | **GET** /events/{date}                  |
 *DefaultApi* | [**events_by_building**](docs/DefaultApi.md#events_by_building)                           | **GET** /events/{date}/{building}       |
 *DefaultApi* | [**grade_aggregation_by_semester**](docs/DefaultApi.md#grade_aggregation_by_semester)     | **GET** /grades/semester                |
 *DefaultApi* | [**grade_aggregation_overall**](docs/DefaultApi.md#grade_aggregation_overall)             | **GET** /grades/overall                 |
 *DefaultApi* | [**grade_aggregation_section_type**](docs/DefaultApi.md#grade_aggregation_section_type)   | **GET** /grades/semester/sectionType    |
 *DefaultApi* | [**grades_by_course_id**](docs/DefaultApi.md#grades_by_course_id)                         | **GET** /course/{id}/grades             |
 *DefaultApi* | [**grades_by_professor_id**](docs/DefaultApi.md#grades_by_professor_id)                   | **GET** /professor/{id}/grades          |
 *DefaultApi* | [**grades_by_section_id**](docs/DefaultApi.md#grades_by_section_id)                       | **GET** /section/{id}/grades            |
 *DefaultApi* | [**mazevo_events**](docs/DefaultApi.md#mazevo_events)                                     | **GET** /mazevo/{date}                  |
 *DefaultApi* | [**object_info**](docs/DefaultApi.md#object_info)                                         | **GET** /storage/{bucket}/{objectID}    |
 *DefaultApi* | [**post_object**](docs/DefaultApi.md#post_object)                                         | **POST** /storage/{bucket}/{objectID}   |
 *DefaultApi* | [**professor_all**](docs/DefaultApi.md#professor_all)                                     | **GET** /professor/all                  |
 *DefaultApi* | [**professor_by_id**](docs/DefaultApi.md#professor_by_id)                                 | **GET** /professor/{id}                 |
 *DefaultApi* | [**professor_course_by_id**](docs/DefaultApi.md#professor_course_by_id)                   | **GET** /professor/{id}/courses         |
 *DefaultApi* | [**professor_course_search**](docs/DefaultApi.md#professor_course_search)                 | **GET** /professor/courses              |
 *DefaultApi* | [**professor_search**](docs/DefaultApi.md#professor_search)                               | **GET** /professor                      |
 *DefaultApi* | [**professor_section_by_id**](docs/DefaultApi.md#professor_section_by_id)                 | **GET** /professor/{id}/sections        |
 *DefaultApi* | [**professor_section_search**](docs/DefaultApi.md#professor_section_search)               | **GET** /professor/sections             |
 *DefaultApi* | [**rooms**](docs/DefaultApi.md#rooms)                                                     | **GET** /rooms                          |
 *DefaultApi* | [**section_by_id**](docs/DefaultApi.md#section_by_id)                                     | **GET** /section/{id}                   |
 *DefaultApi* | [**section_search**](docs/DefaultApi.md#section_search)                                   | **GET** /section                        |
 *DefaultApi* | [**swagger**](docs/DefaultApi.md#swagger)                                                 | **GET** /swagger/{file}                 |
 *DefaultApi* | [**trends_course_section_search**](docs/DefaultApi.md#trends_course_section_search)       | **GET** /course/sections/trends         |
 *DefaultApi* | [**trends_professor_section_search**](docs/DefaultApi.md#trends_professor_section_search) | **GET** /professor/sections/trends      |

## Documentation For Models

- [SchemaAPIResponseArrayInt](docs/SchemaAPIResponseArrayInt.md)
- [SchemaAPIResponseArraySchemaAutocomplete](docs/SchemaAPIResponseArraySchemaAutocomplete.md)
- [SchemaAPIResponseArraySchemaBuildingRooms](docs/SchemaAPIResponseArraySchemaBuildingRooms.md)
- [SchemaAPIResponseArraySchemaCourse](docs/SchemaAPIResponseArraySchemaCourse.md)
- [SchemaAPIResponseArraySchemaGradeData](docs/SchemaAPIResponseArraySchemaGradeData.md)
- [SchemaAPIResponseArraySchemaProfessor](docs/SchemaAPIResponseArraySchemaProfessor.md)
- [SchemaAPIResponseArraySchemaSection](docs/SchemaAPIResponseArraySchemaSection.md)
- [SchemaAPIResponseArraySchemaTypedGradeData](docs/SchemaAPIResponseArraySchemaTypedGradeData.md)
- [SchemaAPIResponseInt](docs/SchemaAPIResponseInt.md)
- [SchemaAPIResponseSchemaBucketInfo](docs/SchemaAPIResponseSchemaBucketInfo.md)
- [SchemaAPIResponseSchemaCourse](docs/SchemaAPIResponseSchemaCourse.md)
- [SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent](docs/SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent.md)
- [SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent](docs/SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent.md)
- [SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime](docs/SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime.md)
- [SchemaAPIResponseSchemaObjectInfo](docs/SchemaAPIResponseSchemaObjectInfo.md)
- [SchemaAPIResponseSchemaProfessor](docs/SchemaAPIResponseSchemaProfessor.md)
- [SchemaAPIResponseSchemaSection](docs/SchemaAPIResponseSchemaSection.md)
- [SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime](docs/SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime.md)
- [SchemaAPIResponseString](docs/SchemaAPIResponseString.md)
- [SchemaAcademicSession](docs/SchemaAcademicSession.md)
- [SchemaAcademicSessionSections](docs/SchemaAcademicSessionSections.md)
- [SchemaAssistant](docs/SchemaAssistant.md)
- [SchemaAstraEvent](docs/SchemaAstraEvent.md)
- [SchemaAutocomplete](docs/SchemaAutocomplete.md)
- [SchemaBucketInfo](docs/SchemaBucketInfo.md)
- [SchemaBuildingRooms](docs/SchemaBuildingRooms.md)
- [SchemaCollectionRequirement](docs/SchemaCollectionRequirement.md)
- [SchemaCourse](docs/SchemaCourse.md)
- [SchemaCourseNumberAcademicSessions](docs/SchemaCourseNumberAcademicSessions.md)
- [SchemaGradeData](docs/SchemaGradeData.md)
- [SchemaLocation](docs/SchemaLocation.md)
- [SchemaMazevoEvent](docs/SchemaMazevoEvent.md)
- [SchemaMeeting](docs/SchemaMeeting.md)
- [SchemaMultiBuildingEventsSchemaAstraEvent](docs/SchemaMultiBuildingEventsSchemaAstraEvent.md)
- [SchemaMultiBuildingEventsSchemaMazevoEvent](docs/SchemaMultiBuildingEventsSchemaMazevoEvent.md)
- [SchemaMultiBuildingEventsSchemaSectionWithTime](docs/SchemaMultiBuildingEventsSchemaSectionWithTime.md)
- [SchemaObjectInfo](docs/SchemaObjectInfo.md)
- [SchemaProfessor](docs/SchemaProfessor.md)
- [SchemaRoomEventsSchemaAstraEvent](docs/SchemaRoomEventsSchemaAstraEvent.md)
- [SchemaRoomEventsSchemaMazevoEvent](docs/SchemaRoomEventsSchemaMazevoEvent.md)
- [SchemaRoomEventsSchemaSectionWithTime](docs/SchemaRoomEventsSchemaSectionWithTime.md)
- [SchemaSection](docs/SchemaSection.md)
- [SchemaSectionNumberProfessors](docs/SchemaSectionNumberProfessors.md)
- [SchemaSectionWithTime](docs/SchemaSectionWithTime.md)
- [SchemaSimpleAcademicSession](docs/SchemaSimpleAcademicSession.md)
- [SchemaSimpleProfessor](docs/SchemaSimpleProfessor.md)
- [SchemaSingleBuildingEventsSchemaAstraEvent](docs/SchemaSingleBuildingEventsSchemaAstraEvent.md)
- [SchemaSingleBuildingEventsSchemaMazevoEvent](docs/SchemaSingleBuildingEventsSchemaMazevoEvent.md)
- [SchemaSingleBuildingEventsSchemaSectionWithTime](docs/SchemaSingleBuildingEventsSchemaSectionWithTime.md)
- [SchemaTypedGradeData](docs/SchemaTypedGradeData.md)
- [SchemaTypedGradeDataDataInner](docs/SchemaTypedGradeDataDataInner.md)

<a id="documentation-for-authorization"></a>

## Documentation For Authorization

Authentication schemes defined for the API:
<a id="api_key"></a>

### api_key

- **Type**: API key
- **API key parameter name**: x-api-key
- **Location**: HTTP header

## Author




