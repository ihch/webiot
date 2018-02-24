import os
from collections import namedtuple
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


class DiscoverInosisi(db.Model):
    discover_time = db.Column(Integer, primary_key = True)
    position_x = db.Column(Integer, primary_key=True)
    position_y = db.Column(Integer, primary_key=True)

    def __init__(self, discover_time, position_x, position_y):
        self.discover_time = discover_time
        self.position_x = position_x
        self.position_y = position_y

    # def __repr__(self):
    #     return "{}\n(x, y): ({}, {})".format(self.discover_time, self.position_x, self.position_y)


@app.route('/test')
def test():
    return "Hello, World!"


@app.route('/post/data', methods=['POST'])
def data():
    d = DiscoverInosisi(request.form['discover_time'], request.form['position_x'], request.form['position_y'])
    db.session.add(
            d
            )
    db.session.commit()
    print(d)


if __name__ == '__main__':
    app.run()

