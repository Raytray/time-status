import re
import timetracker_db

from bson import json_util
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from flask import Flask, render_template, Response, request
from flask.ext.bower import Bower

import pprint

app = Flask(__name__)
Bower(app)


def sanitize_match_group(group):
    """Sanitize match group results so that default result is 0, not None.
    The group result must be a int not a string.

    :param group: Match group from regex package.
    :type group: str
    :rtype: int"""
    if group is None:
        return 0
    return int(group)


def get_data_parameters(args):
    """Converts url parameters of category, start date, end date and period
    to be a mongo parameter search.

    Category is not validated for a filtered set of categories.
    Start date is the start of the requested data.
    End date is the end of the reqested data.
    Period is measured in years, months, days in the format of 1y2m3d
        for retrieving data in the past 1 year, 2 months and 3 days.
        Period will override start."""
    date_format = "%Y-%m-%d"

    parameters = {}
    category = args.get('category')
    if category is not None:
        parameters['Category'] = category

    start_date = args.get('start_date')
    if start_date is not None:
        start_date = datetime.strptime(start_date, date_format)
        parameters['Start time'] = {'$gte': start_date}

    end_date = args.get('end_date')
    period = args.get('period')
    if period is not None:
        parameters['Start time'] = {'$gte': handle_period(period,
                                                                   end_date)}

    if end_date is not None:
        end_date = datetime.strptime(end_date, date_format)
        parameters['End time'] = {'$lte': end_date}

    return parameters


def handle_period(period, end_date=None):
    """Returns the datetime object matching against the requested period"""
    matches = re.match(
        r"((?P<years>[\d]+)y)*((?P<months>[\d]+)m)*((?P<days>[\d]+)d)*",
        period.lower())

    years = matches.group('years')
    months = matches.group('months')
    days = matches.group('days')

    years = sanitize_match_group(years)
    months = sanitize_match_group(months)
    days = sanitize_match_group(days)

    if end_date is None:
        end_date = date.today()

    period = end_date - relativedelta(years=years,
                                          months=months,
                                          days=days)
    return datetime.combine(period, datetime.min.time())


def convert_seconds_to_hours(seconds):
    return float("{0:.2f}".format(seconds / 60 / 60.0))


@app.route('/api/time-series')
def get_data():
    """Time series Handler. Returns the times collection."""
    times_collection = timetracker_db.get_times_collection()

    status = 200
    try:
        parameters = get_data_parameters(request.args)
        data = json_util.dumps({
            'times': times_collection.find(
                parameters,
                {'_id': 0})
        }, default=json_util.default)
    except ValueError as err:
        data = json_util.dumps({"message": err.args,
                "request": request.args})
        status = 400

    response = Response(data, status=status, mimetype='application/json')
    return response


@app.route('/api/time-series/month')
def get_month_data():
    """Time series Handler. Returns the times collection."""

    last_data_date = timetracker_db.get_config_collection().find_one(
        {'last_date_type': 'self_time'})['date']

    times_collection = timetracker_db.get_times_collection()
    status = 200
    try:
        results = {}

        results['period'] = {
            'end_date': last_data_date,
            'period2_start_date': handle_period('2m', end_date=last_data_date),
            'period_start_date': handle_period('1m', end_date=last_data_date)
        }

        categories = request.values.getlist('category')
        for category in categories:
            parameters = {}
            parameters['Category'] = category
            parameters['Start time'] = {
                '$gte': handle_period('1m', end_date=last_data_date)
            }

            period1_seconds = sum([x['seconds'] for x in
                                  list(times_collection.find(
                                      parameters, {'_id': 0}))])

            parameters['Start time'] = {
                '$gte': handle_period('2m', end_date=last_data_date)
            }
            parameters['End time'] = {
                '$lt': handle_period('1m', end_date=last_data_date)
            }

            period2_seconds = sum([x['seconds'] for x in
                                  list(times_collection.find(
                                      parameters, {'_id': 0}))])

            results[category] = {
                'previous': convert_seconds_to_hours(period2_seconds),
                'current': convert_seconds_to_hours(period1_seconds)
            }

        results = json_util.dumps(results)
    except ValueError as err:
        data = json_util.dumps({"message": err.args,
                "request": request.args})
        status = 400

    response = Response(results, status=status, mimetype='application/json')
    return response


@app.route('/')
def index():
    """Serve the template."""
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
