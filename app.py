# import necessary libraries
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/test.sqlite"

db = SQLAlchemy(app)


class Ufo(db.Model):
    __tablename__ = 'ufo'

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    date_time = db.Column(db.DateTime)
    shape = db.Column(db.String)
    duration = db.Column(db.String)
    text = db.Column(db.String)
    city_latitude= db.Column(db.Float)
    city_longitude = db.Column(db.Float)


    def __repr__(self):
        return '<Ufo%r>' % (self.name)



# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


# create route that returns data for plotting
@app.route("/api/city")
def getCity():
    results = db.session.query(Ufo.city, func.count(Ufo.city)).group_by(Ufo.city).all()

    ufo_city = [result[0] for result in results]
    count = results.count()

    trace = {
        "x": ufo_city,
        "y": count,
        "type": "bar"
    }

    return jsonify(trace)

@app.route("/api/state")
def getState():
    results = db.session.query(Ufo.state, func.count(Ufo.state)).group_by(Ufo.state).all()

    ufo_state = [result[0] for result in results]
    count = results.count()

    trace = {
        "x": ufo_state,
        "y": count,
        "type": "bar"
    }

    return jsonify(trace)

@app.route("/api/state")
def getState():
    results = db.session.query(Ufo.state, func.count(Ufo.state)).group_by(Ufo.state).all()

    ufo_state = [result[0] for result in results]
    count = results.count()

    trace = {
        "x": ufo_state,
        "y": count,
        "type": "bar"
    }

    return jsonify(trace)




if __name__ == "__main__":
    app.run()