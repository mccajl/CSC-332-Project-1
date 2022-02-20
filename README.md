# CSC-332-Project-1
Project 1 sensor module for WFU class CSC 332. Module created by Ellie Wheatley and Joe McCalmon.

This repository contains code for a module which automatically detects when houseplants need to be watered. It uses YL-69 moisture sensors, which increase in resistance when in wetter soil to detect moisture. Based on the input voltage returned by the sensor, we light a multicolor LED to indicate the watering status of the plant.

We include a file for running the sensor module on an Arduino Uno, plants_project1.ino. This file is currently set up for two sensor modules, which each have one YL-69 sensor and one multicolor LED, to run on a single Arduino. Since multicolor LEDs require three PWM pins, we can only run up to two of these sensors on an Arduino Uno. More Arduinos can be utilized for more sensing modules. The code in plants_project1.ino can be adapted easily to run only one sensor node.

The image below is an example wiring of a single sensor node:

![alt text](https://github.com/mccajl/CSC-332-Project-1/blob/main/Full_sensor.png?raw=true)

