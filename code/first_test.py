from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo
from time import sleep
import tkinter as tk

Device.pin_factory = PiGPIOFactory()

servo = Servo(25)

def stepUp():
    servo.value -= 0.1

def stepDown():
    servo.value += 0.1

def onKeyPress(event):
    if event.char == "w":
        stepUp()
    elif event.char == "s":
        stepDown()

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()