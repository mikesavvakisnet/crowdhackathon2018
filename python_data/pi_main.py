"""
    File name: pi_main.py
    Author: Georgios Vrettos
    Date created: 29/6/2017
    Date last modified: 29/6/2018
    Python Version: 2.7

Todo :
	* 

"""

from pi_states import InitialMode

class PiMain():

    def __init__(self):

        self.state = InitialMode()

main = PiMain()