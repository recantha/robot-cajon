from gpiozero import MCP3008
from time import sleep

sensor1 = MCP3008(0)
sensor2 = MCP3008(1)
sensor3 = MCP3008(2)

while True:
    print("Sensor 1: " + str(sensor1.value))
    print("Sensor 2: " + str(sensor2.value))
    print("Sensor 3: " + str(sensor3.value))

    sleep(0.1)
