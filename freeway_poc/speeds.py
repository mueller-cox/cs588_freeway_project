from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import models


class Speeds(MethodView):
    def post(self):
        """

        """
        model = models.get_model()
        low = request.form['low']
        high = request.form['high']

        result = model.count_low_high_speeds(low, high)

        return render_template('speeds.html', result=result, low=low, high=high)
