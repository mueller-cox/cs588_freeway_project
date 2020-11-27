from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import models


class Speeds(MethodView):
    def post(self):
        """

        """
        model = models.get_model()
