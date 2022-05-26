from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo, LED
from time import sleep
import tkinter as tk

LASER = 23
SHOULDER = 24
HEAD = 25

Device.pin_factory = PiGPIOFactory()

head = Servo(HEAD, min_pulse_width=0.001050, max_pulse_width=0.0025)
shoulder = Servo(SHOULDER, min_pulse_width=0.0006, max_pulse_width=0.0025)
laser = LED(LASER)

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
    elif event.char == "f":
        laser.toggle()

root = tk.Tk()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()