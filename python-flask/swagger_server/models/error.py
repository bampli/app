# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Error(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=None, description: str=None, reason_phrase: str=None):  # noqa: E501
        """Error - a model defined in Swagger

        :param code: The code of this Error.  # noqa: E501
        :type code: int
        :param description: The description of this Error.  # noqa: E501
        :type description: str
        :param reason_phrase: The reason_phrase of this Error.  # noqa: E501
        :type reason_phrase: str
        """
        self.swagger_types = {
            'code': int,
            'description': str,
            'reason_phrase': str
        }

        self.attribute_map = {
            'code': 'code',
            'description': 'description',
            'reason_phrase': 'reasonPhrase'
        }
        self._code = code
        self._description = description
        self._reason_phrase = reason_phrase

    @classmethod
    def from_dict(cls, dikt) -> 'Error':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this Error.  # noqa: E501
        :rtype: Error
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this Error.


        :return: The code of this Error.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this Error.


        :param code: The code of this Error.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def description(self) -> str:
        """Gets the description of this Error.


        :return: The description of this Error.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Error.


        :param description: The description of this Error.
        :type description: str
        """

        self._description = description

    @property
    def reason_phrase(self) -> str:
        """Gets the reason_phrase of this Error.


        :return: The reason_phrase of this Error.
        :rtype: str
        """
        return self._reason_phrase

    @reason_phrase.setter
    def reason_phrase(self, reason_phrase: str):
        """Sets the reason_phrase of this Error.


        :param reason_phrase: The reason_phrase of this Error.
        :type reason_phrase: str
        """

        self._reason_phrase = reason_phrase