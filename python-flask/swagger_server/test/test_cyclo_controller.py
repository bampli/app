# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cyclo import Cyclo  # noqa: E501
from swagger_server.models.stage import Stage  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCycloController(BaseTestCase):
    """CycloController integration test stubs"""

    def test_add_cyclo(self):
        """Test case for add_cyclo

        Add Cyclo
        """
        body = Cyclo()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_stage(self):
        """Test case for add_stage

        Add Stage
        """
        body = Stage()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_task(self):
        """Test case for add_task

        Add Task
        """
        body = Task()
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cyclo(self):
        """Test case for get_cyclo

        Get Cyclo
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/cyclo',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stage(self):
        """Test case for get_stage

        Get Stage
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/stage',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task(self):
        """Test case for get_task

        Get Task
        """
        query_string = [('search_string', 'search_string_example'),
                        ('skip', 1),
                        ('limit', 10)]
        response = self.client.open(
            '/motta/bampli/1.0.0-oas3/task',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
