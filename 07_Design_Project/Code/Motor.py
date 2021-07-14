from gpiozero import Button
from gpiozero import Motor
from time import sleep

SleepTime = 1

Leftmotor = Motor(forward=20, backward=21)
Rightmotor = Motor(forward=19, backward=26)
Leftbutton = Button(16)
Rightbutton = Button(5)

while True:

      Leftbutton.when_pressed = Leftmotor.forward
      Leftbutton.when_released = Leftmotor.stop



