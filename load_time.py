import argparse
import csv
import timetracker_db

from datetime import datetime as dt


def get_timedelta(start_time, end_time):
    """Returns datetime.timedelta of start_time - end_time

    :param start_time: Start time of delta.
    :type start_time: datetime.datetime
    :param end_time: End time of delta.
    :type end_time: datetime.datetime
    :rtype: datetime.timedelta
    """
    if (end_time - start_time).total_seconds() <= 0:
        raise ValueError("Start Time must be before End Time")

    return (end_time - start_time).total_seconds()


def load_data(filename):
    """For a given file, load the data into MongoDb
    Example format of the file is
    Category,Start time,End time
    Screen,2015-12-01 19:21:41,2015-12-01 19:21:43

    :param filename: string path of the file to load.
    """
    # Get last start date for self timed data
    config_collection = timetracker_db.get_config_collection()
    self_time_filter = {'last_date_type': 'self_time'}
    last_date_document = config_collection.find_one(self_time_filter)
    if last_date_document is None:
        last_date_document = self_time_filter
        last_date_document['date'] = dt(2000, 1, 1)

    # Temporary variable to figure out latest date
    max_start_date = last_date_document['date']

    # Loop through csv and create a array of documents
    with open(filename, 'r') as data:
        reader = csv.DictReader(data)
        documents = []
        for row in reader:
            try:
                # Make datetime objects
                date_format = "%Y-%m-%d %H:%M:%S"
                row['Start time'] = dt.strptime(row['Start time'], date_format)
                row['End time'] = dt.strptime(row['End time'], date_format)

                # If row['Start time'] is within last starttime, don't add.
                if last_date_document['date'] >= row['Start time']:
                    continue
                elif max_start_date < row['Start time']:
                    max_start_date = row['Start time']

                # Get seconds
                row['seconds'] = get_timedelta(row['Start time'],
                                               row['End time'])

            except ValueError:
                continue

            documents.append(row)

    # Insert everything
    if (len(documents) > 0):
        times_collection = timetracker_db.get_times_collection()
        times_collection.insert(documents)

        last_date_document['date'] = max_start_date
        config_collection.find_one_and_replace(self_time_filter,
                                               last_date_document,
                                               upsert=True)


def main():
    """Main function, define arguments and make calls"""
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="csv file to load")

    args = parser.parse_args()
    load_data(args.filename)


if __name__ == "__main__":
    main()
