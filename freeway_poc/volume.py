from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import models


class Volume(MethodView):
    def post(self):
        """
        
        """
        model = models.get_model()
        station = request.form['station_name']
        year = request.form['year']
        day = request.form['day']
        month = request.form['month']

        result = model.volume_by_station(station, year, day, month)

        return render_template('volume.html', result=result, station=station, year=year, day=day, month=month)

