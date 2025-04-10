"""
March 25, 2025
by: Sophie Nguyen
 
using sonar with pico

"""

import time
import board
import adafruit_hcsr04
import digitalio


# variables
seconds_to_microseconds_conversion_number = 1000000
sonar_delays = [2 / seconds_to_microseconds_conversion_number, 10 / seconds_to_microseconds_conversion_number]
delay_between_sonar_cheeks = 1
distance = 0
TOO_CLOSE = 20

# setup
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# loop
while True:
    # Sonar gets the distance form object
    time.sleep(delay_between_sonar_cheeks)
    distance = sonar.distance

    print(f"Distance: {distance} cm")

    # Turns on LED if an object’s distance is equal to or closer then 20 cm from the sonar
    if distance <= TOO_CLOSE:
        led.value = True
    else:
        led.value = False

    # The commented out code is not part of the actual code but is needed to get it working by uncommenting it and then recommenting it
    #time.sleep(delay_between_sonar_cheeks)