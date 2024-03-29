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

class Invitation(object):
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
        'id': 'str',
        'email_address': 'str',
        'public_metadata': 'object',
        'revoked': 'bool',
        'status': 'str',
        'url': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'email_address': 'email_address',
        'public_metadata': 'public_metadata',
        'revoked': 'revoked',
        'status': 'status',
        'url': 'url',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, object=None, id=None, email_address=None, public_metadata=None, revoked=None, status=None, url=None, created_at=None, updated_at=None):  # noqa: E501
        """Invitation - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._email_address = None
        self._public_metadata = None
        self._revoked = None
        self._status = None
        self._url = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.object = object
        self.id = id
        self.email_address = email_address
        if public_metadata is not None:
            self.public_metadata = public_metadata
        if revoked is not None:
            self.revoked = revoked
        self.status = status
        if url is not None:
            self.url = url
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def object(self):
        """Gets the object of this Invitation.  # noqa: E501


        :return: The object of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Invitation.


        :param object: The object of this Invitation.  # noqa: E501
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        allowed_values = ["invitation"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501


        :return: The id of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.


        :param id: The id of this Invitation.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def email_address(self):
        """Gets the email_address of this Invitation.  # noqa: E501


        :return: The email_address of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Invitation.


        :param email_address: The email_address of this Invitation.  # noqa: E501
        :type: str
        """
        if email_address is None:
            raise ValueError("Invalid value for `email_address`, must not be `None`")  # noqa: E501

        self._email_address = email_address

    @property
    def public_metadata(self):
        """Gets the public_metadata of this Invitation.  # noqa: E501


        :return: The public_metadata of this Invitation.  # noqa: E501
        :rtype: object
        """
        return self._public_metadata

    @public_metadata.setter
    def public_metadata(self, public_metadata):
        """Sets the public_metadata of this Invitation.


        :param public_metadata: The public_metadata of this Invitation.  # noqa: E501
        :type: object
        """

        self._public_metadata = public_metadata

    @property
    def revoked(self):
        """Gets the revoked of this Invitation.  # noqa: E501


        :return: The revoked of this Invitation.  # noqa: E501
        :rtype: bool
        """
        return self._revoked

    @revoked.setter
    def revoked(self, revoked):
        """Sets the revoked of this Invitation.


        :param revoked: The revoked of this Invitation.  # noqa: E501
        :type: bool
        """

        self._revoked = revoked

    @property
    def status(self):
        """Gets the status of this Invitation.  # noqa: E501


        :return: The status of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Invitation.


        :param status: The status of this Invitation.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["pending", "accepted", "revoked"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def url(self):
        """Gets the url of this Invitation.  # noqa: E501


        :return: The url of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Invitation.


        :param url: The url of this Invitation.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def created_at(self):
        """Gets the created_at of this Invitation.  # noqa: E501

        Unix timestamp of creation.   # noqa: E501

        :return: The created_at of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Invitation.

        Unix timestamp of creation.   # noqa: E501

        :param created_at: The created_at of this Invitation.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Invitation.  # noqa: E501

        Unix timestamp of last update.   # noqa: E501

        :return: The updated_at of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Invitation.

        Unix timestamp of last update.   # noqa: E501

        :param updated_at: The updated_at of this Invitation.  # noqa: E501
        :type: int
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(Invitation, dict):
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
        if not isinstance(other, Invitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
