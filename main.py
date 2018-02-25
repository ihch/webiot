import os
from collections import namedtuple
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import models
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
engine = create_engine(os.environ["DATABASE_URL"])
models.Base.metadata.bind = engine
models.Base.metadata.create_all(engine)
session = sessionmaker(bind=engine)()


@app.route('/')
def index():
    return "hoge"


@app.route('/test')
def test():
    return "Hello, World!"


@app.route('/add/vigilance_position', methods=['POST'])

def add_vigilance_position():
    data = models.VigilancePosition(
            request.form['discover_time'],
            float(request.form['latitude']),
            float(request.form['longitude'])
            )
    add_db(data)


@app.route('/add/sensor')
def add_sensor():
    data = models.Sensor(
            float(request.form['latitude']),
            float(request.form['longitude'])
            )
    add_db(data)



@app.route("/get/vigilance_position")
def get_vigilance_position():
    read = session.query(models.VigilancePosition).all()
    return repr(read)


@app.route("/get/sensor_position")
def get_sensor_position():
    read = session.query(models.Sensor).all()
    return repr(read)


def add_db(new_cls):
    db.session.add(new_cls)
    # db.session.flush()
    db.session.commit()


if __name__ == '__main__':
    app.run()

