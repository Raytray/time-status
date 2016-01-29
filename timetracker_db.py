import configparser

from pymongo import MongoClient


config = configparser.ConfigParser()
config.read('config.conf')

USERNAME = config.get('mongo', 'USERNAME')
PASSWORD = config.get('mongo', 'PASSWORD')

client = MongoClient()
client.timetracker.authenticate(USERNAME, PASSWORD)


def get_config_collection():
    """Return the collection used for configuration"""
    return client["timetracker"]["config"]


def get_times_collection():
    """Return the collection used for times"""
    return client["timetracker"]["times"]
