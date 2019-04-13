import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from ..models.pose import Pose
from .posenet.load_model import load_posenet_model
from .posenet.utils import process_input, draw_skel_and_kp
from .posenet.decode import decode_multiple_poses
from .posenet.constants import PART_NAMES
import tensorflow as tf

db_folder = os.path.realpath('..') + "/db"
os.makedirs(db_folder, exist_ok=True)
engine = create_engine('sqlite:///'+ db_folder +'/physio.sqlite')

# drop table at every boot of the application
table_name = "poses"
if not engine.dialect.has_table(engine.connect(), table_name):
    Pose.__table__.create(engine)

# load the posenet model
output_stride, model_outputs = load_posenet_model()


def _get_scores(input_image):
    """
    
    :param input_image              : 
    :return: 
    """
    global output_stride, model_outputs

    with tf.Session() as sess:
        # feed the pre-processed image
        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = \
            sess.run(model_outputs, feed_dict={'image:0': input_image})

    # get the pose scores, key-point scores and their coordinates
    pose_scores, keypoint_scores, keypoint_coords = \
        decode_multiple_poses(heatmaps_result.squeeze(axis=0), offsets_result.squeeze(axis=0),
                              displacement_fwd_result.squeeze(axis=0), displacement_bwd_result.squeeze(axis=0),
                              output_stride=output_stride, max_pose_detections=10, min_pose_score=0.25)

    return pose_scores, keypoint_scores, keypoint_coords


# load the posenet model
output_stride, model_outputs = load_posenet_model()


def _get_scores(input_image):
    """
    
    :param input_image              : 
    :return: 
    """
    global output_stride, model_outputs

    with tf.Session() as sess:
        # feed the pre-processed image
        heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = \
            sess.run(model_outputs, feed_dict={'image:0': input_image})

    # get the pose scores, key-point scores and their coordinates
    pose_scores, keypoint_scores, keypoint_coords = \
        decode_multiple_poses(heatmaps_result.squeeze(axis=0), offsets_result.squeeze(axis=0),
                              displacement_fwd_result.squeeze(axis=0), displacement_bwd_result.squeeze(axis=0),
                              output_stride=output_stride, max_pose_detections=10, min_pose_score=0.25)

    return pose_scores, keypoint_scores, keypoint_coords


def save_pose(file):
    session = sessionmaker(bind=engine)()
    try:
        # create pose UUID
        pose_uuid = str(uuid.uuid4())

        # save file to disk
        pose_folder = "/tmp/physio/poses"
        filename = pose_uuid + ".png"
        if file:
            fullPath = os.path.join(pose_folder, filename)
            os.makedirs(os.path.dirname(fullPath), exist_ok=True)
            file.save(fullPath)

        # process the image
        input_image, draw_image, output_scale = process_input(file, output_stride=output_stride)
        # get the scores and the coordinates
        pose_scores, keypoint_scores, keypoint_coords = _get_scores(input_image)
        # scale the coordinates
        keypoint_coords *= output_scale

        # at least one pose should be present in the image
        if len(pose_scores) > 0:
            # draw the image with the key-points and the skeleton
            draw_image = draw_skel_and_kp(draw_image, pose_scores, keypoint_scores, keypoint_coords,
                                          min_pose_score=0.25, min_part_score=0.25)

            # save the name of the key-point, its score and coordinates
            key_point_tuples = []
            for ki, (s, c) in enumerate(zip(keypoint_scores[0, :], keypoint_coords[0, :, :])):
                key_point_tuples.append((PART_NAMES[ki], s, c))

            # TODO: save the draw_image and the key-points
            pose = Pose(uuid=pose_uuid, keypoints='x,x,x')
            session.add(pose)
            session.commit()
    except Exception as e:
        print(e)
        session.rollback()

    return uuid
