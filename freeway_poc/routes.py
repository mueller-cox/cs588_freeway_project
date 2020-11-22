from flask import render_template, request
from flask.views import MethodView
import models


class Routes(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the path_finding form from index.html;
        Redirect to routes template, passing in list of stations on path
        """

        model = models.get_model()
        start = request.form['station_start']
        end = request.form['station_end']
        results = []
        direction = request.form['direction']
        list_results = model.find_route(direction,start, end)
      

        for result in list_results:
            results.append({result['locationtext']:result['milepost']})


        return render_template('routes.html', results=results, start=start, end=end)
