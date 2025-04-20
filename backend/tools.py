from typing import Optional, Union

import openapi_client
from openapi_client import SchemaCourse, SchemaProfessor, SchemaSection

from lib import configuration

api_client = openapi_client.ApiClient(configuration)
api_instance = openapi_client.DefaultApi(api_client)



def search_courses(
        offset: Optional[Union[int, float]] = None,  # Simplified type, allows int or float, compatible with AllowedType
        course_number: Optional[str] = None,  # Compatible with AllowedType
        subject_prefix: Optional[str] = None,  # Compatible with AllowedType
        title: Optional[str] = None,  # Compatible with AllowedType
        description: Optional[str] = None,  # Compatible with AllowedType
        school: Optional[str] = None,  # Compatible with AllowedType
        credit_hours: Optional[str] = None,  # Compatible with AllowedType
        class_level: Optional[str] = None,  # Compatible with AllowedType
        activity_type: Optional[str] = None,  # Compatible with AllowedType
        grading: Optional[str] = None,  # Compatible with AllowedType
        internal_course_number: Optional[str] = None,  # Compatible with AllowedType
        lecture_contact_hours: Optional[str] = None,  # Compatible with AllowedType
        offering_frequency: Optional[str] = None,  # Compatible with AllowedType
        # The technical parameters (_request_timeout, _request_auth, etc.) are omitted
        # from this simplified wrapper function's signature.
) -> list[SchemaCourse]:
    """Searches for UT Dallas courses based on various criteria.

    Retrieves a paginated list of courses matching the provided query parameters.

    Args:
        offset: The starting position (index) for pagination. For example, use 0 for the first course, 16 for the 17th course, etc. Can be an integer or float.
        course_number: The official course number (e.g., "101").
        subject_prefix: The subject prefix (e.g., "CS", "EE").
        title: The course title or a part of it.
        description: The course description or a part of it.
        school: The school offering the course.
        credit_hours: The number of credit hours (e.g., "3").
        class_level: The educational level associated with the course (e.g., "Undergraduate", "Graduate").
        activity_type: The type of class activity (e.g., "Lecture", "Lab").
        grading: The grading status of the course (e.g., "Pass/Fail", "Graded").
        internal_course_number: The internal university number used to reference the course.
        lecture_contact_hours: The weekly contact hours spent in lecture for the course.
        offering_frequency: The frequency at which the course is offered (e.g., "Fall Semester", "Annually").

    Returns:
        A list of courses matching the criteria.

    Raises:
        Any exceptions raised by the underlying API client during the request will be propagated.
    """
    # Call the original course_search method, passing through the simplified parameters.
    # The technical parameters (_request_timeout, _request_auth, etc.) will
    # take their default values as defined in the original course_search method.
    return api_instance.course_search(
        offset=offset,
        course_number=course_number,
        subject_prefix=subject_prefix,
        title=title,
        description=description,
        school=school,
        credit_hours=credit_hours,
        class_level=class_level,
        activity_type=activity_type,
        grading=grading,
        internal_course_number=internal_course_number,
        lecture_contact_hours=lecture_contact_hours,
        offering_frequency=offering_frequency,
    ).data


