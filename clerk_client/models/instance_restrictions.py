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

class InstanceRestrictions(object):
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
        'allowlist': 'bool',
        'blocklist': 'bool',
        'block_email_subaddresses': 'bool'
    }

    attribute_map = {
        'object': 'object',
        'allowlist': 'allowlist',
        'blocklist': 'blocklist',
        'block_email_subaddresses': 'block_email_subaddresses'
    }

    def __init__(self, object=None, allowlist=None, blocklist=None, block_email_subaddresses=None):  # noqa: E501
        """InstanceRestrictions - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._allowlist = None
        self._blocklist = None
        self._block_email_subaddresses = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if allowlist is not None:
            self.allowlist = allowlist
        if blocklist is not None:
            self.blocklist = blocklist
        if block_email_subaddresses is not None:
            self.block_email_subaddresses = block_email_subaddresses

    @property
    def object(self):
        """Gets the object of this InstanceRestrictions.  # noqa: E501

        String representing the object's type. Objects of the same type share the same value.  # noqa: E501

        :return: The object of this InstanceRestrictions.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this InstanceRestrictions.

        String representing the object's type. Objects of the same type share the same value.  # noqa: E501

        :param object: The object of this InstanceRestrictions.  # noqa: E501
        :type: str
        """
        allowed_values = ["instance_restrictions"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def allowlist(self):
        """Gets the allowlist of this InstanceRestrictions.  # noqa: E501


        :return: The allowlist of this InstanceRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._allowlist

    @allowlist.setter
    def allowlist(self, allowlist):
        """Sets the allowlist of this InstanceRestrictions.


        :param allowlist: The allowlist of this InstanceRestrictions.  # noqa: E501
        :type: bool
        """

        self._allowlist = allowlist

    @property
    def blocklist(self):
        """Gets the blocklist of this InstanceRestrictions.  # noqa: E501


        :return: The blocklist of this InstanceRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._blocklist

    @blocklist.setter
    def blocklist(self, blocklist):
        """Sets the blocklist of this InstanceRestrictions.


        :param blocklist: The blocklist of this InstanceRestrictions.  # noqa: E501
        :type: bool
        """

        self._blocklist = blocklist

    @property
    def block_email_subaddresses(self):
        """Gets the block_email_subaddresses of this InstanceRestrictions.  # noqa: E501


        :return: The block_email_subaddresses of this InstanceRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._block_email_subaddresses

    @block_email_subaddresses.setter
    def block_email_subaddresses(self, block_email_subaddresses):
        """Sets the block_email_subaddresses of this InstanceRestrictions.


        :param block_email_subaddresses: The block_email_subaddresses of this InstanceRestrictions.  # noqa: E501
        :type: bool
        """

        self._block_email_subaddresses = block_email_subaddresses

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
        if issubclass(InstanceRestrictions, dict):
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
        if not isinstance(other, InstanceRestrictions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
