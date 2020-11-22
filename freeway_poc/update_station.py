from flask import render_template, request
from flask.views import MethodView
import models


class UpdateStation(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the form on the insert page;
        Redirect to index when completed.
        """

        model = models.get_model()
        results = model.update_station(request.form['station_name'], request.form['milemarker'])
        return render_template('update_station.html', results=results)
