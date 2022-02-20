import numpy as np
import serial
import time
import matplotlib.pyplot as plt

"""
This file reads a single sensor value from the arduino over serial. The data is assumed to be sent every minute.
"""
arduino = serial.Serial(port='/dev/tty.usbmodem143401', baudrate=9600, timeout=.1)

def read():
    data = arduino.readline()
    return data


if __name__ == '__main__':
    values = []
    num_samples = 0
    while True:
        value = read()
        if value:
            value = value.decode()
            value = int(value)
            print("Minute: {} Value: {}".format(num_samples + 1, value)) # printing the value
            values.append(value)
            num_samples += 1

