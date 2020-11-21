from flask import render_template
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
        return redirect(url_for('update_station'), results=results)
