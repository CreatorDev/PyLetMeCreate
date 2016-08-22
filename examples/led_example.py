#!/usr/bin/env python3
"""This example flashes all LED's 10 times."""

from letmecreate.core import led
from time import sleep


led.init()

for i in range(10):
    led.switch_on(led.ALL_LEDS)
    sleep(0.1) # Wait 100ms
    led.switch_off(led.ALL_LEDS)
    sleep(0.4) # Wait 400ms

led.release()
