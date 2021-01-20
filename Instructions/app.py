
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()
Base = automap_base()
Base.prepare(engine, reflect=True

Measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

# Close Session
session.close()

# Create an app
app = Flask(__name__)

# Flask Routes
# Define what to do when user hits the index route
@app.route("/")
def Welcome():
    return(
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
