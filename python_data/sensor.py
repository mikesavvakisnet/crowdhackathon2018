# sensor.py

import RPi.GPIO as GPIO
from time import sleep
import Adafruit_DHT
import json
import microcontroller

class Sensor(object):
    def __init__(self):
        pass

    def read(self):
        data = {}
        try:
            humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17)
            amb_light, battery_status = microcontroller.read(arduino=microcontroller.arduino)
            data = json.dumps({"temperature": temperature, "humidity": humidity,
                                "ambient_light": int(amb_light[:(str(amb_light).find("/r"))]), "battery": battery_status})
        except:
            data = json.dumps({"temperature": "error", "humidity": "error"})

        return data
