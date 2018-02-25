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
            request.args.get('discover_time'),
            float(request.args.get('latitude')),
            float(request.args.get('longitude'))
            )
    add_db(data)
    return "OK"


@app.route('/add/sensor', methods=['POST'])
def add_sensor():
    print(request.args.get('latitude'))
    print(request.args.get('longitude'))
    print("form")
    print(request.form)
    print("data")
    print(request.data)
    data = models.Sensor(
            float(request.args.get('latitude')),
            float(request.args.get('longitude'))
            )
    add_db(data)
    return "OK"


@app.route("/get/vigilance_position", methods=['GET'])
def get_vigilance_position():
    read = session.query(models.VigilancePosition).all()
    return repr(read)


@app.route("/get/sensor_position", methods=['GET'])
def get_sensor_position():
    read = session.query(models.Sensor).all()
    return repr(read)


def add_db(new_cls):
    db.session.add(new_cls)
    # db.session.flush()
    db.session.commit()


if __name__ == '__main__':
    app.run()

