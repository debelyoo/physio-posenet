from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, Sequence, String

Base = declarative_base()

class Pose(Base):
    __tablename__ = 'poses'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    uuid = Column(String(50))
    keypoints = Column(String(50))

    def __repr__(self):
        return "<User(uuid='%s')>" % (self.uuid)