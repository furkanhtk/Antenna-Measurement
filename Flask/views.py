from datetime import datetime
from flask import *
import models
from database import Base,Parameters

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day=today)


def Measurement_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("Measurement.html", day=today)


def parameters_page():
    engine = create_engine('sqlite:///parameters_database.db', connect_args={"check_same_thread": False})
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == "GET":
        parameters_list = models.get_parameters(session)
        return render_template("parameters.html", parameters=parameters_list)
    elif request.form.get('Add') == 'Add':
        form_frequency = request.form["frequency"]
        form_power = request.form["power"]
        models.add_parameter(session,form_frequency,form_power)
        return redirect(url_for("parameters_page"))
    elif request.form.get('Delete') == 'Delete':
        form_parameter_ids = request.form.getlist("parameter_ids")
        for form_parameter_id in form_parameter_ids:
            models.delete_parameter(session, form_parameter_id)
        return redirect(url_for("parameters_page"))
    else:
        return redirect(url_for("parameters_page"))



