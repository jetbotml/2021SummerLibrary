# 3 Lighting an LED using Raspberry Pi

https://projects.raspberrypi.org/en/projects/physical-computing/2

What you will need
![LED](LED.png)
![Jumpers](MtoFJumper.png)
![resistor](resistor.png)


![whatisneeded](whatisneeded.png)


---FlashingLED.py – python code----------------------------------------------------
from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


![LEDPi](LEDPi.png)
![BB](2021-06-19-214020.jpg)
