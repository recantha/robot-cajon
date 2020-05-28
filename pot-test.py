from gpiozero import MCP3008
from time import sleep

pot1 = MCP3008(3)

while True:
    print("Pot 1: " + str(pot1.value))

    sleep(0.1)
