#!/usr/bin/env python3
"""This example shows how to display a number using the 8x8 Click on
Mikrobus 1.
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
