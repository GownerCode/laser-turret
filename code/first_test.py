from gpiozero import Servo
from time import sleep

servo = Servo(25)

servo.value = 1
sleep(5)
servo.value = -1