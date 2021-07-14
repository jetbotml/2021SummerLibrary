from gpiozero import LightSensor
from time import sleep

SleepTime = 1
SensorLight = LightSensor(8)

while True:

    print("Light = " + str(SensorLight.value) )
    sleep(SleepTime)


