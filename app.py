import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Station = Base.classes.station 
Measure = Base.classes.measurement 

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation <br/>"
        f"/api/v1.0/station <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/<start> <br/>"
        f"/api/v1.0/<start>and<end> <br/>"

    )

@app.route("/api/v1.0/precipitation")
def names():

    session = Session(engine)

    twelevem2 = session.query(Measure.date,Measure.prcp).\
        filter(Measure.date >= '2016-06-15',Measure.date <= '2017-05-15').order_by(Measure.date).all()
    
    session.close()
    precipitation =[twelevem2]

    return jsonify(precipitation)

@app.route("/api/v1.0/station")
def station():

    session = Session(engine)

    stat = session.query(Station.name, Station.elevation).all()
        
    session.close()

    return jsonify(stat)

@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    stmt1 = session.query(Measure.date,Measure.tobs).\
        filter(Measure.date >= '2016-08-23',Measure.date <= '2017-08-23').\
            order_by(Measure.date).all()
        
    session.close()
    tob= [stmt1]

    return jsonify(tob)
    

if __name__ == '__main__':
    app.run(debug=True)


