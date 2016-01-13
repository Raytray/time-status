import timetracker_db

from bson import json_util
from datetime import datetime as dt
from flask import Flask, render_template, Response, request


app = Flask(__name__)


def get_data_parameters(args):
    date_format = "%Y-%m-%d"
    start_date = args.get('start_date')

    parameters = {}
    if start_date is not None:
        start_date = dt.strptime(start_date, date_format)
        parameters['Start time'] = {'$gte': start_date}

    end_date = args.get('end_date')
    if end_date is not None:
        end_date = dt.strptime(end_date, date_format)
        parameters['End time'] = {'$lte': end_date}

    category = args.get('category')
    if category is not None:
        parameters['Category'] = category

    return parameters


@app.route('/api/time-series')
def get_data():
    """Time series Handler. Returns the times collection."""
    times_collection = timetracker_db.get_times_collection()

    parameters = get_data_parameters(request.args)

    data = json_util.dumps({
         'times': times_collection.find(
             parameters,
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
