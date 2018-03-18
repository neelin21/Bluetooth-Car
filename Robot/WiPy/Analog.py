#####################################################
# Filename: Analog.py
# Description: This file contains the code to read the analog input pins
# and work with the analog outputs
# Author: Neelin Vakil
#####################################################
from machine import ADC

class Analog(object):

    def __init__(self):

        adc = ADC(0)
        self.input_1 = adc.channel(pin='P13', attn=ADC.ATTN_11DB)

        return
