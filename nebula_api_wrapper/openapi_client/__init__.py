# coding: utf-8

# flake8: noqa

"""
    nebula-api

    The public Nebula Labs API for access to pertinent UT Dallas data

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.default_api import DefaultApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.schema_api_response_array_int import SchemaAPIResponseArrayInt
from openapi_client.models.schema_api_response_array_schema_autocomplete import SchemaAPIResponseArraySchemaAutocomplete
from openapi_client.models.schema_api_response_array_schema_building_rooms import SchemaAPIResponseArraySchemaBuildingRooms
from openapi_client.models.schema_api_response_array_schema_course import SchemaAPIResponseArraySchemaCourse
from openapi_client.models.schema_api_response_array_schema_grade_data import SchemaAPIResponseArraySchemaGradeData
from openapi_client.models.schema_api_response_array_schema_professor import SchemaAPIResponseArraySchemaProfessor
from openapi_client.models.schema_api_response_array_schema_section import SchemaAPIResponseArraySchemaSection
from openapi_client.models.schema_api_response_array_schema_typed_grade_data import SchemaAPIResponseArraySchemaTypedGradeData
from openapi_client.models.schema_api_response_int import SchemaAPIResponseInt
from openapi_client.models.schema_api_response_schema_bucket_info import SchemaAPIResponseSchemaBucketInfo
from openapi_client.models.schema_api_response_schema_course import SchemaAPIResponseSchemaCourse
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_astra_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaAstraEvent
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_mazevo_event import SchemaAPIResponseSchemaMultiBuildingEventsSchemaMazevoEvent
from openapi_client.models.schema_api_response_schema_multi_building_events_schema_section_with_time import SchemaAPIResponseSchemaMultiBuildingEventsSchemaSectionWithTime
from openapi_client.models.schema_api_response_schema_object_info import SchemaAPIResponseSchemaObjectInfo
from openapi_client.models.schema_api_response_schema_professor import SchemaAPIResponseSchemaProfessor
from openapi_client.models.schema_api_response_schema_section import SchemaAPIResponseSchemaSection
from openapi_client.models.schema_api_response_schema_single_building_events_schema_section_with_time import SchemaAPIResponseSchemaSingleBuildingEventsSchemaSectionWithTime
from openapi_client.models.schema_api_response_string import SchemaAPIResponseString
from openapi_client.models.schema_academic_session import SchemaAcademicSession
from openapi_client.models.schema_academic_session_sections import SchemaAcademicSessionSections
from openapi_client.models.schema_assistant import SchemaAssistant
from openapi_client.models.schema_astra_event import SchemaAstraEvent
from openapi_client.models.schema_autocomplete import SchemaAutocomplete
from openapi_client.models.schema_bucket_info import SchemaBucketInfo
from openapi_client.models.schema_building_rooms import SchemaBuildingRooms
from openapi_client.models.schema_collection_requirement import SchemaCollectionRequirement
from openapi_client.models.schema_course import SchemaCourse
from openapi_client.models.schema_course_number_academic_sessions import SchemaCourseNumberAcademicSessions
from openapi_client.models.schema_grade_data import SchemaGradeData
from openapi_client.models.schema_location import SchemaLocation
from openapi_client.models.schema_mazevo_event import SchemaMazevoEvent
from openapi_client.models.schema_meeting import SchemaMeeting
from openapi_client.models.schema_multi_building_events_schema_astra_event import SchemaMultiBuildingEventsSchemaAstraEvent
from openapi_client.models.schema_multi_building_events_schema_mazevo_event import SchemaMultiBuildingEventsSchemaMazevoEvent
from openapi_client.models.schema_multi_building_events_schema_section_with_time import SchemaMultiBuildingEventsSchemaSectionWithTime
from openapi_client.models.schema_object_info import SchemaObjectInfo
from openapi_client.models.schema_professor import SchemaProfessor
from openapi_client.models.schema_room_events_schema_astra_event import SchemaRoomEventsSchemaAstraEvent
from openapi_client.models.schema_room_events_schema_mazevo_event import SchemaRoomEventsSchemaMazevoEvent
from openapi_client.models.schema_room_events_schema_section_with_time import SchemaRoomEventsSchemaSectionWithTime
from openapi_client.models.schema_section import SchemaSection
from openapi_client.models.schema_section_number_professors import SchemaSectionNumberProfessors
from openapi_client.models.schema_section_with_time import SchemaSectionWithTime
from openapi_client.models.schema_simple_academic_session import SchemaSimpleAcademicSession
from openapi_client.models.schema_simple_professor import SchemaSimpleProfessor
from openapi_client.models.schema_single_building_events_schema_astra_event import SchemaSingleBuildingEventsSchemaAstraEvent
from openapi_client.models.schema_single_building_events_schema_mazevo_event import SchemaSingleBuildingEventsSchemaMazevoEvent
from openapi_client.models.schema_single_building_events_schema_section_with_time import SchemaSingleBuildingEventsSchemaSectionWithTime
from openapi_client.models.schema_typed_grade_data import SchemaTypedGradeData
from openapi_client.models.schema_typed_grade_data_data_inner import SchemaTypedGradeDataDataInner
