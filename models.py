from sqlalchemy import Column, Integer, String


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class DiscoverInosisi(db.Model):
    discover_time = Column(Integer, primary_key=True)
    position = Column(Position, primary_key=True)
