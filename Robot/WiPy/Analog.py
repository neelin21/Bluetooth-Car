#####################################################
# Filename: Analog.py
# Description: This file contains the code to read the analog input pins
# and work with the analog outputs
# Author: Neelin Vakil
#####################################################
from machine import ADC
from machine import DAC

class Analog_Inputs(object):

    def __init__(self):
        adc = ADC(0)
        self.input_1 = adc.channel(pin='P13', attn=ADC.ATTN_11DB)
        self.input_2 = adc.channel(pin='P14', attn=ADC.ATTN_11DB)
        self.input_3 = adc.channel(pin='P15', attn=ADC.ATTN_11DB)
        self.input_4 = adc.channel(pin='P16', attn=ADC.ATTN_11DB)
        self.input_5 = adc.channel(pin='P17', attn=ADC.ATTN_11DB)
        self.input_6 = adc.channel(pin='P18', attn=ADC.ATTN_11DB)

        return

class Analog_Outputs(object):

    def __init__(self):
        self.dac_1 = DAC('P21')
        self.dac_2 = DAC('P22')
        return
