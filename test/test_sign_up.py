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
from clerk_client.models.sign_up import SignUp  # noqa: E501
from clerk_client.rest import ApiException


class TestSignUp(unittest.TestCase):
    """SignUp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSignUp(self):
        """Test SignUp"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.sign_up.SignUp()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
