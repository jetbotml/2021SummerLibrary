from __future__ import division
from gpiozero import LEDBoard
from time import sleep

SleepTime = 1
leds = LEDBoard(25, 24, 9, 10, 15, 18, 17, 22, 27, 23)

while True:

    leds.on()
    sleep(SleepTime )
    leds.off()
    sleep(SleepTime )
    leds.value = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 0, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 0, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 0, 0, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 0, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 1, 0, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 1, 1, 0, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 0, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 1, 0)
    sleep(SleepTime )
    leds.value = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sleep(SleepTime )
    leds.value = (1, 0, 1, 0, 1, 0, 1, 0, 1, 0)
    sleep(SleepTime )
    leds.value = (0, 1, 0, 1, 0, 1, 0, 1, 0, 1)
    sleep(SleepTime )
    leds.blink()
    sleep(SleepTime )
    leds.off()
    sleep(SleepTime )
    

