import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from ..models.pose import Pose
from .posenet.load_model import load_posenet_model
from .posenet.utils import process_input, draw_skel_and_kp
from .posenet.decode import decode_multiple_poses
from .posenet.constants import PART_NAMES
from ..util import load_config
import json
import cv2
import numpy as np



config = load_config("config.yml")
model_dir = config["modelDir"]
db_folder = config["databaseDir"]
os.makedirs(db_folder, exist_ok=True)
engine = create_engine('sqlite:///' + db_folder +'/physio.sqlite')

# drop table at every boot of the application
table_name = "poses"
if not engine.dialect.has_table(engine.connect(), table_name):
    Pose.__table__.create(engine)

# load the posenet model
ts_session, output_stride, model_outputs = load_posenet_model(serve_dir=model_dir)

class Coordinate():
    def __init__(self, name, score, coordinates):
        self.name = name
        self.score = score
        self.coordinates = coordinates

def _get_scores(input_image):
    """
    
    :param input_image              : 
    :return: 
    """
    global output_stride, model_outputs, ts_session

        # feed the pre-processed image
    heatmaps_result, offsets_result, displacement_fwd_result, displacement_bwd_result = \
            ts_session.run(model_outputs, feed_dict={'image:0': input_image})

    # get the pose scores, key-point scores and their coordinates
    pose_scores, keypoint_scores, keypoint_coords = \
        decode_multiple_poses(heatmaps_result.squeeze(axis=0), offsets_result.squeeze(axis=0),
                              displacement_fwd_result.squeeze(axis=0), displacement_bwd_result.squeeze(axis=0),
                              output_stride=output_stride, max_pose_detections=10, min_pose_score=0.25)

    return pose_scores, keypoint_scores, keypoint_coords

def extract_keypoints(file, persist=True):
    session = sessionmaker(bind=engine)()
    try:
        # create pose UUID
        pose_uuid = str(uuid.uuid4())

        # save file to disk
        filename, file_extension = os.path.splitext(file.filename)
        pose_folder = "/tmp/physio/poses"
        filename_uuid = pose_uuid + file_extension
        if file and persist:
            fullPath = os.path.join(pose_folder, filename_uuid)
            os.makedirs(os.path.dirname(fullPath), exist_ok=True)
            file.save(fullPath)

        # file.save consumed all the buffer we have to start form the beginning
        file.seek(0)
        img_str = file.read()
        file.close()
        # process the image
        nparr = np.fromstring(img_str, np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        input_image, draw_image, output_scale = process_input(img_np, output_stride=output_stride)
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
            key_point_list = []
            for ki, (s, c) in enumerate(zip(keypoint_scores[0, :], keypoint_coords[0, :, :])):
                key_point_list.append(Coordinate(PART_NAMES[ki], s, list(c)).__dict__)

            json_string = json.dumps(key_point_list)
            # TODO: save the draw_image and the key-points
            if persist:
                pose = Pose(poseid=pose_uuid, keypoints=json_string)
                session.add(pose)
                session.commit()
    except Exception as e:
        print(e)
        if persist:
            session.rollback()

    return pose_uuid, json_string
