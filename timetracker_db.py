from pymongo import MongoClient


client = MongoClient()


def get_config_collection():
    """Return the collection used for configuration"""
    return client["timetracker"]["config"]


def get_times_collection():
    """Return the collection used for times"""
    return client["timetracker"]["times"]
