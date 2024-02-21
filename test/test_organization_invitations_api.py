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
from clerk_client.api.organization_invitations_api import OrganizationInvitationsApi  # noqa: E501
from clerk_client.rest import ApiException


class TestOrganizationInvitationsApi(unittest.TestCase):
    """OrganizationInvitationsApi unit test stubs"""

    def setUp(self):
        self.api = OrganizationInvitationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_organization_invitation(self):
        """Test case for create_organization_invitation

        Create and send an organization invitation  # noqa: E501
        """
        pass

    def test_create_organization_invitation_bulk(self):
        """Test case for create_organization_invitation_bulk

        Bulk create and send organization invitations  # noqa: E501
        """
        pass

    def test_get_organization_invitation(self):
        """Test case for get_organization_invitation

        Retrieve an organization invitation by ID  # noqa: E501
        """
        pass

    def test_list_organization_invitations(self):
        """Test case for list_organization_invitations

        Get a list of organization invitations  # noqa: E501
        """
        pass

    def test_list_pending_organization_invitations(self):
        """Test case for list_pending_organization_invitations

        Get a list of pending organization invitations  # noqa: E501
        """
        pass

    def test_revoke_organization_invitation(self):
        """Test case for revoke_organization_invitation

        Revoke a pending organization invitation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()