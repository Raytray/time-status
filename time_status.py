import csv

from datetime import datetime as dt
from pymongo import MongoClient


client = MongoClient()


def get_config_collection():
    """Return the collection used for configuration"""
    return client["timetracker"]["config"]


def get_times_collection():
    """Return the collection used for times"""
    return client["timetracker"]["times"]


def get_timedelta(start_time, end_time):
    """Return end time minus start time.
    Takes in start and end time as datetime objects
    """
    if (end_time - start_time).total_seconds() <= 0:
        raise ValueError("Start Time must be before End Time")

    return (end_time - start_time).total_seconds()


def load_data(filename):
    """For a given file, load the data into MongoDb
    format of the file is...."""
    # Get last start date for self timed data
    config_collection = get_config_collection()
    self_time_filter = {'last_date_type': 'self_time'}
    last_date_document = config_collection.find_one(self_time_filter)
    if last_date_document is None:
        last_date_document = self_time_filter
        last_date_document['date'] = dt(2000, 1, 1)

    # Loop through csv and create a array of documents
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        documents = []
        for row in reader:
            try:
                # Make datetime objects
                date_format = "%Y-%m-%d %H:%M:%S"
                start_time = dt.strptime(row['Start time'], date_format)
                end_time = dt.strptime(row['End time'], date_format)

                # If start_time is within last starttime, don't add.
                if last_date_document['date'] >= start_time:
                    continue

                # Get seconds
                row['seconds'] = get_timedelta(start_time, end_time)

                # Set last start datetime
                if start_time > last_date_document['date']:
                    last_date_document['date'] = start_time
            except ValueError:
                continue

            documents.append(row)

    # Insert everything
    if (len(documents) > 0):
        times_collection = get_times_collection()
        times_collection.insert(documents)
        config_collection.find_one_and_replace(self_time_filter,
                                               last_date_document,
                                               upsert=True)

if __name__ == "__main__":
    load_data("testdata.csv")
