from flask import render_template
from flask.views import MethodView


class Index(MethodView):
    def get(self):
        """
        when get request is issued for Index renders index.html template
        :return: template to render
        """
        return render_template('index.html')
