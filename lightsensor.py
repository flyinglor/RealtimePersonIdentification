#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
 
channel =4  #input channel of the light sensor, GPIO4
GPIO.setmode(GPIO.BCM) 
GPIO.setup(channel, GPIO.IN)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)

while True:
    try:
        if GPIO.input(channel) == GPIO.HIGH:
        sleep(10)
        if GPIO.input(channel) == GPIO.HIGH:
            count=0
            while count<10:
                GPIO.output(20, GPIO.HIGH)
                sleep(3)
                GPIO.output(20,GPIO.LOW)
                count++
    except KeyboardInterrupt:
        GPIO.cleanup()
        raise
