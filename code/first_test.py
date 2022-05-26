from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo
from time import sleep
import Tkinter as tk

servo = Servo(25)

def stepUp():
    servo.value -= 0.1

def stepDown():
    servo.value += 0.1

def onKeyPress(event):
    text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()