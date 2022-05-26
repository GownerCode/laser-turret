from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo
from time import sleep

Device.pin_factory = PiGPIOFactory()

servo = Servo(25)

servo.max()
sleep(10)
