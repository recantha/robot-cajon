from gpiozero import Button
from time import sleep

button = Button(4)

while True:
    button.wait_for_press()
    print("Button pressed")
    sleep(0.3)
