# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.facility import Facility  # noqa: E501
from swagger_server.models.wip import Wip  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFacilityController(BaseTestCase):
    """FacilityController integration test stubs"""

    def test_add_facility(self):
        """Test case for add_facility

        Add Facility
        """
        body = Facility()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_wip(self):
        """Test case for add_wip

        Add Wip
        """
        body = Wip()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_facility(self):
        """Test case for get_facility

        Get Facility
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/facility',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_search_wip(self):
        """Test case for search_wip

        Get Wip
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 50)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/wip',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
