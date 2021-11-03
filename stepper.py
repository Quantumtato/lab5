import RPi.GPIO as GPIO
import time
from PCF8591 import PCF8591

sensor = PCF8591(1)

class stepper:
  # Define the pin sequence for counter-clockwise motion, noting that
  # two adjacent phases must be actuated together before stepping to
  # a new phase so that the rotor is pulled in the right direction:
  
          
  state = 0  # current position in stator sequence
  def __init__(self, pins):
    self.pins = pins
    self.state = 0
    self.sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,
            1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
    pass

  def delay_us(self, tus): # use microseconds to improve time resolution
    endTime = time.time() + float(tus)/ float(1E6)
    while time.time() < endTime:
      pass

  def halfstep(self,dir):
    # dir = +/- 1 (ccw / cw)
    global state
    state += dir
    if state > 7: state = 0
    elif state < 0: state =  7
    for pin in range(4):    # 4 pins that need to be energized
      GPIO.output(self.pins[pin], self.sequence[state][pin])
    self.delay_us(1000)

  def moveSteps(self, steps, dir):
    # move the actuation sequence a given number of half steps
    for step in steps:
      self.halfstep(dir)

  def zero(self):
    while sensor.read(1) > 100:
      self.moveSteps(1)
    self.state = 0