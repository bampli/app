# coding: utf-8

"""
    bampli-api

    The API for the Business Amplifier project  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CompanyAddress(object):
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
        'street': 'str',
        'street2': 'str',
        'city': 'str',
        'zipcode': 'str',
        'tax_id': 'str'
    }

    attribute_map = {
        'street': 'street',
        'street2': 'street2',
        'city': 'city',
        'zipcode': 'zipcode',
        'tax_id': 'taxId'
    }

    def __init__(self, street=None, street2=None, city=None, zipcode=None, tax_id=None):  # noqa: E501
        """CompanyAddress - a model defined in Swagger"""  # noqa: E501
        self._street = None
        self._street2 = None
        self._city = None
        self._zipcode = None
        self._tax_id = None
        self.discriminator = None
        self.street = street
        if street2 is not None:
            self.street2 = street2
        self.city = city
        self.zipcode = zipcode
        self.tax_id = tax_id

    @property
    def street(self):
        """Gets the street of this CompanyAddress.  # noqa: E501


        :return: The street of this CompanyAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this CompanyAddress.


        :param street: The street of this CompanyAddress.  # noqa: E501
        :type: str
        """
        if street is None:
            raise ValueError("Invalid value for `street`, must not be `None`")  # noqa: E501

        self._street = street

    @property
    def street2(self):
        """Gets the street2 of this CompanyAddress.  # noqa: E501


        :return: The street2 of this CompanyAddress.  # noqa: E501
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """Sets the street2 of this CompanyAddress.


        :param street2: The street2 of this CompanyAddress.  # noqa: E501
        :type: str
        """

        self._street2 = street2

    @property
    def city(self):
        """Gets the city of this CompanyAddress.  # noqa: E501


        :return: The city of this CompanyAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CompanyAddress.


        :param city: The city of this CompanyAddress.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def zipcode(self):
        """Gets the zipcode of this CompanyAddress.  # noqa: E501


        :return: The zipcode of this CompanyAddress.  # noqa: E501
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """Sets the zipcode of this CompanyAddress.


        :param zipcode: The zipcode of this CompanyAddress.  # noqa: E501
        :type: str
        """
        if zipcode is None:
            raise ValueError("Invalid value for `zipcode`, must not be `None`")  # noqa: E501

        self._zipcode = zipcode

    @property
    def tax_id(self):
        """Gets the tax_id of this CompanyAddress.  # noqa: E501


        :return: The tax_id of this CompanyAddress.  # noqa: E501
        :rtype: str
        """
        return self._tax_id

    @tax_id.setter
    def tax_id(self, tax_id):
        """Sets the tax_id of this CompanyAddress.


        :param tax_id: The tax_id of this CompanyAddress.  # noqa: E501
        :type: str
        """
        if tax_id is None:
            raise ValueError("Invalid value for `tax_id`, must not be `None`")  # noqa: E501

        self._tax_id = tax_id

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
        if issubclass(CompanyAddress, dict):
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
        if not isinstance(other, CompanyAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
