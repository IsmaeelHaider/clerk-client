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
from clerk_client.api.actor_tokens_api import ActorTokensApi  # noqa: E501
from clerk_client.rest import ApiException


class TestActorTokensApi(unittest.TestCase):
    """ActorTokensApi unit test stubs"""

    def setUp(self):
        self.api = ActorTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_actor_token(self):
        """Test case for create_actor_token

        Create actor token  # noqa: E501
        """
        pass

    def test_revoke_actor_token(self):
        """Test case for revoke_actor_token

        Revoke actor token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
