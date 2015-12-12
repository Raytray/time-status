import json
import timetracker_db

from bson import json_util
from flask import Flask, jsonify, render_template


app = Flask(__name__)


@app.route('/api/time-series')
def get_data():
    """Time series Handler. Returns the times collection."""
    times_collection = timetracker_db.get_times_collection()
    return json.dumps(times_collection.find_one(), default=json_util.default)


@app.route('/')
def index():
    """Serve the template."""
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
