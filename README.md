
# Ambient Temperature and Humidity Observer

<p>The motivation for this project is to provide a tool for 
people in manufacturing or any other field who 
are interested in the ambient temperature and humidity of the 
room in which raw materials are stored in. At my current 
place of employment we manufacture electronics using organic 
materials that are suscepible to moisture absorbtion it is important 
that we capture the ambient temperature and humidity of the room 
in which experiments are being conducted in, and where raw materials 
are stored in. Ideally we want the materials to stay free of any moisture and 
be stored in rooms as dry as possible.</p>

<p>In this project, I will be using a DHT22 Temperature and Humidity
Sensor Module and a Raspberry Pi 4 accompanied by Flask to run a web 
server. The purpose of the project is to 
use the Raspberry Pi to draw data from the sensor and display it
clearly on a web server on an external display connected to the 
Raspberry Pi or on any other device connected to the same Wi-Fi 
network. A web server will be hosted using Flask and 
hosted on a local server for the user. Using Python and HTML,
a code will be scripted to provide instructions to the Raspberry 
Pi to collect data from the sensor module through GPIO pins and display it on 
a live updating web server. Using this product any person
can be able to quickly receive an accurate reading of the 
ambient temperature and humidity for experimental logging 
or storage quality check.</p> 

<p>Below is an image of the Raspberry Pi connected to the DHT sensor module using a GPIO Extension Board and solderless breadboard.</p>

![IMG_2728](https://user-images.githubusercontent.com/78391004/116921922-a6121300-ac22-11eb-8b41-70ea01007a91.png)


I will begin with experimenting with a code to simply pull data
from the DHT22 Sensor and printing the data on the terminal.

<p><code>DHTcapture.py</code> is the code that tests the sensor. </p>

<p>An initial issue that was found with the sensor module was it was almost impossible to
  have a perfect reading each run. Errors such as "Checksum failed to validate. Try Again." 
  and "A full buffer was not returned. Try again." would consistently happen. To work around this, 
  the DHTcapture.py code was manipulated to sense there is a failure in the reading, display nothing and continue 
  looping until the next successful reading was taken, and then display that. This created a smooth
  flow of data in the command window and next a web server will be established to publish this 
  data for a user.</p>
  
<p>Next, a Flask web server for this data will be created. Using <code>app.py</code>
  this will initialize a web server to display the data pulled from the sensor. The consistent failures
  in the sensor module's reading created very big problems for the Flask web server, because if there
  was a failure in reading the sensor, Flask would not ignore the failure and would create an 
  error in the temperature and humidity variables which would cause the server to crash. The 
  solution to this problem is to change the DHT code to sense that there is an error, 
  and display on the webpage the last successful reading the sensor had. 
  The code will continue like normal and when there is another successful reading it will be displayed.</p>
  
<p>Using HTML the template of the website will be created under <code>layout.html</code>
  which will take the information pulled from the sensor in the Python code and insert the
  temperature and humidity values into the website for the user's display.
  
  Below one can see the web server is working on Chromium on the Raspberry Pi at 127.0.0.1:5000 and 
  the server can also be reached searching the IP address of the Pi on an iOS device connected to the same 
  Wi-Fi network.

  
![IMG_2714](https://user-images.githubusercontent.com/78391004/116745929-ce530500-a9c9-11eb-80e3-44caf34898a8.png)<img width="539" alt="Screen Shot 2021-04-30 at 3 30 42 PM" src="https://user-images.githubusercontent.com/78391004/116745995-e62a8900-a9c9-11eb-9a40-205d149f9a36.png">

<p>Below is a .gif image showing the web server updating on Chromium. 

![My Movie 1](https://user-images.githubusercontent.com/78391004/116749034-59ce9500-a9ce-11eb-846d-496fa44a633e.gif)
<center>

<p>Click on the image below to be redirected to a YouTube video of a demonstration of the project running on Chromium on Raspberry Pi, and on Google Chrome on a MacBook Pro.</p>

[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/78391004/117704618-0bbd4c80-b199-11eb-8a61-37a123c3990e.png)](https://youtu.be/L2MpAoBKkuo)



<p>At the end of the project, the problems that came with developing the web server have been overcome.
  For this being my first IoT related project, I am proud of the progress made from starting with minimal knowledge of IoT 
  at the beginning of the semester. This was a valuable hands-on learning experience that I wouldn't have gotten 
  from other course, and it broadened my experiences to something I never had learned before. 
  In the future to make the project more robust, a higher quality temperature and humidity sensor module
  could be employed. Using a higher quality sensor could provide less reading failures, more 
  accurate readings and a quicker sampling rate than the DHT22 that was used.</p>
