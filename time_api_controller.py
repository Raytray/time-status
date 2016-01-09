import timetracker_db

from bson import json_util
from datetime import datetime as dt
from flask import Flask, render_template, Response, request


app = Flask(__name__)


@app.route('/api/time-series')
def get_data():
    """Time series Handler. Returns the times collection."""
    times_collection = timetracker_db.get_times_collection()
    date_format = "%Y-%m-%d"
    start_date = request.args.get('start_date', '2015-01-01')
    end_date = request.args.get('end_date', '2999-01-01')
    start_date = dt.strptime(start_date, date_format)
    end_date = dt.strptime(end_date, date_format)

    data = json_util.dumps({
         'times': times_collection.find({
             'Start time': {'$gte': start_date},
             'End time': {'$lte': end_date}},
             {'_id': 0})
     }, default=json_util.default)
    response = Response(data, status=200, mimetype='application/json')
    return response


@app.route('/')
def index():
    """Serve the template."""
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
