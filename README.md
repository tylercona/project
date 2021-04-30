# Ambient Temperature and Humidity Observer

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
  and "A full buffer was not returned. Try again." would consistently happen. To work around this, 
  the code was manipulated to display the last successful reading until the next reading is available. </p>
  
<p>Next, a Flask web server for this data will be created. Using <code>app.py</code>
  this will initialize a web server to display the data pulled from the sensor. The consistent failures
  in the sensor modules reading created very big problems for the Flask web server, because if there
  was a failure in reading the sensor then the server would crash. The solution to this problem is to 
  display the last successful reading the sensor had on every refresh, until a new reading is taken.</p>
  
<p>Using HTML the template of the website will be created under <code>layout.html</code>
  which will take the information pulled from the sensor in the Python code and insert the
  temperature and humidity values into the website for the user's display.
  
  Below it can be seen the webserver is working on Chromium on the Raspberry Pi at 127.0.0.1:5000 and 
  by searching the IP address of the Pi on an iOS device connected to the same 
  Wi-Fi network the server can also be reached.
  
![IMG_2672](https://user-images.githubusercontent.com/78391004/115900794-58c9c080-a42e-11eb-9684-aa5fb1a093e8.png)

![Screen Shot 2021-04-23 at 12 16 34 PM](https://user-images.githubusercontent.com/78391004/115900273-c1646d80-a42d-11eb-9066-b42c330f26fa.png)
