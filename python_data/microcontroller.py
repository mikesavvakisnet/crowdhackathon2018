# microcontroller.py

import serial
from time import sleep


def read(arduino):
    try:
        while(arduino.in_waiting < 0):
            pass

        arduino.reset_input_buffer()
        amb_light = arduino.readline()
        battery_status = 100
    except:
        amb_light = 'Error'
        battery_status = 'Error'
        print 'Error reading from microcontroller!'
    return amb_light, battery_status

arduino = serial.Serial('/dev/ttyUSB0')
arduino.baudrate=9600