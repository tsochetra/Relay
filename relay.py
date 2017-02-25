import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pinList = [26, 17, 27, 22, 18, 23, 24, 25]
#GPIO number on Raspberry Pi 

def turnon(NumGPIO, NumRelay):
    GPIO.setup(NumGPIO, GPIO.OUT)
    if GPIO.input(NumGPIO) == GPIO.LOW:
        return "light "+NumRelay+" has already been opened"
    else:
        GPIO.output(NumGPIO, GPIO.LOW)
        return "light "+NumRelay+" is now opened"



def turnoff(NumGPIO, NumRelay):
    GPIO.setup(NumGPIO, GPIO.OUT)
    if GPIO.input(NumGPIO) == GPIO.HIGH:
        return "light "+NumRelay+" has already been closed"
    else:
        GPIO.output(NumGPIO, GPIO.HIGH)
        return "light "+NumRelay+" is now closed"


if len(sys.argv) == 3:

    NumGPIO = pinList[int(sys.argv[1]) - 1]
    NumRelay = sys.argv[1]
    if sys.argv[2] == "on":
        out = turnon(NumGPIO, NumRelay)
        print(out)
    elif sys.argv[2] == "off":
        out = turnoff(NumGPIO, NumRelay)
        print(out)



elif len(sys.argv) == 2:
    parameter = sys.argv[1]
    if parameter == "get":
        arr = ""
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            if GPIO.input(i) == GPIO.HIGH:
                arr += ("Off,")
            else:
                arr += ("On,")
        print(arr)
    elif parameter == "openall":
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.LOW)
    elif parameter == "closeall":
        for i in pinList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
