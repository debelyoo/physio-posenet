import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uuid
from ..models.pose import Pose

engine = create_engine('sqlite:////Users/jean.rossier/tools/arkathon/physio-posenet/db/physio.sqlite')

# drop table at every boot of the application
Pose.__table__.drop(engine)
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

        pose = Pose(uuid=pose_uuid, keypoints='x,x,x')
        session.add(pose)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

    return uuid