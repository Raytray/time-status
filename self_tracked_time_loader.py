import csv

from datetime import datetime as dt
from pymongo import MongoClient


def get_timedelta(start_time, end_time):
    """Return end time minus start time.
    Takes in start and end time as strings in this format: %Y-%m-%d %H:%M:%S
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    start_time = dt.strptime(start_time, date_format)
    end_time = dt.strptime(end_time, date_format)

    if (end_time - start_time).total_seconds() <= 0:
        raise ValueError("Start Time must be before End Time")

    return (end_time - start_time).total_seconds()


def load_data(filename):
    """For a given file, load the data into MongoDb"""
    # TODO: Move mongo client information out
    # Set up mongo client
    client = MongoClient()
    db = client.timetracker
    collection = db.times

    # Loop through csv and create a array of documents
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        documents = []
        for row in reader:
            try:
                row['seconds'] = get_timedelta(row['Start time'], row['End time'])
            except ValueError:
                continue

            documents.append(row)

    # Insert everything
    collection.insert(documents)
