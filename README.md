# CSC-332-Project-1
Project 1 sensor module for WFU class CSC 332. Module created by Ellie Wheatley and Joe McCalmon.

This repository contains code for a module which automatically detects when houseplants need to be watered. It uses YL-69 moisture sensors, which increase in resistance when in wetter soil to detect moisture. Based on the input voltage returned by the sensor, we light a multicolor (RGB) LED to indicate the watering status of the plant.

We include a file for running the sensor module on an Arduino Uno, plants_project1.ino. This file is currently set up for two sensor modules, which each have one YL-69 sensor and one RGB LED, to run on a single Arduino. Since RGB LEDs require three PWM pins, we can only run up to two of these sensors on an Arduino Uno. More Arduinos can be utilized for more sensing modules. The code in plants_project1.ino can be adapted easily to run only one sensor node.

The image below is an example wiring of a single sensor node:

![sensor](https://github.com/mccajl/CSC-332-Project-1/blob/main/Full_sensor.png?raw=true)


![wiring](https://github.com/mccajl/CSC-332-Project-1/blob/main/Wiring_picture.png?raw=true)

# Wiring Details
The YL-69 sensor is hooked up to a potentiometer to give it analog input capabilities. Connect the sensor to the potentiometer via power and ground. Connect the power and ground pins on the potentiometer to the buses on the breadboard, and the analog output pin to the A0 pin on the Arduino. The soil sensor should now be configured correctly and its readings can be called by the analog 0 pin.

The RGB LED requires four separate pin wirings, one for each RGB component and one for ground. Connect the long pin of the RGB LED to ground on the Arduino. Connect three PWM pins (we use 9, 10, 11) to the other three prongs on the RGB LED. We use a 220 ohm resistor on each of these wirings to avoid overloading the LED. To display a color on the RGB LED, we perform three separate analogWrite() calls to each pin, 9, 10, and 11, with the blue, green, and red values, respectively.

# Code Details
Inside the loop function in the code, we first read the voltage value from the YL-69 sensor. If that value is less than 450 then the LED lights up blue, indicating the plant is overwatered. If it is between 450 and 800, the LED lights up green, meaning that it is in a good state. If it is greater than 800, the LED lights up red, indicating that the plant needs watering. This process occurs once a minute. These thresholds were determined through testing on our own houseplants.


The figure below shows an expected sensor reading of the module, starting when the plant is watered and continuing for 30 hours after. This plant in its particular placement needs to be watered around every 3 days, and by extrapolating the plot to that amount of time, we can see that the module should light up red around then.

![soil_readings](https://user-images.githubusercontent.com/59152508/154866154-7e85de5d-9b7a-416b-a100-b46f18cad88a.png)

