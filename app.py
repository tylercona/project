from flask import Flask, render_template
from flask import send_from_directory
import os
import time
import board
import adafruit_dht

app = Flask(__name__)

dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

@app.route("/")
def index():

    temperature, humidity = sensor()
    print(temperature)
    print(humidity)

    return render_template("layout.html", temperature=temperature, humidity=humidity)

def sensor():
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity

    if humidity is None or temperature is None:
        return temperature == 0, humidity == 0
    else:
        return temperature, humidity
    

if __name__ == "__main__":
    app.run(debug=False)
