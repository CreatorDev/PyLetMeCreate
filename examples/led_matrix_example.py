#!/usr/bin/env python3
"""This example shows how to use the 8x8R Click wrapper of the LetMeCreate.

It gradually turns on all the LED's of the led matrix (8x8R Click) from the
bottom-right corner to the top-left corner.

The 8x8R Click must be inserted in Mikrobus 1 before running this program.
"""

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import spi
from letmecreate.click import led_matrix
from time import sleep


spi.init()
spi.select_bus(MIKROBUS_1)
led_matrix.enable()
led_matrix.set_intensity(3)

columns = [0] * 8

for cols in range(8):
    for lines in range(8):
        columns[cols] |= 1 << lines
        led_matrix.set_columns(columns)
        sleep(0.04)

led_matrix.disable()
spi.release()
