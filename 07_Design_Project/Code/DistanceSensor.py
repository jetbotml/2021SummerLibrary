from __future__ import division
from gpiozero import DistanceSensor
from time import sleep

SleepTime = 1

SensorDistance = DistanceSensor(echo=11, trigger=7)

while True:
    
    print("Distance inches = " + str(SensorDistance.distance*39.3701) )
    sleep(SleepTime )
