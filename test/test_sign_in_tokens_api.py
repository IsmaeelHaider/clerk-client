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
from clerk_client.api.sign_in_tokens_api import SignInTokensApi  # noqa: E501
from clerk_client.rest import ApiException


class TestSignInTokensApi(unittest.TestCase):
    """SignInTokensApi unit test stubs"""

    def setUp(self):
        self.api = SignInTokensApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_sign_in_token(self):
        """Test case for create_sign_in_token

        Create sign-in token  # noqa: E501
        """
        pass

    def test_revoke_sign_in_token(self):
        """Test case for revoke_sign_in_token

        Revoke the given sign-in token  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()