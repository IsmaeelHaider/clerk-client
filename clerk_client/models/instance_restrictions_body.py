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

class InstanceRestrictionsBody(object):
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
        'allowlist': 'bool',
        'blocklist': 'bool',
        'block_email_subaddresses': 'bool',
        'block_disposable_email_domains': 'bool'
    }

    attribute_map = {
        'allowlist': 'allowlist',
        'blocklist': 'blocklist',
        'block_email_subaddresses': 'block_email_subaddresses',
        'block_disposable_email_domains': 'block_disposable_email_domains'
    }

    def __init__(self, allowlist=None, blocklist=None, block_email_subaddresses=None, block_disposable_email_domains=None):  # noqa: E501
        """InstanceRestrictionsBody - a model defined in Swagger"""  # noqa: E501
        self._allowlist = None
        self._blocklist = None
        self._block_email_subaddresses = None
        self._block_disposable_email_domains = None
        self.discriminator = None
        if allowlist is not None:
            self.allowlist = allowlist
        if blocklist is not None:
            self.blocklist = blocklist
        if block_email_subaddresses is not None:
            self.block_email_subaddresses = block_email_subaddresses
        if block_disposable_email_domains is not None:
            self.block_disposable_email_domains = block_disposable_email_domains

    @property
    def allowlist(self):
        """Gets the allowlist of this InstanceRestrictionsBody.  # noqa: E501


        :return: The allowlist of this InstanceRestrictionsBody.  # noqa: E501
        :rtype: bool
        """
        return self._allowlist

    @allowlist.setter
    def allowlist(self, allowlist):
        """Sets the allowlist of this InstanceRestrictionsBody.


        :param allowlist: The allowlist of this InstanceRestrictionsBody.  # noqa: E501
        :type: bool
        """

        self._allowlist = allowlist

    @property
    def blocklist(self):
        """Gets the blocklist of this InstanceRestrictionsBody.  # noqa: E501


        :return: The blocklist of this InstanceRestrictionsBody.  # noqa: E501
        :rtype: bool
        """
        return self._blocklist

    @blocklist.setter
    def blocklist(self, blocklist):
        """Sets the blocklist of this InstanceRestrictionsBody.


        :param blocklist: The blocklist of this InstanceRestrictionsBody.  # noqa: E501
        :type: bool
        """

        self._blocklist = blocklist

    @property
    def block_email_subaddresses(self):
        """Gets the block_email_subaddresses of this InstanceRestrictionsBody.  # noqa: E501


        :return: The block_email_subaddresses of this InstanceRestrictionsBody.  # noqa: E501
        :rtype: bool
        """
        return self._block_email_subaddresses

    @block_email_subaddresses.setter
    def block_email_subaddresses(self, block_email_subaddresses):
        """Sets the block_email_subaddresses of this InstanceRestrictionsBody.


        :param block_email_subaddresses: The block_email_subaddresses of this InstanceRestrictionsBody.  # noqa: E501
        :type: bool
        """

        self._block_email_subaddresses = block_email_subaddresses

    @property
    def block_disposable_email_domains(self):
        """Gets the block_disposable_email_domains of this InstanceRestrictionsBody.  # noqa: E501


        :return: The block_disposable_email_domains of this InstanceRestrictionsBody.  # noqa: E501
        :rtype: bool
        """
        return self._block_disposable_email_domains

    @block_disposable_email_domains.setter
    def block_disposable_email_domains(self, block_disposable_email_domains):
        """Sets the block_disposable_email_domains of this InstanceRestrictionsBody.


        :param block_disposable_email_domains: The block_disposable_email_domains of this InstanceRestrictionsBody.  # noqa: E501
        :type: bool
        """

        self._block_disposable_email_domains = block_disposable_email_domains

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
        if issubclass(InstanceRestrictionsBody, dict):
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
        if not isinstance(other, InstanceRestrictionsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other