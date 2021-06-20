# 6 Programming a Button

https://projects.raspberrypi.org/en/projects/physical-computing/2




---FlashingLED.py – python code----------------------------------------------------
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

