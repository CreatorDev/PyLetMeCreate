#!/usr/bin/env python3
"""This examples show how to use some features of the LED wrapper of the
LetMeCreate library.

It turns on gradually all the LED's present on the Ci40 from left to right in
1.6 second. This operation is repeated three times.
"""

from letmecreate.core import led
from time import sleep


led.init()

for i in range(10):
    led.switch_on(led.ALL_LEDS)
    sleep(0.1) # Wait 100ms
    led.switch_off(led.ALL_LEDS)
    sleep(0.4) # Wait 400ms

led.release()
