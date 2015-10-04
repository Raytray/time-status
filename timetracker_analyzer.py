import csv

from datetime import datetime as dt
from pprint import pprint


def get_month_year(date):
    """Return the month's full name  and the year of the date.
    For analyzing data, we will be taking the date something started
    as the month it is in.
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    date = dt.strptime(date, date_format)
    key_format = "%B - %Y"
    return date.strftime(key_format)


def get_timedelta(start_time, end_time):
    """Return end time minus start time.
    Takes in start and end time as strings in this format: %Y-%m-%d %H:%M:%S
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    start_time = dt.strptime(start_time, date_format)
    end_time = dt.strptime(end_time, date_format)

    if (end_time - start_time).total_seconds() < 0:
        raise ValueError("Start Time must be before End Time")

    return end_time - start_time


def analyze_data(filename):
    """For a given file, analyze the file and return a dictionary object
    composed of months, tasks within that month, and total time for each task.
    {Month Year: [{name: name, count: activity-count, time: timedelta}]}
    """
    # For the given date, find the correct month
    # call total up tasks
    # Add it to the month total for that task
    # If no end time, add it as an activity
    with open(filename, 'r') as data:
        reader = csv.DictReader(data,
                                fieldnames=['task', 'start_time', 'end_time'])
        for row in reader:
            month_year = get_month_year(row.start_time)
            results[month_year]


analyze_data('timetracker-2015-10-03-19-30-48.csv')
