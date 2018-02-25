from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


class VigilancePosition(Base):
    __tablename__ = "vigilanceposition"

    id = Column(Integer)
    discover_time = Column(String(100))
    latitude = Column(Float, primary_key=True)
    longitude = Column(Float, primary_key=True)
    youtube_id = Column(String, primary_key=True)

    def __init__(self, discover_time, latitude, longitude, youtube_id):
        self.discover_time = discover_time
        self.latitude = latitude
        self.longitude = longitude
        self.youtube_id = youtube_id

    def __repr__(self):
        return "Sensor(id={}, latitude={}, longitude={}, youtube_id)".format(
                self.id, self.latitude, self.longitude, self.youtube_id)


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "Sensor(id={}, latitude={}, longitude={})".format(
self.id, self.latitude, self.longitude)


