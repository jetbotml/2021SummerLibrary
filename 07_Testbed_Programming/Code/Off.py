from __future__ import division
from gpiozero import Button
from gpiozero import Motor
from gpiozero import DistanceSensor
from gpiozero import LED
from gpiozero import Buzzer
from gpiozero import RGBLED
from gpiozero import LightSensor
from gpiozero import LEDBoard
from time import sleep

SleepTime = 1

leds = LEDBoard(25, 24, 9, 10, 15, 18, 17, 22, 27, 23)
FullColorled = RGBLED(red=12, green=6, blue=13)
SensorLight = LightSensor(8)
SensorDistance = DistanceSensor(echo=11, trigger=7)
Leftmotor = Motor(forward=20, backward=21)
Rightmotor = Motor(forward=19, backward=26)
buzzer = Buzzer(4)
Leftbutton = Button(16)
Rightbutton = Button(5)

leds.off()
FullColorled.color = (0, 0, 0)  # off
buzzer.off()
