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
        return '<Ufo %r>' % (self.id)
    
@app.route("/")
def home():
    return render_template("index.html")