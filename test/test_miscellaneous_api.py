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
from clerk_client.api.miscellaneous_api import MiscellaneousApi  # noqa: E501
from clerk_client.rest import ApiException


class TestMiscellaneousApi(unittest.TestCase):
    """MiscellaneousApi unit test stubs"""

    def setUp(self):
        self.api = MiscellaneousApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_public_interstitial(self):
        """Test case for get_public_interstitial

        Returns the markup for the interstitial page  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()