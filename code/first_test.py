from gpiozero import Servo
from time import sleep

servo = Servo(25)

servo.min()
sleep(10)
