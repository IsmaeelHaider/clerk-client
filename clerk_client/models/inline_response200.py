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

class InlineResponse200(object):
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
        'object': 'str',
        'jwt': 'str'
    }

    attribute_map = {
        'object': 'object',
        'jwt': 'jwt'
    }

    def __init__(self, object=None, jwt=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._jwt = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if jwt is not None:
            self.jwt = jwt

    @property
    def object(self):
        """Gets the object of this InlineResponse200.  # noqa: E501


        :return: The object of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this InlineResponse200.


        :param object: The object of this InlineResponse200.  # noqa: E501
        :type: str
        """
        allowed_values = ["token"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def jwt(self):
        """Gets the jwt of this InlineResponse200.  # noqa: E501


        :return: The jwt of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._jwt

    @jwt.setter
    def jwt(self, jwt):
        """Sets the jwt of this InlineResponse200.


        :param jwt: The jwt of this InlineResponse200.  # noqa: E501
        :type: str
        """

        self._jwt = jwt

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
