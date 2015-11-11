import json
import timetracker_db

from bson import json_util
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/api/time-status')
def get_data():
    times_collection = timetracker_db.get_times_collection()
    return json.dumps(times_collection.find_one(), default=json_util.default)


if __name__ == '__main__':
    app.debug = True
    app.run()
