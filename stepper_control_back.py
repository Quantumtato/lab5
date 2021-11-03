from stepper import stepper
from PCF8591 import PCF8591

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4

for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

step1 = stepper(pins)




try:
  step1.moveSteps(1000,1)
except:
  pass
GPIO.cleanup() 