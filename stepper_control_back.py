from stepper import stepper
import json
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins = [18,21,22,23] # controller inputs: in1, in2, in3, in4

for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

step1 = stepper(pins)

while True:
  with open("lab5.txt", 'r') as f:
    data = json.load(f)
    angle = float(data['angle']) 
    home = float(data['home']) 
    if home == 1:
      step1.zero()
    else:
      step1.moveSteps(256*angle/360,1)
  time.sleep(0.01)


try:
  step1.moveSteps(1000,1)
except:
  pass
GPIO.cleanup() 