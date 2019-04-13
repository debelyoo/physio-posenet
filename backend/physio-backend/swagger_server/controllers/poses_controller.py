import connexion
import six

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util
from flask import Response
from swagger_server.pose.pose_handler import extract_keypoints, get_image
from flask import send_file
from ..physio_utils import load_config

def add_pose(file):  # noqa: E501
    """Add a new pose to the library

     # noqa: E501

    :param file: Picture showing the pose that needs to be added to the library
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """

    pose_uuid, _ = extract_keypoints(file)

    return Response("{'message':'Pose uploaded !', 'id':'" + pose_uuid + "'}", status=201, mimetype='application/json')


def get_pose_by_id(poseId):  # noqa: E501
    """Find pose by ID

    Returns a single pose # noqa: E501

    :param poseId: ID of pose to return
    :type poseId: int

    :rtype: Tag
    """
    return 'do some magic!'


def poses_get():  # noqa: E501
    """Get all poses in the library

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def validate_pose(poseId, file=None):  # noqa: E501
    """Validates a pose

    Validates a pose (sent in body) against the keypoints/skeleton in server # noqa: E501

    :param poseId: ID of pose to validate
    :type poseId: int
    :param file: image of the pose to validate
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'

def get_image_by_pose_id_and_index(poseId, index):  # noqa: E501
    """Find image for a pose by index

    Returns a single image # noqa: E501

    :param poseId: ID of pose to return
    :type poseId: str
    :param index: index of the image
    :type index: int

    :rtype: None
    """

    image = get_image(poseId)

    config = load_config("config.yml")
    pose_folder = model_dir = config["poseFolder"]
    filename = '{}/raw/{}{}'.format(pose_folder, poseId, image.extension)
    return send_file(filename, mimetype='image/png')


def get_image_with_skeleton_by_pose_id_and_index(poseId, index):  # noqa: E501
    """Find image with skeleton for a pose by index

    Returns a single image with skeleton # noqa: E501

    :param poseId: ID of pose to return
    :type poseId: str
    :param index: index of the image
    :type index: int

    :rtype: None
    """
    return 'do some magic!'