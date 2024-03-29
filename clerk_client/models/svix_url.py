# coding: utf-8

"""
    Clerk Backend API

    The Clerk REST Backend API, meant to be accessed by backend servers. Please see https://clerk.com/docs for more information.  # noqa: E501

    OpenAPI spec version: v1
    Contact: support@clerk.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class SvixURL(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'svix_url': 'str'
    }

    attribute_map = {
        'svix_url': 'svix_url'
    }

    def __init__(self, svix_url=None):  # noqa: E501
        """SvixURL - a model defined in Swagger"""  # noqa: E501
        self._svix_url = None
        self.discriminator = None
        self.svix_url = svix_url

    @property
    def svix_url(self):
        """Gets the svix_url of this SvixURL.  # noqa: E501


        :return: The svix_url of this SvixURL.  # noqa: E501
        :rtype: str
        """
        return self._svix_url

    @svix_url.setter
    def svix_url(self, svix_url):
        """Sets the svix_url of this SvixURL.


        :param svix_url: The svix_url of this SvixURL.  # noqa: E501
        :type: str
        """
        if svix_url is None:
            raise ValueError("Invalid value for `svix_url`, must not be `None`")  # noqa: E501

        self._svix_url = svix_url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(SvixURL, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SvixURL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
