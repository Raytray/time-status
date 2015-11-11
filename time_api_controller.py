from flask import Flask
import timetracker_db


app = Flask(__name__)


@app.route('/api/time-status')
def get_data():
    config_collection = timetracker_db.get_config_collection()
    return config_collection.find()


if __name__ == '__main__':
    app.run()
