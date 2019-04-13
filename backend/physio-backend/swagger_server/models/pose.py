from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, Sequence, String

Base = declarative_base()

class Pose(Base):
    __tablename__ = 'poses'
    id = Column(Integer, Sequence('pose_id_seq'), primary_key=True)
    poseid = Column(String(50))
    name = Column(String(50))
    thumbnail = Column(String(500))

    def __repr__(self):
        return "<Pose(poseid='%s', name='%s')>" % (self.poseid, self.name)

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, Sequence('image_id_seq'), primary_key=True)
    poseid = Column(String(50))
    keypoints = Column(String(500))
    index = Integer

    def __repr__(self):
        return "<Image(poseid='%s',index='%d')>" % (self.poseid, self.index)