"""
March 25, 2025
by: Sophie Nguyen
 
using sonar with arduino

"""

import time
import board
import adafruit_hcsr04

#constants
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.GP2, echo_pin=board.GP3)

led.value = False

while True:
    if sonar.distance < 10:
         #turns on LED
        led.value = True

    else:
        #turns LED off
        led.value = False
