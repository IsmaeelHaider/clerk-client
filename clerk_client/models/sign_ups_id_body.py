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

class SignUpsIdBody(object):
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
        'custom_action': 'bool',
        'external_id': 'str'
    }

    attribute_map = {
        'custom_action': 'custom_action',
        'external_id': 'external_id'
    }

    def __init__(self, custom_action=None, external_id=None):  # noqa: E501
        """SignUpsIdBody - a model defined in Swagger"""  # noqa: E501
        self._custom_action = None
        self._external_id = None
        self.discriminator = None
        if custom_action is not None:
            self.custom_action = custom_action
        if external_id is not None:
            self.external_id = external_id

    @property
    def custom_action(self):
        """Gets the custom_action of this SignUpsIdBody.  # noqa: E501

        Specifies whether a custom action has run for this sign-up attempt. This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user. After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting `custom_action` to `true`.  # noqa: E501

        :return: The custom_action of this SignUpsIdBody.  # noqa: E501
        :rtype: bool
        """
        return self._custom_action

    @custom_action.setter
    def custom_action(self, custom_action):
        """Sets the custom_action of this SignUpsIdBody.

        Specifies whether a custom action has run for this sign-up attempt. This is important when your instance has been configured to require a custom action to run before converting a sign-up into a user. After executing any external business logic you deem necessary, you can mark the sign-up as ready-to-convert by setting `custom_action` to `true`.  # noqa: E501

        :param custom_action: The custom_action of this SignUpsIdBody.  # noqa: E501
        :type: bool
        """

        self._custom_action = custom_action

    @property
    def external_id(self):
        """Gets the external_id of this SignUpsIdBody.  # noqa: E501

        The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution. This will be copied to the resulting user when the sign-up is completed.  # noqa: E501

        :return: The external_id of this SignUpsIdBody.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SignUpsIdBody.

        The ID of the guest attempting to sign up as used in your external systems or your previous authentication solution. This will be copied to the resulting user when the sign-up is completed.  # noqa: E501

        :param external_id: The external_id of this SignUpsIdBody.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

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
        if issubclass(SignUpsIdBody, dict):
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
        if not isinstance(other, SignUpsIdBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
