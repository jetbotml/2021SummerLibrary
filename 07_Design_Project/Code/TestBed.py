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

while True:

    leds.on()
    sleep(SleepTime)
    leds.off()
    sleep(SleepTime)
    leds.value = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 0, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 1, 1, 0, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 0, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
    sleep(SleepTime)
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sleep(SleepTime)
    leds.value = (1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
    sleep(SleepTime)
    leds.value = (0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
    sleep(SleepTime)
    leds.blink()
    sleep(SleepTime)
    leds.off()
    sleep(SleepTime)
    
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

    for n in range(5):
      print(SensorLight.value)
      sleep(SleepTime)

    while SensorLight.value < .85:
      FullColorled.color = (0, 0, 0)  # off
      print(SensorLight.value)

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
    
    for n in range(5):
      print("Distance inches = " + str(SensorDistance.distance*39.3701) )
      sleep(SleepTime)

    while (SensorDistance.distance*39.3701 < 20):
      print("Press left or right button")
      print("           ")
      print("Distance inches = " + str(SensorDistance.distance*39.3701) )
      Leftbutton.when_pressed = Leftmotor.forward
      Leftbutton.when_released = Leftmotor.stop
      if Rightbutton.is_pressed:
        buzzer.on()
      else:
        buzzer.off()
      sleep(SleepTime)

    print("5 sec to start over")
    sleep(5)
