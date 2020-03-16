# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_towdata_delete(self):
        """Test case for towdata_delete

        Deletes the current prediction data
        """
        response = self.client.open(
            '/towdata',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_towdata_get(self):
        """Test case for towdata_get

        returns the prediction for the current dataset
        """
        response = self.client.open(
            '/towdata',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_towdata_post(self):
        """Test case for towdata_post

        uploads data to train and predict over
        """
        body = Body1()
        response = self.client.open(
            '/towdata',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_towdata_put(self):
        """Test case for towdata_put

        Uploads live data to the server for predicition
        """
        body = Body()
        response = self.client.open(
            '/towdata',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
