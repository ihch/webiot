import os
from collections import namedtuple
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime
from models import VigilancePosition, Sensor

app = Flask(__name__)
engine = create_engine(os.environ["DATABASE_URL"], echo=True)
db.Base.metadata.bind = engine
db.Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


@app.route('/')
def index():
    return "hoge"


@app.route('/test')
def test():
    return "Hello, World!"


@app.route('/add/vigilance_position', methods=['POST'])

def add_vigilance_position():
    data = VigilancePosition(
            request.form['discover_time'],
            float(request.form['latitude']),
            float(request.form['longitude'])
            )
    add_db(data)


@app.route('/add/sensor')
def add_sensor():
    data = Sensor(
            float(request.form['latitude']),
            float(request.form['longitude'])
            )
    add_db(data)



@app.route("/get/vigilance_position")
def get_vigilance_position():
    read = session.query(db.VigilancePosition).all()
    return repr(read)


@app.route("/get/sensor_position")
def get_sensor_position():
    read = session.query(db.Sensor).all()
    return repr(read)


def add_db(new_cls):
    db.session.add(new_cls)
    # db.session.flush()
    db.session.commit()


if __name__ == '__main__':
    app.run()

