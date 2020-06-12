# coding: utf-8

"""
    bAmpli API

    Business Amplifier API  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Cyclo(object):
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
        'cyclo': 'str',
        'name': 'str',
        'last_modified': 'datetime',
        'company': 'Company'
    }

    attribute_map = {
        'cyclo': 'cyclo',
        'name': 'name',
        'last_modified': 'lastModified',
        'company': 'company'
    }

    def __init__(self, cyclo=None, name=None, last_modified=None, company=None):  # noqa: E501
        """Cyclo - a model defined in Swagger"""  # noqa: E501
        self._cyclo = None
        self._name = None
        self._last_modified = None
        self._company = None
        self.discriminator = None
        self.cyclo = cyclo
        self.name = name
        self.last_modified = last_modified
        self.company = company

    @property
    def cyclo(self):
        """Gets the cyclo of this Cyclo.  # noqa: E501


        :return: The cyclo of this Cyclo.  # noqa: E501
        :rtype: str
        """
        return self._cyclo

    @cyclo.setter
    def cyclo(self, cyclo):
        """Sets the cyclo of this Cyclo.


        :param cyclo: The cyclo of this Cyclo.  # noqa: E501
        :type: str
        """
        if cyclo is None:
            raise ValueError("Invalid value for `cyclo`, must not be `None`")  # noqa: E501

        self._cyclo = cyclo

    @property
    def name(self):
        """Gets the name of this Cyclo.  # noqa: E501


        :return: The name of this Cyclo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cyclo.


        :param name: The name of this Cyclo.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_modified(self):
        """Gets the last_modified of this Cyclo.  # noqa: E501


        :return: The last_modified of this Cyclo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified):
        """Sets the last_modified of this Cyclo.


        :param last_modified: The last_modified of this Cyclo.  # noqa: E501
        :type: datetime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def company(self):
        """Gets the company of this Cyclo.  # noqa: E501


        :return: The company of this Cyclo.  # noqa: E501
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this Cyclo.


        :param company: The company of this Cyclo.  # noqa: E501
        :type: Company
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

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
        if issubclass(Cyclo, dict):
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
        if not isinstance(other, Cyclo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
