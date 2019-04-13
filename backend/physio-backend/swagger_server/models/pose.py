from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, Sequence, String

Base = declarative_base()

class Pose(Base):
    __tablename__ = 'poses'
    id = Column(Integer, Sequence('pose_id_seq'), primary_key=True)
    poseid = Column(String(50))
    name = Column(String(50))
    thumbnail = Column(String(500))
    thumbnail_with_skeleton = Column(String(500))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Pose(poseid='%s', name='%s')>" % (self.poseid, self.name)

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, Sequence('image_id_seq'), primary_key=True)
    poseid = Column(String(50))
    extension = Column(String(50))
    keypoints = Column(String(500))
    index = Integer

    def __repr__(self):
        return "<Image(poseid='%s',index='%d')>" % (self.poseid, self.index)

class Placement(Base):
    __tablename__ = 'placements'
    id = Column(Integer, Sequence('placement_id_seq'), primary_key=True)
    placementid = Column(String(50))
    bbox = Column(String(500))
    index = Integer

    def __repr__(self):
        return "<Placement(placementid='%s',index='%d')>" % (self.placementid, self.index)