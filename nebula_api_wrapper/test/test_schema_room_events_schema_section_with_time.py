# coding: utf-8

"""
    nebula-api

    The public Nebula Labs API for access to pertinent UT Dallas data

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.schema_room_events_schema_section_with_time import SchemaRoomEventsSchemaSectionWithTime

class TestSchemaRoomEventsSchemaSectionWithTime(unittest.TestCase):
    """SchemaRoomEventsSchemaSectionWithTime unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaRoomEventsSchemaSectionWithTime:
        """Test SchemaRoomEventsSchemaSectionWithTime
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaRoomEventsSchemaSectionWithTime`
        """
        model = SchemaRoomEventsSchemaSectionWithTime()
        if include_optional:
            return SchemaRoomEventsSchemaSectionWithTime(
                events = [
                    openapi_client.models.schema/section_with_time.schema.SectionWithTime(
                        end_time = '', 
                        section = '', 
                        start_time = '', )
                    ],
                room = ''
            )
        else:
            return SchemaRoomEventsSchemaSectionWithTime(
        )
        """

    def testSchemaRoomEventsSchemaSectionWithTime(self):
        """Test SchemaRoomEventsSchemaSectionWithTime"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
