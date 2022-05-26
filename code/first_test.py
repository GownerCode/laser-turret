from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
from gpiozero import Servo
from time import sleep
from pynput import keyboard

def stepUp():
    print("stepped up")
    servo.value -= 0.1

def stepDown():
    print("stepped down")
    servo.value += 0.1

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['up', 'down']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        if k == "up":
            print(f"pressed {k}")
            stepUp()
        elif k == "down":
            print(f"pressed {k}")
            stepDown()
        return False  # stop listener; remove this if want more keys

Device.pin_factory = PiGPIOFactory()

servo = Servo(25)

servo.mid()
sleep(1)

listener = keyboard.Listener(on_press=on_press)
listener.start()  # start to listen on a separate thread

while True:
    pass