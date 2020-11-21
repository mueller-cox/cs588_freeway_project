"""
  This file initializes the flask app and contains the url routing information for each page in the app
"""

import flask
from index import Index
from insert import Add
from remove import Delete
from view_all import AllEntries

app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/volume/',
                 view_func=Volume.as_view('volume'),
                 methods=['POST'])

app.add_url_rule('/routes/',
                 view_func=Routes.as_view('routes'),
                 methods=['POST'])

app.add_url_rule('/update_station/',
                 view_func=UpdateStation.as_view('update_station'),
                 methods=['POST'])

app.add_url_rule('/speeds/',
                 view_func=Delete.as_view('speeds'),
                 methods=['POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
