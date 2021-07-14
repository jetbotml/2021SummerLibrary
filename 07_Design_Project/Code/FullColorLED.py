from __future__ import division
from gpiozero import RGBLED
from time import sleep

SleepTime = 1

FullColorled = RGBLED(red=12, green=6, blue=13)

while True:

  FullColorled.color = (1, 0, 0)  # full red
  sleep(SleepTime)
  FullColorled.color = (0, 1, 0)  # full green
  sleep(SleepTime)
  FullColorled.color = (0, 0, 1)  # full blue
  sleep(SleepTime)
  FullColorled.color = (1, 0, 1)  # magenta
  sleep(SleepTime)
  FullColorled.color = (1, 1, 0)  # yellow
  sleep(SleepTime)
  FullColorled.color = (0, 1, 1)  # cyan
  sleep(SleepTime)
  FullColorled.color = (1, 1, 1)  # white
  sleep(SleepTime)
  FullColorled.color = (0, 0, 0)  # off
  sleep(SleepTime)

  FullColorled.color = (0, 0, 0)  # off

  # slowly increase intensity of blue
  for n in range(100):
    FullColorled.blue = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off
 
  # slowly increase intensity of red
  for n in range(100):
    FullColorled.red = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off

  # slowly increase intensity of green
  for n in range(100):
    FullColorled.green = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off
  
  for n in range(100):
    FullColorled.green = n/100
    FullColorled.red = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off

  for n in range(100):
    FullColorled.blue = n/100
    FullColorled.red = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off

  for n in range(100):
    FullColorled.blue = n/100
    FullColorled.green = n/100
    sleep(0.05)
  FullColorled.color = (0, 0, 0)  # off
    
