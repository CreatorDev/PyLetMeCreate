#!/usr/bin/env python3
"""This example shows how to use the RpiSenseHat wrapper of the LetMeCreate
library.

It reads the temperature, humidity and pressure from sensors on the board.
Then, it displays a rainbow on the led matrix for 5 seconds.

The RpiSenseHat must be inserted in the RpiSenseHat header before running this
program.
"""


from letmecreate.core import i2c
from letmecreate import rpisensehat
from time import sleep


i2c.init()
rpisensehat.init()

print('temperature: {} degrees celsius'.format(rpisensehat.get_temperature()))
print('humidity: {}%'.format(rpisensehat.get_humidity()))
print('pressure: {}hPa'.format(rpisensehat.get_pressure()))

rpisensehat.display_rainbow()

sleep(5)

rpisensehat.release()
i2c.release()
