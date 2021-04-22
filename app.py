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
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        
        if temperature is None or humidity is None:
            time.sleep(1)
 
    except RuntimeError as error:
        temperature = 0
        humidity = 0

    return render_template("layout.html", temperature=temperature, humidity=humidity)

#def sensor():
#    temperature = dhtDevice.temperature
#    humidity = dhtDevice.humidity
#
#    if humidity is None or temperature is None:
#        time.sleep(10)
#    else:
#        return temperature, humidity
    

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
