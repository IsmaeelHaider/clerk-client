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

class BetaFeaturesInstanceSettingsBody(object):
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
        'restricted_to_allowlist': 'bool',
        'from_email_address': 'str',
        'progressive_sign_up': 'bool',
        'session_token_template': 'str',
        'enhanced_email_deliverability': 'bool',
        'test_mode': 'bool'
    }

    attribute_map = {
        'restricted_to_allowlist': 'restricted_to_allowlist',
        'from_email_address': 'from_email_address',
        'progressive_sign_up': 'progressive_sign_up',
        'session_token_template': 'session_token_template',
        'enhanced_email_deliverability': 'enhanced_email_deliverability',
        'test_mode': 'test_mode'
    }

    def __init__(self, restricted_to_allowlist=False, from_email_address=None, progressive_sign_up=None, session_token_template=None, enhanced_email_deliverability=None, test_mode=None):  # noqa: E501
        """BetaFeaturesInstanceSettingsBody - a model defined in Swagger"""  # noqa: E501
        self._restricted_to_allowlist = None
        self._from_email_address = None
        self._progressive_sign_up = None
        self._session_token_template = None
        self._enhanced_email_deliverability = None
        self._test_mode = None
        self.discriminator = None
        if restricted_to_allowlist is not None:
            self.restricted_to_allowlist = restricted_to_allowlist
        if from_email_address is not None:
            self.from_email_address = from_email_address
        if progressive_sign_up is not None:
            self.progressive_sign_up = progressive_sign_up
        if session_token_template is not None:
            self.session_token_template = session_token_template
        if enhanced_email_deliverability is not None:
            self.enhanced_email_deliverability = enhanced_email_deliverability
        if test_mode is not None:
            self.test_mode = test_mode

    @property
    def restricted_to_allowlist(self):
        """Gets the restricted_to_allowlist of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist.  # noqa: E501

        :return: The restricted_to_allowlist of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: bool
        """
        return self._restricted_to_allowlist

    @restricted_to_allowlist.setter
    def restricted_to_allowlist(self, restricted_to_allowlist):
        """Sets the restricted_to_allowlist of this BetaFeaturesInstanceSettingsBody.

        Whether sign up is restricted to email addresses, phone numbers and usernames that are on the allowlist.  # noqa: E501

        :param restricted_to_allowlist: The restricted_to_allowlist of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: bool
        """

        self._restricted_to_allowlist = restricted_to_allowlist

    @property
    def from_email_address(self):
        """Gets the from_email_address of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent. Only alphanumeric values are allowed. Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`).  # noqa: E501

        :return: The from_email_address of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: str
        """
        return self._from_email_address

    @from_email_address.setter
    def from_email_address(self, from_email_address):
        """Sets the from_email_address of this BetaFeaturesInstanceSettingsBody.

        The local part of the email address from which authentication-related emails (e.g. OTP code, magic links) will be sent. Only alphanumeric values are allowed. Note that this value should contain only the local part of the address (e.g. `foo` for `foo@example.com`).  # noqa: E501

        :param from_email_address: The from_email_address of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: str
        """

        self._from_email_address = from_email_address

    @property
    def progressive_sign_up(self):
        """Gets the progressive_sign_up of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info.  # noqa: E501

        :return: The progressive_sign_up of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: bool
        """
        return self._progressive_sign_up

    @progressive_sign_up.setter
    def progressive_sign_up(self, progressive_sign_up):
        """Sets the progressive_sign_up of this BetaFeaturesInstanceSettingsBody.

        Enable the Progressive Sign Up algorithm. Refer to the [docs](https://clerk.com/docs/upgrade-guides/progressive-sign-up) for more info.  # noqa: E501

        :param progressive_sign_up: The progressive_sign_up of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: bool
        """

        self._progressive_sign_up = progressive_sign_up

    @property
    def session_token_template(self):
        """Gets the session_token_template of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string.  # noqa: E501

        :return: The session_token_template of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: str
        """
        return self._session_token_template

    @session_token_template.setter
    def session_token_template(self, session_token_template):
        """Sets the session_token_template of this BetaFeaturesInstanceSettingsBody.

        The name of the JWT Template used to augment your session tokens. To disable this, pass an empty string.  # noqa: E501

        :param session_token_template: The session_token_template of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: str
        """

        self._session_token_template = session_token_template

    @property
    def enhanced_email_deliverability(self):
        """Gets the enhanced_email_deliverability of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain. This can be helpful if you do not have a high domain reputation.  # noqa: E501

        :return: The enhanced_email_deliverability of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: bool
        """
        return self._enhanced_email_deliverability

    @enhanced_email_deliverability.setter
    def enhanced_email_deliverability(self, enhanced_email_deliverability):
        """Sets the enhanced_email_deliverability of this BetaFeaturesInstanceSettingsBody.

        The \"enhanced_email_deliverability\" feature will send emails from \"verifications@clerk.dev\" instead of your domain. This can be helpful if you do not have a high domain reputation.  # noqa: E501

        :param enhanced_email_deliverability: The enhanced_email_deliverability of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: bool
        """

        self._enhanced_email_deliverability = enhanced_email_deliverability

    @property
    def test_mode(self):
        """Gets the test_mode of this BetaFeaturesInstanceSettingsBody.  # noqa: E501

        Toggles test mode for this instance, allowing the use of test email addresses and phone numbers. Defaults to true for development instances.  # noqa: E501

        :return: The test_mode of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :rtype: bool
        """
        return self._test_mode

    @test_mode.setter
    def test_mode(self, test_mode):
        """Sets the test_mode of this BetaFeaturesInstanceSettingsBody.

        Toggles test mode for this instance, allowing the use of test email addresses and phone numbers. Defaults to true for development instances.  # noqa: E501

        :param test_mode: The test_mode of this BetaFeaturesInstanceSettingsBody.  # noqa: E501
        :type: bool
        """

        self._test_mode = test_mode

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
        if issubclass(BetaFeaturesInstanceSettingsBody, dict):
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
        if not isinstance(other, BetaFeaturesInstanceSettingsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other