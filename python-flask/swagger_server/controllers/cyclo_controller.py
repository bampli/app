import connexion
import six

from swagger_server.models.cyclo import Cyclo  # noqa: E501
from swagger_server.models.stage import Stage  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server import util


def add_cyclo(body=None):  # noqa: E501
    """Add Cyclo

    Adds a Cyclo to the system # noqa: E501

    :param body: Cyclo item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Cyclo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_stage(body=None):  # noqa: E501
    """Add Stage

    Adds a Stage to the system # noqa: E501

    :param body: Stage item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Stage.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_task(body=None):  # noqa: E501
    """Add Task

    Adds a Task to the system # noqa: E501

    :param body: Task item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Task.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_cyclo(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Cyclo

    Search for an available Cyclo in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Cyclo]
    """
    return 'do some magic!'


def get_stage(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Stage

    Search for an available Stage in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Stage]
    """
    return 'do some magic!'


def get_task(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Task

    Search for an available Task in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Task]
    """
    return 'do some magic!'
