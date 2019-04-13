# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestElectrodesController(BaseTestCase):
    """ElectrodesController integration test stubs"""

    def test_add_electrode(self):
        """Test case for add_electrode

        Add a new electrode to the library
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/electrodes',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_electrodes_get(self):
        """Test case for electrodes_get

        Get all electrodes in the library
        """
        response = self.client.open(
            '/api/electrodes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_image_by_electrode_id_and_index(self):
        """Test case for get_image_by_electrode_id_and_index

        Find image for an electrode by index
        """
        response = self.client.open(
            '/api/electrodes/{electrodeId}/images/raw/{index}'.format(electrodeId='electrodeId_example', index=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_electrodes(self):
        """Test case for validate_electrodes

        Validates electrodes position
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/electrodes/{electrodeId}/check'.format(electrodeId='electrodeId_example'),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
