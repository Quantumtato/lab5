import stepper
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4

for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

step1 = stepper(pins)
step1.pins


try:
  step1.moveSteps(1000,1)
except:
  pass
GPIO.cleanup() 