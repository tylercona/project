# Ambient Temperature and Humidity 

The motivation for this project is to provide a tool for 
people in electronics manufacturing or any other field who 
are interested in the ambient temperature and humidity of the 
room in which raw materials are stored in. At my current 
place of employment, it is important that we capture the 
ambient temperature and humidity of the room in which experiments
are being conducted in, and where raw materials are stored in 
because we want the materials to stay free of any moisture and 
be stored in rooms as dry as possible.

In this project, I will be using a DHT22 Temperature and Humidity
Sensor Module and a Raspberry Pi 4 accompanied by Flask. The purpose of the project is to 
use the Raspberry Pi to draw data from the sensor and display it
clearly on a web server or an external display connected to the 
Raspberry Pi. A web server will be hosted using Flask and 
hosted on a local server for the user. Using Python and HTML
a code will be scripted to provide instructions to the Raspberry 
Pi to collect data from the sensor module and display it on 
a live updating web server. Using this product any person
can be able to quickly receive an accurate reading of the 
ambient temperature and humidity for experimental logging 
or storage quality check. 

I will begin with experimenting with a code to simply pull data
from the DHT22 Sensor and printing the data on the terminal.

<p><code>DHTcapture.py</code> is the code that tests the sensor. </p>

<p>An initial issue that was found with the sensor module was it was almost impossible to
  have a perfect reading each run. Errors such as "Checksum failed to validate. Try Again." 
  and "A full buffer was not returned. Try again." To work around this, it was decided that 
  if there was an error in the reading, the program will set the temperature and 
  humidity values equal to 0. </p>
  
<p>Next, a Flask web server for this data will be created. Using <code>app.py</code>
  this will initialize a web server to display the data pulled from the sensor. </p>
  
<p>Using HTML the template of the website will be created under <code>layout.html</code>
  which will take the information pulled from the sensor in the Python code and insert the
  temperature and humidity values into the website for the user's convenience.

