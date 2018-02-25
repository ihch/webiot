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
            request.form['youtube_id']
            )
    add_db(data)
    return "OK"


@app.route('/add/sensor', methods=['POST'])
def add_sensor():
    data = models.Sensor(
            float(request.form['latitude']),
            float(request.form['longitude'])
            )
    add_db(data)
    return "OK"


@app.route("/get/vigilance_position", methods=['GET'])
def get_vigilance_position():
    read = session.query(models.VigilancePosition).all()
    # return repr(read)
    res = [trans_dict_vigilanse_position(vp) for vp in read]
    return jsonify(results=res)


@app.route("/get/sensor_position", methods=['GET'])
def get_sensor_position():
    read = session.query(models.Sensor).all()
    # return repr(read)
    res = [trans_dict_sensor(s) for s in read]
    return jsonify(results=res)


def add_db(new_cls):
    session.add(new_cls)
    # db.session.flush()
    session.commit()


def trans_dict_vigilanse_position(vp):
    res = dict()
    res['discover_time'] = vp.dicover_time
    res['latitude'] = vp.latitude
    res['longitude'] = vp.longitude
    return res


def trans_dict_sensor(s):
    res = dict()
    res['latitude'] = s.latitude
    res['longitude'] = s.longitude
    return res


if __name__ == '__main__':
    app.run()

