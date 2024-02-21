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

class OrganizationsBody(object):
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
        'created_by': 'str',
        'private_metadata': 'object',
        'public_metadata': 'object',
        'slug': 'str',
        'max_allowed_memberships': 'int'
    }

    attribute_map = {
        'name': 'name',
        'created_by': 'created_by',
        'private_metadata': 'private_metadata',
        'public_metadata': 'public_metadata',
        'slug': 'slug',
        'max_allowed_memberships': 'max_allowed_memberships'
    }

    def __init__(self, name=None, created_by=None, private_metadata=None, public_metadata=None, slug=None, max_allowed_memberships=None):  # noqa: E501
        """OrganizationsBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._created_by = None
        self._private_metadata = None
        self._public_metadata = None
        self._slug = None
        self._max_allowed_memberships = None
        self.discriminator = None
        self.name = name
        self.created_by = created_by
        if private_metadata is not None:
            self.private_metadata = private_metadata
        if public_metadata is not None:
            self.public_metadata = public_metadata
        if slug is not None:
            self.slug = slug
        if max_allowed_memberships is not None:
            self.max_allowed_memberships = max_allowed_memberships

    @property
    def name(self):
        """Gets the name of this OrganizationsBody.  # noqa: E501

        The name of the new organization  # noqa: E501

        :return: The name of this OrganizationsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationsBody.

        The name of the new organization  # noqa: E501

        :param name: The name of this OrganizationsBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this OrganizationsBody.  # noqa: E501

        The ID of the User who will become the administrator for the new organization  # noqa: E501

        :return: The created_by of this OrganizationsBody.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this OrganizationsBody.

        The ID of the User who will become the administrator for the new organization  # noqa: E501

        :param created_by: The created_by of this OrganizationsBody.  # noqa: E501
        :type: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def private_metadata(self):
        """Gets the private_metadata of this OrganizationsBody.  # noqa: E501

        Metadata saved on the organization, accessible only from the Backend API  # noqa: E501

        :return: The private_metadata of this OrganizationsBody.  # noqa: E501
        :rtype: object
        """
        return self._private_metadata

    @private_metadata.setter
    def private_metadata(self, private_metadata):
        """Sets the private_metadata of this OrganizationsBody.

        Metadata saved on the organization, accessible only from the Backend API  # noqa: E501

        :param private_metadata: The private_metadata of this OrganizationsBody.  # noqa: E501
        :type: object
        """

        self._private_metadata = private_metadata

    @property
    def public_metadata(self):
        """Gets the public_metadata of this OrganizationsBody.  # noqa: E501

        Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API  # noqa: E501

        :return: The public_metadata of this OrganizationsBody.  # noqa: E501
        :rtype: object
        """
        return self._public_metadata

    @public_metadata.setter
    def public_metadata(self, public_metadata):
        """Sets the public_metadata of this OrganizationsBody.

        Metadata saved on the organization, read-only from the Frontend API and fully accessible (read/write) from the Backend API  # noqa: E501

        :param public_metadata: The public_metadata of this OrganizationsBody.  # noqa: E501
        :type: object
        """

        self._public_metadata = public_metadata

    @property
    def slug(self):
        """Gets the slug of this OrganizationsBody.  # noqa: E501

        A slug for the new organization. Can contain only lowercase alphanumeric characters and the dash \"-\". Must be unique for the instance.  # noqa: E501

        :return: The slug of this OrganizationsBody.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OrganizationsBody.

        A slug for the new organization. Can contain only lowercase alphanumeric characters and the dash \"-\". Must be unique for the instance.  # noqa: E501

        :param slug: The slug of this OrganizationsBody.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def max_allowed_memberships(self):
        """Gets the max_allowed_memberships of this OrganizationsBody.  # noqa: E501

        The maximum number of memberships allowed for this organization  # noqa: E501

        :return: The max_allowed_memberships of this OrganizationsBody.  # noqa: E501
        :rtype: int
        """
        return self._max_allowed_memberships

    @max_allowed_memberships.setter
    def max_allowed_memberships(self, max_allowed_memberships):
        """Sets the max_allowed_memberships of this OrganizationsBody.

        The maximum number of memberships allowed for this organization  # noqa: E501

        :param max_allowed_memberships: The max_allowed_memberships of this OrganizationsBody.  # noqa: E501
        :type: int
        """

        self._max_allowed_memberships = max_allowed_memberships

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
        if issubclass(OrganizationsBody, dict):
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
        if not isinstance(other, OrganizationsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other