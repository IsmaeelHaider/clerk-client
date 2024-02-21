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

class SAMLConnection(object):
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
        'name': 'str',
        'domain': 'str',
        'idp_entity_id': 'str',
        'idp_sso_url': 'str',
        'idp_certificate': 'str',
        'idp_metadata_url': 'str',
        'acs_url': 'str',
        'sp_entity_id': 'str',
        'sp_metadata_url': 'str',
        'attribute_mapping': 'SAMLConnectionAttributeMapping',
        'active': 'bool',
        'provider': 'str',
        'user_count': 'int',
        'sync_user_attributes': 'bool',
        'allow_subdomains': 'bool',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'name': 'name',
        'domain': 'domain',
        'idp_entity_id': 'idp_entity_id',
        'idp_sso_url': 'idp_sso_url',
        'idp_certificate': 'idp_certificate',
        'idp_metadata_url': 'idp_metadata_url',
        'acs_url': 'acs_url',
        'sp_entity_id': 'sp_entity_id',
        'sp_metadata_url': 'sp_metadata_url',
        'attribute_mapping': 'attribute_mapping',
        'active': 'active',
        'provider': 'provider',
        'user_count': 'user_count',
        'sync_user_attributes': 'sync_user_attributes',
        'allow_subdomains': 'allow_subdomains',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, object=None, id=None, name=None, domain=None, idp_entity_id=None, idp_sso_url=None, idp_certificate=None, idp_metadata_url=None, acs_url=None, sp_entity_id=None, sp_metadata_url=None, attribute_mapping=None, active=None, provider=None, user_count=None, sync_user_attributes=None, allow_subdomains=None, created_at=None, updated_at=None):  # noqa: E501
        """SAMLConnection - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._name = None
        self._domain = None
        self._idp_entity_id = None
        self._idp_sso_url = None
        self._idp_certificate = None
        self._idp_metadata_url = None
        self._acs_url = None
        self._sp_entity_id = None
        self._sp_metadata_url = None
        self._attribute_mapping = None
        self._active = None
        self._provider = None
        self._user_count = None
        self._sync_user_attributes = None
        self._allow_subdomains = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.object = object
        self.id = id
        self.name = name
        self.domain = domain
        self.idp_entity_id = idp_entity_id
        self.idp_sso_url = idp_sso_url
        self.idp_certificate = idp_certificate
        if idp_metadata_url is not None:
            self.idp_metadata_url = idp_metadata_url
        self.acs_url = acs_url
        self.sp_entity_id = sp_entity_id
        self.sp_metadata_url = sp_metadata_url
        if attribute_mapping is not None:
            self.attribute_mapping = attribute_mapping
        self.active = active
        self.provider = provider
        self.user_count = user_count
        self.sync_user_attributes = sync_user_attributes
        if allow_subdomains is not None:
            self.allow_subdomains = allow_subdomains
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def object(self):
        """Gets the object of this SAMLConnection.  # noqa: E501


        :return: The object of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this SAMLConnection.


        :param object: The object of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        allowed_values = ["saml_connection"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def id(self):
        """Gets the id of this SAMLConnection.  # noqa: E501


        :return: The id of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SAMLConnection.


        :param id: The id of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this SAMLConnection.  # noqa: E501


        :return: The name of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SAMLConnection.


        :param name: The name of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def domain(self):
        """Gets the domain of this SAMLConnection.  # noqa: E501


        :return: The domain of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SAMLConnection.


        :param domain: The domain of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def idp_entity_id(self):
        """Gets the idp_entity_id of this SAMLConnection.  # noqa: E501


        :return: The idp_entity_id of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, idp_entity_id):
        """Sets the idp_entity_id of this SAMLConnection.


        :param idp_entity_id: The idp_entity_id of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if idp_entity_id is None:
            raise ValueError("Invalid value for `idp_entity_id`, must not be `None`")  # noqa: E501

        self._idp_entity_id = idp_entity_id

    @property
    def idp_sso_url(self):
        """Gets the idp_sso_url of this SAMLConnection.  # noqa: E501


        :return: The idp_sso_url of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._idp_sso_url

    @idp_sso_url.setter
    def idp_sso_url(self, idp_sso_url):
        """Sets the idp_sso_url of this SAMLConnection.


        :param idp_sso_url: The idp_sso_url of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if idp_sso_url is None:
            raise ValueError("Invalid value for `idp_sso_url`, must not be `None`")  # noqa: E501

        self._idp_sso_url = idp_sso_url

    @property
    def idp_certificate(self):
        """Gets the idp_certificate of this SAMLConnection.  # noqa: E501


        :return: The idp_certificate of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._idp_certificate

    @idp_certificate.setter
    def idp_certificate(self, idp_certificate):
        """Sets the idp_certificate of this SAMLConnection.


        :param idp_certificate: The idp_certificate of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if idp_certificate is None:
            raise ValueError("Invalid value for `idp_certificate`, must not be `None`")  # noqa: E501

        self._idp_certificate = idp_certificate

    @property
    def idp_metadata_url(self):
        """Gets the idp_metadata_url of this SAMLConnection.  # noqa: E501


        :return: The idp_metadata_url of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._idp_metadata_url

    @idp_metadata_url.setter
    def idp_metadata_url(self, idp_metadata_url):
        """Sets the idp_metadata_url of this SAMLConnection.


        :param idp_metadata_url: The idp_metadata_url of this SAMLConnection.  # noqa: E501
        :type: str
        """

        self._idp_metadata_url = idp_metadata_url

    @property
    def acs_url(self):
        """Gets the acs_url of this SAMLConnection.  # noqa: E501


        :return: The acs_url of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._acs_url

    @acs_url.setter
    def acs_url(self, acs_url):
        """Sets the acs_url of this SAMLConnection.


        :param acs_url: The acs_url of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if acs_url is None:
            raise ValueError("Invalid value for `acs_url`, must not be `None`")  # noqa: E501

        self._acs_url = acs_url

    @property
    def sp_entity_id(self):
        """Gets the sp_entity_id of this SAMLConnection.  # noqa: E501


        :return: The sp_entity_id of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._sp_entity_id

    @sp_entity_id.setter
    def sp_entity_id(self, sp_entity_id):
        """Sets the sp_entity_id of this SAMLConnection.


        :param sp_entity_id: The sp_entity_id of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if sp_entity_id is None:
            raise ValueError("Invalid value for `sp_entity_id`, must not be `None`")  # noqa: E501

        self._sp_entity_id = sp_entity_id

    @property
    def sp_metadata_url(self):
        """Gets the sp_metadata_url of this SAMLConnection.  # noqa: E501


        :return: The sp_metadata_url of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._sp_metadata_url

    @sp_metadata_url.setter
    def sp_metadata_url(self, sp_metadata_url):
        """Sets the sp_metadata_url of this SAMLConnection.


        :param sp_metadata_url: The sp_metadata_url of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if sp_metadata_url is None:
            raise ValueError("Invalid value for `sp_metadata_url`, must not be `None`")  # noqa: E501

        self._sp_metadata_url = sp_metadata_url

    @property
    def attribute_mapping(self):
        """Gets the attribute_mapping of this SAMLConnection.  # noqa: E501


        :return: The attribute_mapping of this SAMLConnection.  # noqa: E501
        :rtype: SAMLConnectionAttributeMapping
        """
        return self._attribute_mapping

    @attribute_mapping.setter
    def attribute_mapping(self, attribute_mapping):
        """Sets the attribute_mapping of this SAMLConnection.


        :param attribute_mapping: The attribute_mapping of this SAMLConnection.  # noqa: E501
        :type: SAMLConnectionAttributeMapping
        """

        self._attribute_mapping = attribute_mapping

    @property
    def active(self):
        """Gets the active of this SAMLConnection.  # noqa: E501


        :return: The active of this SAMLConnection.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SAMLConnection.


        :param active: The active of this SAMLConnection.  # noqa: E501
        :type: bool
        """
        if active is None:
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def provider(self):
        """Gets the provider of this SAMLConnection.  # noqa: E501


        :return: The provider of this SAMLConnection.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this SAMLConnection.


        :param provider: The provider of this SAMLConnection.  # noqa: E501
        :type: str
        """
        if provider is None:
            raise ValueError("Invalid value for `provider`, must not be `None`")  # noqa: E501

        self._provider = provider

    @property
    def user_count(self):
        """Gets the user_count of this SAMLConnection.  # noqa: E501


        :return: The user_count of this SAMLConnection.  # noqa: E501
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """Sets the user_count of this SAMLConnection.


        :param user_count: The user_count of this SAMLConnection.  # noqa: E501
        :type: int
        """
        if user_count is None:
            raise ValueError("Invalid value for `user_count`, must not be `None`")  # noqa: E501

        self._user_count = user_count

    @property
    def sync_user_attributes(self):
        """Gets the sync_user_attributes of this SAMLConnection.  # noqa: E501


        :return: The sync_user_attributes of this SAMLConnection.  # noqa: E501
        :rtype: bool
        """
        return self._sync_user_attributes

    @sync_user_attributes.setter
    def sync_user_attributes(self, sync_user_attributes):
        """Sets the sync_user_attributes of this SAMLConnection.


        :param sync_user_attributes: The sync_user_attributes of this SAMLConnection.  # noqa: E501
        :type: bool
        """
        if sync_user_attributes is None:
            raise ValueError("Invalid value for `sync_user_attributes`, must not be `None`")  # noqa: E501

        self._sync_user_attributes = sync_user_attributes

    @property
    def allow_subdomains(self):
        """Gets the allow_subdomains of this SAMLConnection.  # noqa: E501


        :return: The allow_subdomains of this SAMLConnection.  # noqa: E501
        :rtype: bool
        """
        return self._allow_subdomains

    @allow_subdomains.setter
    def allow_subdomains(self, allow_subdomains):
        """Sets the allow_subdomains of this SAMLConnection.


        :param allow_subdomains: The allow_subdomains of this SAMLConnection.  # noqa: E501
        :type: bool
        """

        self._allow_subdomains = allow_subdomains

    @property
    def created_at(self):
        """Gets the created_at of this SAMLConnection.  # noqa: E501

        Unix timestamp of creation.   # noqa: E501

        :return: The created_at of this SAMLConnection.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SAMLConnection.

        Unix timestamp of creation.   # noqa: E501

        :param created_at: The created_at of this SAMLConnection.  # noqa: E501
        :type: int
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SAMLConnection.  # noqa: E501

        Unix timestamp of last update.   # noqa: E501

        :return: The updated_at of this SAMLConnection.  # noqa: E501
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SAMLConnection.

        Unix timestamp of last update.   # noqa: E501

        :param updated_at: The updated_at of this SAMLConnection.  # noqa: E501
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
        if issubclass(SAMLConnection, dict):
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
        if not isinstance(other, SAMLConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other