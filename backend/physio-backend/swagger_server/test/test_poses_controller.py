# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPosesController(BaseTestCase):
    """PosesController integration test stubs"""

    def test_add_pose(self):
        """Test case for add_pose

        Add a new pose to the library
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/poses',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_image_by_pose_id_and_index(self):
        """Test case for get_image_by_pose_id_and_index

        Find image for a pose by index
        """
        response = self.client.open(
            '/api/poses/{poseId}/images/raw/{index}'.format(poseId='poseId_example', index=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_image_with_skeleton_by_pose_id_and_index(self):
        """Test case for get_image_with_skeleton_by_pose_id_and_index

        Find image with skeleton for a pose by index
        """
        response = self.client.open(
            '/api/poses/{poseId}/images/skeleton/{index}'.format(poseId='poseId_example', index=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pose_by_id(self):
        """Test case for get_pose_by_id

        Find pose by ID
        """
        response = self.client.open(
            '/api/poses/{poseId}'.format(poseId='poseId_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_poses_get(self):
        """Test case for poses_get

        Get all poses in the library
        """
        response = self.client.open(
            '/api/poses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_pose(self):
        """Test case for validate_pose

        Validates a pose
        """
        data = dict(file=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/poses/{poseId}/check'.format(poseId='poseId_example'),
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
