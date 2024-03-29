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

class DomainsBody(object):
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
        'name': 'str',
        'is_satellite': 'bool',
        'proxy_url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'is_satellite': 'is_satellite',
        'proxy_url': 'proxy_url'
    }

    def __init__(self, name=None, is_satellite=None, proxy_url=None):  # noqa: E501
        """DomainsBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._is_satellite = None
        self._proxy_url = None
        self.discriminator = None
        self.name = name
        self.is_satellite = is_satellite
        if proxy_url is not None:
            self.proxy_url = proxy_url

    @property
    def name(self):
        """Gets the name of this DomainsBody.  # noqa: E501

        The new domain name. Can contain the port for development instances.  # noqa: E501

        :return: The name of this DomainsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DomainsBody.

        The new domain name. Can contain the port for development instances.  # noqa: E501

        :param name: The name of this DomainsBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_satellite(self):
        """Gets the is_satellite of this DomainsBody.  # noqa: E501

        Marks the new domain as satellite. Only `true` is accepted at the moment.  # noqa: E501

        :return: The is_satellite of this DomainsBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_satellite

    @is_satellite.setter
    def is_satellite(self, is_satellite):
        """Sets the is_satellite of this DomainsBody.

        Marks the new domain as satellite. Only `true` is accepted at the moment.  # noqa: E501

        :param is_satellite: The is_satellite of this DomainsBody.  # noqa: E501
        :type: bool
        """
        if is_satellite is None:
            raise ValueError("Invalid value for `is_satellite`, must not be `None`")  # noqa: E501

        self._is_satellite = is_satellite

    @property
    def proxy_url(self):
        """Gets the proxy_url of this DomainsBody.  # noqa: E501

        The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances.  # noqa: E501

        :return: The proxy_url of this DomainsBody.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this DomainsBody.

        The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. Applicable only to production instances.  # noqa: E501

        :param proxy_url: The proxy_url of this DomainsBody.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

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
        if issubclass(DomainsBody, dict):
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
        if not isinstance(other, DomainsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
