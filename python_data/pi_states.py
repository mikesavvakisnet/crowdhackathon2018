"""
    File name: pi_states.py
    Author: Georgios Vrettos
    Date created: 29/6/2017
    Date last modified: 29/6/2018
    Python Version: 2.7

Todo :
	* 

"""

from sensor import Sensor
from camera import Camera
from recognition import Recognition

import requests
import datetime
import time
import json

# GLOBAL VARIABLES
hostname = "https://hackathoncrowd.herokuapp.com"

class InitialMode():

    def __init__(self):

        print(self.__class__.__name__)

        # Initialize modules
        sensor = Sensor()
        camera = Camera()
        recognition = Recognition()

        # Engage active mode
        self.state = ActiveMode(sensor=sensor, camera=camera, recognition=recognition)


class ActiveMode():

    # Class variables
    recognition_elements = ['cup','chair']

    def __init__(self, sensor, camera, recognition):

        self.camera = camera
        self.recognition = recognition
        self.sensor = sensor

        print(self.__class__.__name__)

        while True:
            self.get_sensor()
            self.get_camera()
            time.sleep(1)


    def get_camera(self):

        detection_status = False

        try:
            # Capture image
            image_file = self.camera.capture()
            # Get element list
            elements_list = self.recognition.detect(image=image_file)
            # Compare results
            detection_status = self.recognition.compare_values(recognition_elements=self.recognition_elements,
                                                          recognition_results=elements_list)
        except:
            print("Error: Camera failed.")
            detection_status = False


        if(detection_status==True):
            print("Item detected")
            # http request
            data = {"reason":"Detection Alarm","date":self.get_local_time()}
            self.http_request(data,type="camera")
        else:
            print("Nothing interesting detected")

    '''
    def get_pic(self):
        i=0
        while(i<20):
            image_file = self.camera.capture(i_name=str(i))
            time.sleep(7)
            i+=1
    '''

    def get_sensor(self):
        try:
            # Capture data
            data = self.sensor.read()
        except:
            print("Error: Data capture failed")

        # http request
        self.http_request(data,type="sensor")



    def http_request(self,data,type):
        try:
            if(type=="camera"):
                response = requests.post(hostname + "/api/sensit/alert", data=data)
                print("Request sent!")
                print(response)
            elif(type=="sensor"):
                data = json.loads(data)
                print(data)
                response = requests.post(hostname + "/api/sensit/data", data=data)
                print("Request sent!")
                print(response)


        except:
            print("ERROR: HTTP Request failed.")

    def get_local_time(self):

        # Get the local timestamp using functions from the datetime package.
        current_time = datetime.datetime.now().strftime("%d-%m-%-Y %H:%M:%S")
        return current_time





