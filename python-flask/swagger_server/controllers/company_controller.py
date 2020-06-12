import connexion
import six

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server import util


def add_company(body=None):  # noqa: E501
    """Add Company

    Adds a Company to the system # noqa: E501

    :param body: Company item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Company.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_product(body=None):  # noqa: E501
    """Add Product

    Adds a Product to the system # noqa: E501

    :param body: Product item to add
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Product.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_company(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Company

    Search for an available Company in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Company]
    """
    return 'do some magic!'


def get_product(search_string=None, skip=None, limit=None):  # noqa: E501
    """Get Product

    Search for an available Product in the system  # noqa: E501

    :param search_string: pass an optional search string for looking up inventory
    :type search_string: str
    :param skip: number of records to skip for pagination
    :type skip: int
    :param limit: maximum number of records to return
    :type limit: int

    :rtype: List[Product]
    """
    return 'do some magic!'
