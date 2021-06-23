# 6 Programming a Button

https://gpiozero.readthedocs.io/en/stable/recipes.html#button-controlled-led

<img src="button-LED.png" width="50%" height="50%">

    from gpiozero import LED, Button
    from signal import pause

    led = LED(17)
    button = Button(2)

    button.when_pressed = led.on
    button.when_released = led.off

    pause()

<img src="2021-06-23-105414.jpg" width="50%" height="50%">
