#####################################################
# Filename: UART.py
# Description: This file will handle the communication protocol between the WiPy
# and Raspberry Pi
# Author: Neelin Vakil
#####################################################

from machine import UART
from time import sleep
import machine
import _thread

class Pi_Comm(object):

    def __init__(self):
        self.message_queue = []
        self.uart = UART(1, 9600)                         # init with given baudrate
        self.uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

        UART.irq(UART.RX_ANY, priority=1, handler=self.received_from_pi, wake=machine.IDLE)
        _thread.start_new_thread(self.th_process_message, [])

        return

    def send_to_pi(self, message):
        self.uart.write(message)
        return

    def received_from_pi(self):
        self.message_queue.append(self.uart.read(8))
        return

    def th_process_message(self):
        while True:
            if self.message_queue != []:
                message = self.message_queue[0]

                # parse message and handler

                # Remove message that was just processed
                del self.message_queue[0]

        return
