"""
    File name: recognition.py
    Author: Georgios Vrettos
    Date created: 29/6/2018
    Date last modified: 29/6/2018
    Python Version: 2.7


This module contains image recognition settings and functions.

Todo :
	* 

"""

import os
import base64
import json

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

# Global variables
# --------------------------------------------------------------------------------------------------

# Image save directory
DEFAULT_SAVE_DIRECTORY = "/home/hacker/crowdhackathon/Senseit/camera_images/"

# A JSON file containing all Google application credentials.
GOOGLE_CREDENTIALS_JSON = "/home/hacker/crowdhackathon/Senseit/vision1-575dce996932.json"

# Exporting GOOGLE authentication variable.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GOOGLE_CREDENTIALS_JSON

# Number of the maximum results for the Google Algorithm.
RESULTS_COUNT = 10


# --------------------------------------------------------------------------------------------------


class Recognition():

    def __init__(self, image_directory=DEFAULT_SAVE_DIRECTORY):

        # Authentication process
        credentials = GoogleCredentials.get_application_default()
        self.service = discovery.build('vision', 'v1', credentials=credentials)

        self.image_directory = image_directory

    def detect(self, image):

        image = self.image_directory + image

        with open(image, 'rb') as image:
            image_content = base64.b64encode(image.read())
            service_request = self.service.images().annotate(body={
                'requests': [{
                    'image': {
                        'content': image_content.decode('UTF-8')
                    },
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': RESULTS_COUNT
                    }]
                }]
            })
            response = service_request.execute()
            # response is converted into JSON object.
            response = json.dumps(response, indent=4, sort_keys=True)
            print(response)
            return response

    def compare_values(self,recognition_elements,recognition_results):

        detected = False

        try:
            decoded_results = json.loads(recognition_results)
            for response in decoded_results['responses']:
                for annotation in response['labelAnnotations']:
                    if(annotation['description']) in recognition_elements:
                        # If an wanted element is detected
                        print(annotation['description'] + " detected!")
                        print("Score: " + str(annotation['score']))
                        detected = True

        except (ValueError, KeyError, TypeError):
            print "JSON format error"


        return detected


