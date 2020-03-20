from __future__ import absolute_import

from flask import json
import unittest
from filehash import FileHash
from swagger_server.controllers import default_controller
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.test import BaseTestCase
import os
from joblib import dump, load



class TestApi(BaseTestCase):

    def test_towdata_post(self):
        """Test case for towdata_post

        uploads data to train and predict over
        """


        file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/test/test-files/uploadTest.csv"
        retrieved_file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

        with open(file, 'r') as myfile:
            data = myfile.read()
            body = Body1(1, data)
        response = self.client.open(
            '/towdata',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')

        default_controller.towdata_post(body)
        md5hasher = FileHash("md5")

        expected_hash = md5hasher.hash_file(file)
        obtained_hash = md5hasher.hash_file(retrieved_file)

        self.assertEqual(expected_hash, obtained_hash)

    def test_towdata_put(self):
        """Test case for towdata_put

        Uploads live data to the server for predicition
        """

        update_file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/test/test-files/updateTest.csv"
        test_file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/test/test-files/appendedUpdateTest.csv"
        retrieved_file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

        with open(update_file, 'r') as myfile:
            data = myfile.read()
            body = Body1(1, data)
        response = self.client.open(
            '/towdata',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')

        default_controller.towdata_put(body.csv)
        md5hasher = FileHash("md5")

        expected_hash = md5hasher.hash_file(test_file)
        obtained_hash = md5hasher.hash_file(retrieved_file)
        self.assertEqual(expected_hash, obtained_hash)


    def test_towdata_delete(self):
        """Test case for towdata_delete

        Deletes the current prediction data
        """

        file = "C:/Users/21ale/Documents/CLASE/TFG/TFG-proyect/TFG-web/server/swagger_server/database/savefile.csv"

        response = self.client.open(
            '/towdata',
            method='DELETE')

        default_controller.towdata_delete()
        filesize = os.path.getsize(file)
        self.assertEqual(0, filesize)


    """def test_towdata_get(self):"""
    """Test case for towdata_get
    
    returns the prediction for the current dataset
        """
    """response = self.client.open(
        '/towdata',
        method='GET')


    expected_pred = load("path-to-expected-pred")
    retrieved_pred = default_controller.towdata_get()


    self.assertEqual(expected_pred, retrieved_pred)"""


if __name__ == '__main__':
    unittest.main()