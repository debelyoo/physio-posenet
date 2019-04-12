import connexion
import six

from swagger_server.models.tag import Tag  # noqa: E501
from swagger_server import util
from flask import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from ..models.pose import Pose

engine = create_engine('sqlite:////Users/jean.rossier/tools/arkathon/physio-posenet/db/physio.sqlite')
Pose.__table__.create(engine)

def add_pose(file):  # noqa: E501
    """Add a new pose to the library

     # noqa: E501

    :param file: Picture showing the pose that needs to be added to the library
    :type file: werkzeug.datastructures.FileStorage

    :rtype: None
    """

    session = sessionmaker(bind=engine)()
    try:
        pose_uuid = str(uuid.uuid4())
        pose = Pose(uuid=pose_uuid, keypoints='x,x,x')
        session.add(pose)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

    return Response("{'message':'Pose uploaded !'}", status=201, mimetype='application/json')


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
