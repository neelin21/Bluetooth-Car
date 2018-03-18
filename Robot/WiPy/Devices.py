#####################################################
# Filename: Devices.py
# Description: This file contains codes to interface with devices connected via I2C
# Author: Neelin Vakil
#####################################################
from machine import I2C

class Devices(object):

    def __init__(self):
        self.i2c = I2C(0, I2C.MASTER, baudrate=100000)
        return
