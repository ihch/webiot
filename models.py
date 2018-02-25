from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String

Base = declarative_base()


class VigilancePosition(Base):
    __tablename__ = "vigilanceposition"

    id = Column(Integer, primary_key=True)
    discover_time = db.Column(db.String(100))
    latitude = db.Column(db.Float, primary_key=True)
    longitude = db.Column(db.Float, primary_key=True)

    def __init__(self, discover_time, latitude, longitude):
        self.discover_time = discover_time
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "Sensor(id={}, latitude={}, longitude={})".format(
self.id, self.latitude, self.longitude)


class Sensor(Base):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return "Sensor(id={}, latitude={}, longitude={})".format(
self.id, self.latitude, self.longitude)


