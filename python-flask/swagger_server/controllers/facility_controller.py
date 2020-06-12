import connexion
import six

from swagger_server.models.facility import Facility  # noqa: E501
from swagger_server.models.wip import Wip  # noqa: E501
from swagger_server import util


def add_facility(body=None):  # noqa: E501
    """Add Facility

    Adds a Facility to the system # noqa: E501

    :param body: Facility item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Facility.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_wip(body=None):  # noqa: E501
    """Add Wip

    Adds a Wip to the system # noqa: E501

    :param body: Wip item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Wip.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_facility(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Facility

    Search for an available Facility in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Facility]
    """
    return 'do some magic!'


def search_wip(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Wip

    Search for an available Wip in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up wip
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Wip]
    """
    return 'do some magic!'
