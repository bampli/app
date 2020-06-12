# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.company import Company  # noqa: E501
from swagger_server.models.product import Product  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCompanyController(BaseTestCase):
    """CompanyController integration test stubs"""

    def test_add_company(self):
        """Test case for add_company

        Add Company
        """
        body = Company()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_product(self):
        """Test case for add_product

        Add Product
        """
        body = Product()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_company(self):
        """Test case for get_company

        Get Company
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/company',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_product(self):
        """Test case for get_product

        Get Product
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/product',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
