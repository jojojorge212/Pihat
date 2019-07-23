#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
#this will clear any LEDs left in the 'on' statethat a 
#that a diffrent script may have left on

print("clearing LEDs")

sense.clear()
