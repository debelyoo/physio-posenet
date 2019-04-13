# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestFrontController(BaseTestCase):
    """FrontController integration test stubs"""

    def test_front_get(self):
        """Test case for front_get

        Get the home page
        """
        response = self.client.open(
            '/api/front',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
