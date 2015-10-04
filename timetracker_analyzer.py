import csv

from datetime import datetime as dt


def get_month_year(date):
    pass


def get_time_delta(start_time, end_time):
    """Return end time minus start time."""
    # Handle negative values
    # Handle none values
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
    with open(filename) as data:
        reader = csv.reader(data)
        for row in data:
            pass


analyze_data('timetracker-2015-10-03-19-30-48.csv')
