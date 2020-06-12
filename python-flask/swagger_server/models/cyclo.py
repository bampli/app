# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.company import Company  # noqa: F401,E501
from swagger_server import util


class Cyclo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cyclo: str=None, name: str=None, last_modified: datetime=None, company: Company=None):  # noqa: E501
        """Cyclo - a model defined in Swagger

        :param cyclo: The cyclo of this Cyclo.  # noqa: E501
        :type cyclo: str
        :param name: The name of this Cyclo.  # noqa: E501
        :type name: str
        :param last_modified: The last_modified of this Cyclo.  # noqa: E501
        :type last_modified: datetime
        :param company: The company of this Cyclo.  # noqa: E501
        :type company: Company
        """
        self.swagger_types = {
            'cyclo': str,
            'name': str,
            'last_modified': datetime,
            'company': Company
        }

        self.attribute_map = {
            'cyclo': 'cyclo',
            'name': 'name',
            'last_modified': 'lastModified',
            'company': 'company'
        }
        self._cyclo = cyclo
        self._name = name
        self._last_modified = last_modified
        self._company = company

    @classmethod
    def from_dict(cls, dikt) -> 'Cyclo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Cyclo of this Cyclo.  # noqa: E501
        :rtype: Cyclo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cyclo(self) -> str:
        """Gets the cyclo of this Cyclo.


        :return: The cyclo of this Cyclo.
        :rtype: str
        """
        return self._cyclo

    @cyclo.setter
    def cyclo(self, cyclo: str):
        """Sets the cyclo of this Cyclo.


        :param cyclo: The cyclo of this Cyclo.
        :type cyclo: str
        """
        if cyclo is None:
            raise ValueError("Invalid value for `cyclo`, must not be `None`")  # noqa: E501

        self._cyclo = cyclo

    @property
    def name(self) -> str:
        """Gets the name of this Cyclo.


        :return: The name of this Cyclo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Cyclo.


        :param name: The name of this Cyclo.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def last_modified(self) -> datetime:
        """Gets the last_modified of this Cyclo.


        :return: The last_modified of this Cyclo.
        :rtype: datetime
        """
        return self._last_modified

    @last_modified.setter
    def last_modified(self, last_modified: datetime):
        """Sets the last_modified of this Cyclo.


        :param last_modified: The last_modified of this Cyclo.
        :type last_modified: datetime
        """
        if last_modified is None:
            raise ValueError("Invalid value for `last_modified`, must not be `None`")  # noqa: E501

        self._last_modified = last_modified

    @property
    def company(self) -> Company:
        """Gets the company of this Cyclo.


        :return: The company of this Cyclo.
        :rtype: Company
        """
        return self._company

    @company.setter
    def company(self, company: Company):
        """Sets the company of this Cyclo.


        :param company: The company of this Cyclo.
        :type company: Company
        """
        if company is None:
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company
