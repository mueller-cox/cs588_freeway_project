from flask import render_template
from flask.views import MethodView


class Routes(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the path_finding form from index.html;
        Redirect to routes template, passing in list of stations on path
        """

        model = models.get_model()
        start = request.form['station_start']
        end = request.form['station_end']
        results = model.find_route(start, end)
        return render_template('routes.html', results=results, start=start, end=end)
