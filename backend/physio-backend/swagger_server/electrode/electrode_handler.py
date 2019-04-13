#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
import os
from ..physio_utils import load_config
import numpy as np
import cv2
import json
from ..models.pose import Placement
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import gluoncv as gcv

config = load_config("config.yml")
db_folder = config["databaseDir"]
os.makedirs(db_folder, exist_ok=True)
engine = create_engine('sqlite:///' + db_folder +'/physio.sqlite')

# load the model once
net = gcv.model_zoo.get_model('ssd_512_mobilenet1.0_custom', classes=classes, pretrained_base=False)
net.load_parameters('neural_net')

# drop table at every boot of the application
table_name = "placements"
if not engine.dialect.has_table(engine.connect(), table_name):
    Placement.__table__.create(engine)

def extract_bounding_boxes(file, save_bbox=False):
    session = sessionmaker(bind=engine)()
    try:
        # create placement UUID
        placement_id = str(uuid.uuid4())

        # save image to disk
        filename, file_extension = os.path.splitext(file.filename)
        placement_folder = config["electrodesFolder"]
        filename_uuid = placement_id + file_extension
        if file:
            raw_folder = os.path.join(placement_folder, 'raw')
            fullPath = os.path.join(raw_folder, filename_uuid)
            os.makedirs(os.path.dirname(fullPath), exist_ok=True)
            file.save(fullPath)

        bbox_string = ""
        if save_bbox:
            # file.save consumed all the buffer we have to start form the beginning
            file.seek(0)
            img_str = file.read()
            file.close()
            # process the image
            nparr = np.fromstring(img_str, np.uint8)
            img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # get bounding boxes
            x, image = gcv.data.transforms.presets.ssd.transform_test(imgs=[img_np], max_size=512)
            cid, score, bbox = net(x)

            bbox_string = json.dumps({})
            
            #return best bboxes
            bboxes = [bbox[0][i] for i in range(len(score[0])) if score[0][i] > 0.7] # SLOW! NO TIME TO WRITE FAST

        index = 0 # fix index as long as we don't have video
        thumbnail_url = '/electrodes/{}/images/raw/{}'.format(placement_id, index)
        print('write to DB')
        placement = Placement(placementid=placement_id, name='', thumbnail=thumbnail_url, bbox=bbox_string)
        session.add(placement)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()
    return placement_id, bbox_string

def get_placement_image(placement, index):
    session = sessionmaker(bind=engine)()
    try:
        image = session.query(Placement).filter_by(placementid=placement, index=index).first()
        return image
    except Exception as e:
        print(e)
