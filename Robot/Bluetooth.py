#This file will contain code used to read in bluetooth signals from the transmitter
#Neelin Vakil
#March 2017

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Use GPIO pins 13 and 19 for PWM
#13 - Left Wheel
#19 - Right Wheel
def GetMessage( ):

    GPIO.setup(13, GPIO.OUT) #Left
    GPIO.setup(19, GPIO.OUT) #Right
    
    #pwm = GPIO.PWM(pin, frequency)
    #pwm.start(duty cycle)
    #pwm.ChangeDutyCycle(duty cycle)
    PWMLeft = GPIO.PWM(13, 1000)
    PWMRight = GPIO.PWM(19,1000)
    
    BTmessage = ""
#Bluetooth part to get message


    
