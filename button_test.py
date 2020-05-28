from gpiozero import Button, LED
from time import sleep

button = Button(23)
button_led = LED(25)

button_led.on()

while True:
    button.wait_for_press()

    print("Button has been pressed")
    sleep(1)