def search_professors(
        offset: Optional[Union[int, float]] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        titles: Optional[str] = None,
        email: Optional[str] = None,
        phone_number: Optional[str] = None,
        office_building: Optional[str] = None,
        office_room: Optional[str] = None,
        office_map_uri: Optional[str] = None,
        profile_uri: Optional[str] = None,
        image_uri: Optional[str] = None,
        office_hours_start_date: Optional[str] = None,
        office_hours_end_date: Optional[str] = None,
        office_hours_meeting_days: Optional[str] = None,
        office_hours_start_time: Optional[str] = None,
        office_hours_end_time: Optional[str] = None,
        office_hours_modality: Optional[str] = None,
        office_hours_location_building: Optional[str] = None,
        office_hours_location_room: Optional[str] = None,
        office_hours_location_map_uri: Optional[str] = None,
) -> list[SchemaProfessor]:
    """Searches for professors based on various criteria.

    Retrieves a paginated list of professors matching the provided query parameters.
    This function simplifies the calling convention by hiding technical API details.

    Args:
        offset: The starting position (index) for pagination. For example, use 0 for the first professor, 16 for the 17th professor, etc. Can be an integer or float.
        first_name: The professor's first name.
        last_name: The professor's last name.
        titles: One of the professor's titles.
        email: The professor's email address.
        phone_number: The professor's phone number.
        office_building: The building of the professor's office location.
        office_room: The room number of the professor's office location.
        office_map_uri: A hyperlink to the UTD room locator for the professor's office.
        profile_uri: A hyperlink to the professor's official university profile.
        image_uri: A link to the image used for the professor on their official university profile.
        office_hours_start_date: The start date of one of the professor's office hours meetings.
        office_hours_end_date: The end date of one of the professor's office hours meetings.
        office_hours_meeting_days: One of the days for one of the professor's office hours meetings.
        office_hours_start_time: The start time for one of the professor's office hours meetings.
        office_hours_end_time: The end time for one of the professor's office hours meetings.
        office_hours_modality: The modality of one of the professor's office hours meetings.
        office_hours_location_building: The building for one of the professor's office hours meetings.
        office_hours_location_room: The room number for one of the professor's office hours meetings.
        office_hours_location_map_uri: A hyperlink to the UTD room locator for one of the professor's office hours meetings.

    Returns:
        A list of professors matching the criteria.

    Raises:
        Any exceptions raised by the underlying API client during the request will be propagated.
    """
    # Call the original professor_search method, passing through the simplified parameters.
    # The technical parameters (_request_timeout, _request_auth, etc.) will
    # take their default values as defined in the original professor_search method.
    return api_instance.professor_search(
        offset=offset,
        first_name=first_name,
        last_name=last_name,
        titles=titles,
        email=email,
        phone_number=phone_number,
        office_building=office_building,
        office_room=office_room,
        office_map_uri=office_map_uri,
        profile_uri=profile_uri,
        image_uri=image_uri,
        office_hours_start_date=office_hours_start_date,
        office_hours_end_date=office_hours_end_date,
        office_hours_meeting_days=office_hours_meeting_days,
        office_hours_start_time=office_hours_start_time,
        office_hours_end_time=office_hours_end_time,
        office_hours_modality=office_hours_modality,
        office_hours_location_building=office_hours_location_building,
        office_hours_location_room=office_hours_location_room,
        office_hours_location_map_uri=office_hours_location_map_uri,
    ).data


def get_professor_sections(
        professor_id: str,
) -> list[SchemaSection]:
    """Retrieves all sections taught by a specific professor.

    Fetches a list of course sections associated with the professor identified by the provided ID.
    This function simplifies the calling convention by hiding technical API details.

    Args:
        professor_id: The unique identifier (ID) of the professor whose sections are to be retrieved.

    Returns:
        A list of sections taught by the professor.

    Raises:
        Any exceptions raised by the underlying API client during the request will be propagated.
    """
    return api_instance.professor_section_by_id(
        id=professor_id,
    ).data


