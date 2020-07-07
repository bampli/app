# coding: utf-8

"""
    bampli-api

    The API for the Business Amplifier project.  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: josemotta@bampli.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Product(object):
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
        'product_id': 'str',
        'name': 'str',
        'active': 'bool',
        'company_id': 'str'
    }

    attribute_map = {
        'product_id': 'product_id',
        'name': 'name',
        'active': 'active',
        'company_id': 'company_id'
    }

    def __init__(self, product_id=None, name=None, active=True, company_id=None):  # noqa: E501
        """Product - a model defined in Swagger"""  # noqa: E501
        self._product_id = None
        self._name = None
        self._active = None
        self._company_id = None
        self.discriminator = None
        self.product_id = product_id
        self.name = name
        if active is not None:
            self.active = active
        self.company_id = company_id

    @property
    def product_id(self):
        """Gets the product_id of this Product.  # noqa: E501

        Auto-generated primary key field  # noqa: E501

        :return: The product_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this Product.

        Auto-generated primary key field  # noqa: E501

        :param product_id: The product_id of this Product.  # noqa: E501
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")  # noqa: E501

        self._product_id = product_id

    @property
    def name(self):
        """Gets the name of this Product.  # noqa: E501


        :return: The name of this Product.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Product.


        :param name: The name of this Product.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def active(self):
        """Gets the active of this Product.  # noqa: E501


        :return: The active of this Product.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Product.


        :param active: The active of this Product.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def company_id(self):
        """Gets the company_id of this Product.  # noqa: E501

        This property is a reference to a Company  # noqa: E501

        :return: The company_id of this Product.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this Product.

        This property is a reference to a Company  # noqa: E501

        :param company_id: The company_id of this Product.  # noqa: E501
        :type: str
        """
        if company_id is None:
            raise ValueError("Invalid value for `company_id`, must not be `None`")  # noqa: E501

        self._company_id = company_id

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
        if issubclass(Product, dict):
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
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
