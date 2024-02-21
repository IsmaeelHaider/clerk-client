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
from clerk_client.api.domains_api import DomainsApi  # noqa: E501
from clerk_client.rest import ApiException


class TestDomainsApi(unittest.TestCase):
    """DomainsApi unit test stubs"""

    def setUp(self):
        self.api = DomainsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_domain(self):
        """Test case for add_domain

        Add a domain  # noqa: E501
        """
        pass

    def test_delete_domain(self):
        """Test case for delete_domain

        Delete a satellite domain  # noqa: E501
        """
        pass

    def test_list_domains(self):
        """Test case for list_domains

        List all instance domains  # noqa: E501
        """
        pass

    def test_update_domain(self):
        """Test case for update_domain

        Update a domain  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()