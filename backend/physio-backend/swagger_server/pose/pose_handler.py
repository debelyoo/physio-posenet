import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from ..models.pose import Pose

db_folder = os.path.realpath('..') + "/db"
os.makedirs(db_folder, exist_ok=True)
engine = create_engine('sqlite:///'+ db_folder +'/physio.sqlite')

# drop table at every boot of the application
table_name = "poses"
if not engine.dialect.has_table(engine.connect(), table_name):
    Pose.__table__.create(engine)

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

        # TODO - extract keypoints

        # persist in DB
        pose = Pose(uuid=pose_uuid, keypoints='x,x,x')
        session.add(pose)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

    return uuid