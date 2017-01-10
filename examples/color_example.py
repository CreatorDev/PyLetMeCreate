#!/usr/bin/env python3
"""This example shows how to use the Color Click wrapper of the LetMeCreate.

It takes a measurement from the sensor, prints it in the terminal and exits.

The Color Click must be inserted in Mikrobus 1 before running this program.
"""

from letmecreate.core import i2c
from letmecreate.click import color

i2c.init()
color.enable()
measure = color.get_color()
color.disable()
i2c.release()

print('clear: {}'.format(measure[0]))
print('red  : {}'.format(measure[1]))
print('green: {}'.format(measure[2]))
print('blue : {}'.format(measure[3]))
