"""
    File name: camera.py
    Author: Georgios Vrettos
    Date created: 29/6/2018
    Date last modified: 29/6/2018
    Python Version: 2.7



"""

import subprocess
import time
import datetime


# Global variables
# --------------------------------------------------------------------------------------------------

# Capture device port
CAMERA_DEVICE_PORT = "/dev/video0"

# Setting camera resolution (pixel)
DEFAULT_IMAGE_WIDTH = "1920"
DEFAULT_IMAGE_HEIGHT = "1080"

# Camera delay setting
CAMERA_DELAY = 1

# Image save directory and image info
DEFAULT_SAVE_DIRECTORY = "/home/hacker/crowdhackathon/Senseit/camera_images/"
DEFAULT_IMAGE_FILE_NAME = "image"
DEFAULT_FILE_TYPE = ".jpg"


# --------------------------------------------------------------------------------------------------

class Camera():
    """
    This class represents the camera object. It includes all camera settings and functions
    """

    def __init__(self, image_width=DEFAULT_IMAGE_WIDTH,image_height=DEFAULT_IMAGE_HEIGHT,save_directory=DEFAULT_SAVE_DIRECTORY):

        self.image_width = image_width
        self.image_height = image_height
        self.save_directory = save_directory


    def capture(self,file_name = DEFAULT_IMAGE_FILE_NAME):

        name = file_name + self.get_local_time() + DEFAULT_FILE_TYPE

        # A subprocess handles the image capture using the program "fswebcam" with specified settings.
        subprocess.Popen("fswebcam -d " + CAMERA_DEVICE_PORT + " -D " + str(CAMERA_DELAY) + " -r " + self.image_width + "x" + self.image_height + " " + self.save_directory + name, shell=True);
        # a small delay is necessary for the image capture subprocess to complete.
        time.sleep(CAMERA_DELAY + 3)
        print("Image captured")
        return name

    def get_local_time(self):

        # Get the local timestamp using functions from the datetime package.
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H_%M")
        return current_time


