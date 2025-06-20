# coding: utf-8

"""
    nebula-api

    The public Nebula Labs API for access to pertinent UT Dallas data

    The version of the OpenAPI document: 1.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.schema_section_number_professors import SchemaSectionNumberProfessors

class TestSchemaSectionNumberProfessors(unittest.TestCase):
    """SchemaSectionNumberProfessors unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SchemaSectionNumberProfessors:
        """Test SchemaSectionNumberProfessors
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SchemaSectionNumberProfessors`
        """
        model = SchemaSectionNumberProfessors()
        if include_optional:
            return SchemaSectionNumberProfessors(
                professors = [
                    openapi_client.models.schema/simple_professor.schema.SimpleProfessor(
                        first_name = '', 
                        last_name = '', )
                    ],
                section_number = ''
            )
        else:
            return SchemaSectionNumberProfessors(
        )
        """

    def testSchemaSectionNumberProfessors(self):
        """Test SchemaSectionNumberProfessors"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
