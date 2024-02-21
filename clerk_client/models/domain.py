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

class Domain(object):
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
        'is_satellite': 'bool',
        'frontend_api_url': 'str',
        'accounts_portal_url': 'str',
        'proxy_url': 'str',
        'development_origin': 'str',
        'cname_targets': 'list[CNameTarget]'
    }

    attribute_map = {
        'object': 'object',
        'id': 'id',
        'name': 'name',
        'is_satellite': 'is_satellite',
        'frontend_api_url': 'frontend_api_url',
        'accounts_portal_url': 'accounts_portal_url',
        'proxy_url': 'proxy_url',
        'development_origin': 'development_origin',
        'cname_targets': 'cname_targets'
    }

    def __init__(self, object=None, id=None, name=None, is_satellite=None, frontend_api_url=None, accounts_portal_url=None, proxy_url=None, development_origin=None, cname_targets=None):  # noqa: E501
        """Domain - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._id = None
        self._name = None
        self._is_satellite = None
        self._frontend_api_url = None
        self._accounts_portal_url = None
        self._proxy_url = None
        self._development_origin = None
        self._cname_targets = None
        self.discriminator = None
        self.object = object
        self.id = id
        self.name = name
        self.is_satellite = is_satellite
        self.frontend_api_url = frontend_api_url
        if accounts_portal_url is not None:
            self.accounts_portal_url = accounts_portal_url
        if proxy_url is not None:
            self.proxy_url = proxy_url
        self.development_origin = development_origin
        if cname_targets is not None:
            self.cname_targets = cname_targets

    @property
    def object(self):
        """Gets the object of this Domain.  # noqa: E501


        :return: The object of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this Domain.


        :param object: The object of this Domain.  # noqa: E501
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")  # noqa: E501
        allowed_values = ["domain"]  # noqa: E501
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"  # noqa: E501
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def id(self):
        """Gets the id of this Domain.  # noqa: E501


        :return: The id of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Domain.


        :param id: The id of this Domain.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Domain.  # noqa: E501


        :return: The name of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Domain.


        :param name: The name of this Domain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def is_satellite(self):
        """Gets the is_satellite of this Domain.  # noqa: E501


        :return: The is_satellite of this Domain.  # noqa: E501
        :rtype: bool
        """
        return self._is_satellite

    @is_satellite.setter
    def is_satellite(self, is_satellite):
        """Sets the is_satellite of this Domain.


        :param is_satellite: The is_satellite of this Domain.  # noqa: E501
        :type: bool
        """
        if is_satellite is None:
            raise ValueError("Invalid value for `is_satellite`, must not be `None`")  # noqa: E501

        self._is_satellite = is_satellite

    @property
    def frontend_api_url(self):
        """Gets the frontend_api_url of this Domain.  # noqa: E501


        :return: The frontend_api_url of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._frontend_api_url

    @frontend_api_url.setter
    def frontend_api_url(self, frontend_api_url):
        """Sets the frontend_api_url of this Domain.


        :param frontend_api_url: The frontend_api_url of this Domain.  # noqa: E501
        :type: str
        """
        if frontend_api_url is None:
            raise ValueError("Invalid value for `frontend_api_url`, must not be `None`")  # noqa: E501

        self._frontend_api_url = frontend_api_url

    @property
    def accounts_portal_url(self):
        """Gets the accounts_portal_url of this Domain.  # noqa: E501

        Null for satellite domains.   # noqa: E501

        :return: The accounts_portal_url of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._accounts_portal_url

    @accounts_portal_url.setter
    def accounts_portal_url(self, accounts_portal_url):
        """Sets the accounts_portal_url of this Domain.

        Null for satellite domains.   # noqa: E501

        :param accounts_portal_url: The accounts_portal_url of this Domain.  # noqa: E501
        :type: str
        """

        self._accounts_portal_url = accounts_portal_url

    @property
    def proxy_url(self):
        """Gets the proxy_url of this Domain.  # noqa: E501


        :return: The proxy_url of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._proxy_url

    @proxy_url.setter
    def proxy_url(self, proxy_url):
        """Sets the proxy_url of this Domain.


        :param proxy_url: The proxy_url of this Domain.  # noqa: E501
        :type: str
        """

        self._proxy_url = proxy_url

    @property
    def development_origin(self):
        """Gets the development_origin of this Domain.  # noqa: E501


        :return: The development_origin of this Domain.  # noqa: E501
        :rtype: str
        """
        return self._development_origin

    @development_origin.setter
    def development_origin(self, development_origin):
        """Sets the development_origin of this Domain.


        :param development_origin: The development_origin of this Domain.  # noqa: E501
        :type: str
        """
        if development_origin is None:
            raise ValueError("Invalid value for `development_origin`, must not be `None`")  # noqa: E501

        self._development_origin = development_origin

    @property
    def cname_targets(self):
        """Gets the cname_targets of this Domain.  # noqa: E501


        :return: The cname_targets of this Domain.  # noqa: E501
        :rtype: list[CNameTarget]
        """
        return self._cname_targets

    @cname_targets.setter
    def cname_targets(self, cname_targets):
        """Sets the cname_targets of this Domain.


        :param cname_targets: The cname_targets of this Domain.  # noqa: E501
        :type: list[CNameTarget]
        """

        self._cname_targets = cname_targets

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
        if issubclass(Domain, dict):
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
        if not isinstance(other, Domain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
