# coding: utf-8

"""
    Clerk Backend API

    The Clerk REST Backend API, meant to be accessed by backend servers. Please see https://clerk.com/docs for more information.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@clerk.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import clerk_client
from clerk_client.api.email__sms_templates_api import EmailSMSTemplatesApi  # noqa: E501
from clerk_client.rest import ApiException


class TestEmailSMSTemplatesApi(unittest.TestCase):
    """EmailSMSTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = EmailSMSTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_template(self):
        """Test case for get_template

        Retrieve a template  # noqa: E501
        """
        pass

    def test_get_template_list(self):
        """Test case for get_template_list

        List all templates  # noqa: E501
        """
        pass

    def test_preview_template(self):
        """Test case for preview_template

        Preview changes to a template  # noqa: E501
        """
        pass

    def test_revert_template(self):
        """Test case for revert_template

        Revert a template  # noqa: E501
        """
        pass

    def test_toggle_template_delivery(self):
        """Test case for toggle_template_delivery

        Toggle the delivery by Clerk for a template of a given type and slug  # noqa: E501
        """
        pass

    def test_upsert_template(self):
        """Test case for upsert_template

        Update a template for a given type and slug  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()