def search_sections(
        offset: Optional[Union[int, float]] = None,
        section_number: Optional[str] = None,
        academic_session_name: Optional[str] = None,
        academic_session_start_date: Optional[str] = None,
        academic_session_end_date: Optional[str] = None,
        teaching_assistants_first_name: Optional[str] = None,
        teaching_assistants_last_name: Optional[str] = None,
        teaching_assistants_role: Optional[str] = None,
        teaching_assistants_email: Optional[str] = None,
        internal_class_number: Optional[str] = None,
        instruction_mode: Optional[str] = None,
        meetings_start_date: Optional[str] = None,
        meetings_end_date: Optional[str] = None,
        meetings_meeting_days: Optional[str] = None,
        meetings_start_time: Optional[str] = None,
        meetings_end_time: Optional[str] = None,
        meetings_modality: Optional[str] = None,
        meetings_location_building: Optional[str] = None,
        meetings_location_room: Optional[str] = None,
        meetings_location_map_uri: Optional[str] = None,
        core_flags: Optional[str] = None,
        syllabus_uri: Optional[str] = None,
) -> list[SchemaSection]:
    """Searches for course sections based on various criteria.

    Retrieves a paginated list of sections matching the provided query parameters.
    This function simplifies the calling convention by hiding technical API details.

    Args:
        offset: The starting position (index) for pagination. For example, use 0 for the first section, 16 for the 17th section, etc. Can be an integer or float.
        section_number: The section's official number.
        academic_session_name: The name of the academic session the section belongs to.
        academic_session_start_date: The start date of the academic session classes for this section.
        academic_session_end_date: The end date of the academic session classes for this section.
        teaching_assistants_first_name: The first name of one of the section's teaching assistants.
        teaching_assistants_last_name: The last name of one of the section's teaching assistants.
        teaching_assistants_role: The role of one of the section's teaching assistants.
        teaching_assistants_email: The email address of one of the section's teaching assistants.
        internal_class_number: The internal university number used to reference this section.
        instruction_mode: The instruction modality for this section (e.g., "Online", "In-Person").
        meetings_start_date: The start date of one of the section's scheduled meetings.
        meetings_end_date: The end date of one of the section's scheduled meetings.
        meetings_meeting_days: One of the days on which a section meeting occurs.
        meetings_start_time: The start time for one of the section's scheduled meetings.
        meetings_end_time: The end time for one of the section's scheduled meetings.
        meetings_modality: The modality of one of the section's scheduled meetings.
        meetings_location_building: The building where one of the section's meetings takes place.
        meetings_location_room: The room number where one of the section's meetings takes place.
        meetings_location_map_uri: A hyperlink to the UTD room locator for one of the section's meeting locations.
        core_flags: One of the core requirement codes this section fulfills.
        syllabus_uri: A web link to the section's syllabus.

    Returns:
        A list of sections matching the criteria.

    Raises:
        Any exceptions raised by the underlying API client during the request will be propagated.
    """
    return api_instance.section_search(
        offset=offset,
        section_number=section_number,
        academic_session_name=academic_session_name,
        academic_session_start_date=academic_session_start_date,
        academic_session_end_date=academic_session_end_date,
        teaching_assistants_first_name=teaching_assistants_first_name,
        teaching_assistants_last_name=teaching_assistants_last_name,
        teaching_assistants_role=teaching_assistants_role,
        teaching_assistants_email=teaching_assistants_email,
        internal_class_number=internal_class_number,
        instruction_mode=instruction_mode,
        meetings_start_date=meetings_start_date,
        meetings_end_date=meetings_end_date,
        meetings_meeting_days=meetings_meeting_days,
        meetings_start_time=meetings_start_time,
        meetings_end_time=meetings_end_time,
        meetings_modality=meetings_modality,
        meetings_location_building=meetings_location_building,
        meetings_location_room=meetings_location_room,
        meetings_location_map_uri=meetings_location_map_uri,
        core_flags=core_flags,
        syllabus_uri=syllabus_uri,
    ).data


def get_section_by_id(
        section_id: str,
) -> SchemaSection:
    """Retrieves a specific course section by its ID.

    Fetches the details of a single course section identified by the provided ID.
    This function simplifies the calling convention by hiding technical API details.

    Args:
        section_id: The unique identifier (ID) of the section to retrieve.

    Returns:
        A response object containing the details of the requested section.
        The exact structure is determined by SchemaAPIResponseSchemaSection.

    Raises:
        Any exceptions raised by the underlying API client during the request will be propagated.
        This may include errors if a section with the given ID is not found.
    """
    return api_instance.section_by_id(
        id=section_id,
    ).data

def get_course_by_id(
        course_id: str,
    ) -> SchemaCourse:
        """Retrieves a specific course by its ID.

        Fetches the details of a single course identified by the provided ID.
        This function simplifies the calling convention by hiding technical API details.

        Args:
            course_id: The unique identifier (ID) of the course to retrieve.

        Returns:
            A response object containing the details of the requested course.
            The exact structure is determined by SchemaAPIResponseSchemaCourse.

        Raises:
            Any exceptions raised by the underlying API client during the request will be propagated.
            This may include errors if a course with the given ID is not found.
        """
        return api_instance.course_by_id(
            id=course_id,
        ).data

def get_professor_grades(
        professor_id: str,
    ) -> dict[str, int]:
        """Retrieves the overall grade distribution for a specific professor.

        Fetches the aggregate grade data (e.g., distribution counts for A, B, C, etc.)
        for the professor identified by the provided ID across all their courses/sections.
        This function simplifies the calling convention by hiding technical API details.

        Args:
            professor_id: The unique identifier (ID) of the professor for whom to retrieve grade data.

        Returns:
            A response object containing the overall grade distribution, typically as an array of integers
            or a similar structure representing counts for different grade categories.
            The exact structure is determined by SchemaAPIResponseArrayInt.

        Raises:
            Any exceptions raised by the underlying API client during the request will be propagated.
            This may include errors if grade data for the given professor ID is not found.
        """
        return dict(zip(('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F', 'W'), api_instance.grades_by_professor_id(
            id=professor_id,
        ).data))