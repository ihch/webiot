import os
from collections import namedtuple
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, DateTime
from models import VigilancePosition, Sensor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app, echo=True)


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


def add_db(new_cls):
    db.session.add(new_cls)
    # db.session.flush()
    db.session.commit()


if __name__ == '__main__':
    app.run()

