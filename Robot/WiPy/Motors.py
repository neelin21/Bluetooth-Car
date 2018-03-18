#####################################################
# Filename: Motors.py
# Description: This will contain the motor control code
# Author: Neelin Vakil
#####################################################
from machine import PWM
from machine import Pin

class Motors(object):

    def __init__(self):

        pwm = PWM(0, frequency=10000)  # use PWM timer 0, with a frequency of 5KHz
        # create pwm channel on pin P12 with a duty cycle of 0%
        self.left_motor = pwm.channel(0, pin='P20', duty_cycle=0.0)
        self.right_motor = pwm.channel(1, pin='P19', duty_cycle=0.0)

        # Right Motor direction controls
        self.right_forward = Pin('P5', mode=Pin.OUT)
        self.right_forward.value(0)
        self.right_reverse = Pin('P6', mode=Pin.OUT)
        self.right_reverse.value(0)

        # Left Motor direction controls
        self.left_forward = Pin('P7', mode=Pin.OUT)
        self.left_forward.value(0)
        self.left_reverse = Pin('P8', mode=Pin.OUT)
        self.left_reverse.value(0)

        return

    def left_forward(self, speed):
        self.left_reverse.value(0)
        self.left_forward.value(1)
        self.left_motor.duty_cycle(speed)
        return

    def left_reverse(self, speed):
        self.left_forward.value(0)
        self.left_reverse.value(1)
        self.left_motor.duty_cycle(speed)
        return

    def right_forward(self, speed):
        self.right_reverse.value(0)
        self.right_forward.value(1)
        self.right_motor.duty_cycle(speed)
        return

    def right_reverse(self, speed):
        self.right_forward.value(0)
        self.right_reverse.value(1)
        self.right_motor.duty_cycle(speed)
        return

    def forward(self, speed):
        # Turn off reverse signals
        self.left_reverse.value(0)
        self.right_reverse.value(0)

        # Turn on forward signals
        self.left_forward.value(1)
        self.right_forward.value(1)

        self.right_motor.duty_cycle(speed)
        self.left_motor.duty_cycle(speed)
        return

    def reverse(self, speed):
        # Turn off forward signals
        self.left_forward.value(0)
        self.right_forward.value(0)

        # Turn on reverse signals
        self.left_reverse.value(1)
        self.right_reverse.value(1)

        self.right_motor.duty_cycle(speed)
        self.left_motor.duty_cycle(speed)
        return
