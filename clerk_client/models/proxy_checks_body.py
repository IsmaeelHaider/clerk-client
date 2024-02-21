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

class ProxyChecksBody(object):
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
        'domain_id': 'str',
        'proxy_url': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'proxy_url': 'proxy_url'
    }

    def __init__(self, domain_id=None, proxy_url=None):  # noqa: E501
        """ProxyChecksBody - a model defined in Swagger"""  # noqa: E501
        self._domain_id = None
        self._proxy_url = None
        self.discriminator = None
        if domain_id is not None:
            self.domain_id = domain_id
        if proxy_url is not None:
            self.proxy_url = proxy_url

    @property
    def domain_id(self):
        """Gets the domain_id of this ProxyChecksBody.  # noqa: E501

        The ID of the domain that will be updated.  # noqa: E501

        :return: The domain_id of this ProxyChecksBody.  # noqa: E501
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this ProxyChecksBody.

        The ID of the domain that will be updated.  # noqa: E501

        :param domain_id: The domain_id of this ProxyChecksBody.  # noqa: E501
        :type: str
        """

        self._domain_id = domain_id

    @property
    def proxy_url(self):
        """Gets the proxy_url of this ProxyChecksBody.  # noqa: E501

        The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk  # noqa: E501

        :return: The proxy_url of this ProxyChecksBody.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this ProxyChecksBody.

        The full URL of the proxy which will forward requests to the Clerk Frontend API for this domain. e.g. https://example.com/__clerk  # noqa: E501

        :param proxy_url: The proxy_url of this ProxyChecksBody.  # noqa: E501
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
        if issubclass(ProxyChecksBody, dict):
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
        if not isinstance(other, ProxyChecksBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
