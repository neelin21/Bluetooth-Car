#This file will contain code used to read in bluetooth signals from the transmitter
#Neelin Vakil
#March 2017

import RPi.GPIO as GPIO
import serial

GPIO.setmode(GPIO.BCM)

#Use GPIO pins 13 and 19 for PWM
#13 - Left Wheel
#19 - Right Wheel
#Make GPIO pins for forward and reverse
# - Forward Left
# - Reverse Left
# - Forward Right
# - Reverse Right
def GetMessage( ):

    GPIO.setup(13, GPIO.OUT) #Left
    GPIO.setup(19, GPIO.OUT) #Right

    #pwm = GPIO.PWM(pin, frequency)
    #pwm.start(duty cycle)
    #pwm.ChangeDutyCycle(duty cycle)
    PWMLeft = GPIO.PWM(13, 1000)
    PWMRight = GPIO.PWM(19,1000)
    ser = serial.Serial ("/dev/ttyAMA0")    #Open named port
    #Set baud rate to 9600
    ser.baudrate = 9600

    while true:
        BTmessage = ser.read(10)
        #Bluetooth part to get message
        AnalyzeMessage(BTmessage)

        ser.write(data)                         #Send back the received data

    #ser.close()

    return

def AnalyzeMessage( message ):
    #Message format for movement
    #._-#
    #F - Forward
    #B - Back
    #R - Right
    #L - Left
    Parse = message.split("-")

    if Pasre[0] == '.F':
        #Forward

    elif message == '.B':
        #Back

    elif message == '.L':
        #Left

    elif message == '.R':
        #Right

    else:
        #Default case
        PWMLeft.ChangeDutyCycle(0)
        PWMRight.ChangeDutyCycle(0)

    print message
    return
