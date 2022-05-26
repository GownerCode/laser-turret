from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo
from time import sleep
import tkinter as tk

Device.pin_factory = PiGPIOFactory()

head = Servo(25)
shoulder = Servo(24)

def stepUp():
    try:
        head.value -= 0.1
    except:
        pass

def stepDown():
    try:
        head.value += 0.1
    except:
        pass

def stepLeft():
    try:
        shoulder.value += 0.1
    except:
        pass

def stepRight():
    try:
        shoulder.value -= 0.1
    except:
        pass

def onKeyPress(event):
    if event.char == "w":
        stepUp()
    elif event.char == "s":
        stepDown()
    elif event.char == "a":
        stepLeft()
    elif event.char == "d":
        stepRight()

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()