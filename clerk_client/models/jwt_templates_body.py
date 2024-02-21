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

class JwtTemplatesBody(object):
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
        'claims': 'object',
        'lifetime': 'float',
        'allowed_clock_skew': 'float',
        'custom_signing_key': 'bool',
        'signing_algorithm': 'str',
        'signing_key': 'str'
    }

    attribute_map = {
        'name': 'name',
        'claims': 'claims',
        'lifetime': 'lifetime',
        'allowed_clock_skew': 'allowed_clock_skew',
        'custom_signing_key': 'custom_signing_key',
        'signing_algorithm': 'signing_algorithm',
        'signing_key': 'signing_key'
    }

    def __init__(self, name=None, claims=None, lifetime=None, allowed_clock_skew=None, custom_signing_key=None, signing_algorithm=None, signing_key=None):  # noqa: E501
        """JwtTemplatesBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._claims = None
        self._lifetime = None
        self._allowed_clock_skew = None
        self._custom_signing_key = None
        self._signing_algorithm = None
        self._signing_key = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if claims is not None:
            self.claims = claims
        if lifetime is not None:
            self.lifetime = lifetime
        if allowed_clock_skew is not None:
            self.allowed_clock_skew = allowed_clock_skew
        if custom_signing_key is not None:
            self.custom_signing_key = custom_signing_key
        if signing_algorithm is not None:
            self.signing_algorithm = signing_algorithm
        if signing_key is not None:
            self.signing_key = signing_key

    @property
    def name(self):
        """Gets the name of this JwtTemplatesBody.  # noqa: E501

        JWT template name  # noqa: E501

        :return: The name of this JwtTemplatesBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JwtTemplatesBody.

        JWT template name  # noqa: E501

        :param name: The name of this JwtTemplatesBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def claims(self):
        """Gets the claims of this JwtTemplatesBody.  # noqa: E501

        JWT template claims in JSON format  # noqa: E501

        :return: The claims of this JwtTemplatesBody.  # noqa: E501
        :rtype: object
        """
        return self._claims

    @claims.setter
    def claims(self, claims):
        """Sets the claims of this JwtTemplatesBody.

        JWT template claims in JSON format  # noqa: E501

        :param claims: The claims of this JwtTemplatesBody.  # noqa: E501
        :type: object
        """

        self._claims = claims

    @property
    def lifetime(self):
        """Gets the lifetime of this JwtTemplatesBody.  # noqa: E501

        JWT token lifetime  # noqa: E501

        :return: The lifetime of this JwtTemplatesBody.  # noqa: E501
        :rtype: float
        """
        return self._lifetime

    @lifetime.setter
    def lifetime(self, lifetime):
        """Sets the lifetime of this JwtTemplatesBody.

        JWT token lifetime  # noqa: E501

        :param lifetime: The lifetime of this JwtTemplatesBody.  # noqa: E501
        :type: float
        """

        self._lifetime = lifetime

    @property
    def allowed_clock_skew(self):
        """Gets the allowed_clock_skew of this JwtTemplatesBody.  # noqa: E501

        JWT token allowed clock skew  # noqa: E501

        :return: The allowed_clock_skew of this JwtTemplatesBody.  # noqa: E501
        :rtype: float
        """
        return self._allowed_clock_skew

    @allowed_clock_skew.setter
    def allowed_clock_skew(self, allowed_clock_skew):
        """Sets the allowed_clock_skew of this JwtTemplatesBody.

        JWT token allowed clock skew  # noqa: E501

        :param allowed_clock_skew: The allowed_clock_skew of this JwtTemplatesBody.  # noqa: E501
        :type: float
        """

        self._allowed_clock_skew = allowed_clock_skew

    @property
    def custom_signing_key(self):
        """Gets the custom_signing_key of this JwtTemplatesBody.  # noqa: E501

        Whether a custom signing key/algorithm is also provided for this template  # noqa: E501

        :return: The custom_signing_key of this JwtTemplatesBody.  # noqa: E501
        :rtype: bool
        """
        return self._custom_signing_key

    @custom_signing_key.setter
    def custom_signing_key(self, custom_signing_key):
        """Sets the custom_signing_key of this JwtTemplatesBody.

        Whether a custom signing key/algorithm is also provided for this template  # noqa: E501

        :param custom_signing_key: The custom_signing_key of this JwtTemplatesBody.  # noqa: E501
        :type: bool
        """

        self._custom_signing_key = custom_signing_key

    @property
    def signing_algorithm(self):
        """Gets the signing_algorithm of this JwtTemplatesBody.  # noqa: E501

        The custom signing algorithm to use when minting JWTs  # noqa: E501

        :return: The signing_algorithm of this JwtTemplatesBody.  # noqa: E501
        :rtype: str
        """
        return self._signing_algorithm

    @signing_algorithm.setter
    def signing_algorithm(self, signing_algorithm):
        """Sets the signing_algorithm of this JwtTemplatesBody.

        The custom signing algorithm to use when minting JWTs  # noqa: E501

        :param signing_algorithm: The signing_algorithm of this JwtTemplatesBody.  # noqa: E501
        :type: str
        """

        self._signing_algorithm = signing_algorithm

    @property
    def signing_key(self):
        """Gets the signing_key of this JwtTemplatesBody.  # noqa: E501

        The custom signing private key to use when minting JWTs  # noqa: E501

        :return: The signing_key of this JwtTemplatesBody.  # noqa: E501
        :rtype: str
        """
        return self._signing_key

    @signing_key.setter
    def signing_key(self, signing_key):
        """Sets the signing_key of this JwtTemplatesBody.

        The custom signing private key to use when minting JWTs  # noqa: E501

        :param signing_key: The signing_key of this JwtTemplatesBody.  # noqa: E501
        :type: str
        """

        self._signing_key = signing_key

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
        if issubclass(JwtTemplatesBody, dict):
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
        if not isinstance(other, JwtTemplatesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
