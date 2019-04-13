import connexion
import six
from math import atan2, degrees
from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util
from flask import Response
from swagger_server.pose.pose_handler import extract_keypoints, get_image, get_poses
from flask import send_file
from ..physio_utils import load_config
import json
from ..physio_utils import load_config
from flask import send_file


CONNECTED_PART_NAMES = [
    ("leftHip", "leftShoulder"), ("leftElbow", "leftShoulder"),
    ("leftElbow", "leftWrist"), ("leftHip", "leftKnee"),
    ("leftKnee", "leftAnkle"), ("rightHip", "rightShoulder"),
    ("rightElbow", "rightShoulder"), ("rightElbow", "rightWrist"),
    ("rightHip", "rightKnee"), ("rightKnee", "rightAnkle"),
    ("leftShoulder", "rightShoulder"), ("leftHip", "rightHip")
]

def angle_between_matching_parts(reference_part, reading_part):
    """ get angle between reference part and reading part
        returns angle difference between reference and reading part"""

    # calculate angle of part inclination
    part_ref_angle = atan2(abs(reference_part[0][2] - reference_part[1][2]),
                           abs(reference_part[0][1] - reference_part[1][1]))

    part_read_angle = atan2(abs(reading_part[0][2] - reading_part[1][2]),
                            abs(reading_part[0][1] - reading_part[1][1]))

    angle_diff = part_ref_angle - part_read_angle
    return angle_diff


def compare_skeleton(skeleton_reference, skeleton_reading):
    """ iterate over all body parts and check the angle differences
        between reference and reading parts """
    skeleton_matched = {}
    for body_part in CONNECTED_PART_NAMES:
        reference_part = (skeleton_reference[body_part[0]],
                          skeleton_reference[body_part[1]])

        reading_part = (skeleton_reading[body_part[0]],
                        skeleton_reading[body_part[1]])
        angle_diff = angle_between_matching_parts(reference_part, reading_part)
        skeleton_matched[body_part[0] + ', ' + body_part[1]] = degrees(angle_diff)
    return skeleton_matched


def add_pose(file):  # noqa: E501
    """Add a new pose to the library

     # noqa: E501

    :param file: Picture showing the pose that needs to be added to the library
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """

    pose_uuid, _ = extract_keypoints(file)

    return Response('{"message":"Pose uploaded !", "id":"' + pose_uuid + '"}', status=201, mimetype='application/json')


def get_pose_by_id(poseId):  # noqa: E501
    """Find pose by ID

    Returns a single pose # noqa: E501

    :param poseId: ID of pose to return
    :type poseId: int

    :rtype: Tag
    """
    return 'do some magic!'


def api_poses_get():  # noqa: E501
    """Get all poses in the library

     # noqa: E501


    :rtype: None
    """

    poses = []
    for pose in get_poses():
        poses.append(pose.as_dict())
    json_string = json.dumps(poses)

    return Response(json_string, status=200, mimetype='application/json')


def validate_pose(poseId, file=None):  # noqa: E501
    """Validates a pose

    Validates a pose (sent in body) against the keypoints/skeleton in server # noqa: E501

    :param poseId: ID of pose to validate
    :type poseId: int
    :param file: image of the pose to validate
    :type file: werkzeug.datastructures.FileStorage

    :rtype: dict
    """

    # from patient
    _, keypoints = extract_keypoints(file, False)
    keypoints = json.loads(keypoints)
    image = get_image(poseId)
    # from doctor
    reference_keypoints = json.loads(image.keypoints)

    print(keypoints)
    print(reference_keypoints)

    matched_skeleton = compare_skeleton(reference_keypoints, keypoints)

    return matched_skeleton

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
    image = get_image(poseId)

    config = load_config("config.yml")
    pose_folder = model_dir = config["poseFolder"]
    filename = '{}/processed/{}{}'.format(pose_folder, poseId, image.extension)
    return send_file(filename, mimetype='image/png')