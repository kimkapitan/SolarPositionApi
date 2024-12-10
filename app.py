from flask import Flask, jsonify
from pysolar.solar import get_altitude
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/solar-position/<int:timestamp>/<float:latitude>/<float:longitude>/')
def get_solar_position(timestamp, latitude, longitude):
    date = datetime.fromtimestamp(timestamp, pytz.UTC)
    return jsonify([get_altitude(latitude, longitude, date.replace(hour = hour, minute = 0, second = 0)) for hour in range(24)])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)