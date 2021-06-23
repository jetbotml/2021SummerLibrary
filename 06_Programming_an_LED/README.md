# 6 Programming an LED

https://magpi.raspberrypi.org/articles/breadboard-tutorial

https://projects.raspberrypi.org/en/projects/physical-computing



    from gpiozero import LED
    from time import sleep

    led = LED(17)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)

