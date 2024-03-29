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

class Web3Wallet(object):
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
        'id': 'str',
        'object': 'str',
        'web3_wallet': 'str',
        'verification': 'OneOfWeb3WalletVerification'
    }

    attribute_map = {
        'id': 'id',
        'object': 'object',
        'web3_wallet': 'web3_wallet',
        'verification': 'verification'
    }

    def __init__(self, id=None, object=None, web3_wallet=None, verification=None):  # noqa: E501
        """Web3Wallet - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._object = None
        self._web3_wallet = None
        self._verification = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.object = object
        self.web3_wallet = web3_wallet
        self.verification = verification

    @property
    def id(self):
        """Gets the id of this Web3Wallet.  # noqa: E501


        :return: The id of this Web3Wallet.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Web3Wallet.


        :param id: The id of this Web3Wallet.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def object(self):
        """Gets the object of this Web3Wallet.  # noqa: E501

        String representing the object's type. Objects of the same type share the same value.   # noqa: E501

        :return: The object of this Web3Wallet.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Web3Wallet.

        String representing the object's type. Objects of the same type share the same value.   # noqa: E501

        :param object: The object of this Web3Wallet.  # noqa: E501
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        allowed_values = ["web3_wallet"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def web3_wallet(self):
        """Gets the web3_wallet of this Web3Wallet.  # noqa: E501


        :return: The web3_wallet of this Web3Wallet.  # noqa: E501
        :rtype: str
        """
        return self._web3_wallet

    @web3_wallet.setter
    def web3_wallet(self, web3_wallet):
        """Sets the web3_wallet of this Web3Wallet.


        :param web3_wallet: The web3_wallet of this Web3Wallet.  # noqa: E501
        :type: str
        """
        if web3_wallet is None:
            raise ValueError("Invalid value for `web3_wallet`, must not be `None`")  # noqa: E501

        self._web3_wallet = web3_wallet

    @property
    def verification(self):
        """Gets the verification of this Web3Wallet.  # noqa: E501


        :return: The verification of this Web3Wallet.  # noqa: E501
        :rtype: OneOfWeb3WalletVerification
        """
        return self._verification

    @verification.setter
    def verification(self, verification):
        """Sets the verification of this Web3Wallet.


        :param verification: The verification of this Web3Wallet.  # noqa: E501
        :type: OneOfWeb3WalletVerification
        """
        if verification is None:
            raise ValueError("Invalid value for `verification`, must not be `None`")  # noqa: E501

        self._verification = verification

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
        if issubclass(Web3Wallet, dict):
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
        if not isinstance(other, Web3Wallet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
