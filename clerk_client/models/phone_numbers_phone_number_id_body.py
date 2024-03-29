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

class PhoneNumbersPhoneNumberIdBody(object):
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
        'verified': 'bool',
        'primary': 'bool',
        'reserved_for_second_factor': 'bool'
    }

    attribute_map = {
        'verified': 'verified',
        'primary': 'primary',
        'reserved_for_second_factor': 'reserved_for_second_factor'
    }

    def __init__(self, verified=None, primary=None, reserved_for_second_factor=None):  # noqa: E501
        """PhoneNumbersPhoneNumberIdBody - a model defined in Swagger"""  # noqa: E501
        self._verified = None
        self._primary = None
        self._reserved_for_second_factor = None
        self.discriminator = None
        if verified is not None:
            self.verified = verified
        if primary is not None:
            self.primary = primary
        if reserved_for_second_factor is not None:
            self.reserved_for_second_factor = reserved_for_second_factor

    @property
    def verified(self):
        """Gets the verified of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501

        The phone number will be marked as verified.  # noqa: E501

        :return: The verified of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this PhoneNumbersPhoneNumberIdBody.

        The phone number will be marked as verified.  # noqa: E501

        :param verified: The verified of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :type: bool
        """

        self._verified = verified

    @property
    def primary(self):
        """Gets the primary of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501

        Set this phone number as the primary phone number for the user.  # noqa: E501

        :return: The primary of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PhoneNumbersPhoneNumberIdBody.

        Set this phone number as the primary phone number for the user.  # noqa: E501

        :param primary: The primary of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :type: bool
        """

        self._primary = primary

    @property
    def reserved_for_second_factor(self):
        """Gets the reserved_for_second_factor of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501

        Set this phone number as reserved for multi-factor authentication. The phone number must also be verified. If there are no other reserved second factors, the phone number will be set as the default second factor.  # noqa: E501

        :return: The reserved_for_second_factor of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._reserved_for_second_factor

    @reserved_for_second_factor.setter
    def reserved_for_second_factor(self, reserved_for_second_factor):
        """Sets the reserved_for_second_factor of this PhoneNumbersPhoneNumberIdBody.

        Set this phone number as reserved for multi-factor authentication. The phone number must also be verified. If there are no other reserved second factors, the phone number will be set as the default second factor.  # noqa: E501

        :param reserved_for_second_factor: The reserved_for_second_factor of this PhoneNumbersPhoneNumberIdBody.  # noqa: E501
        :type: bool
        """

        self._reserved_for_second_factor = reserved_for_second_factor

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
        if issubclass(PhoneNumbersPhoneNumberIdBody, dict):
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
        if not isinstance(other, PhoneNumbersPhoneNumberIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
