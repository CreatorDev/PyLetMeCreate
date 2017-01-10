#!/usr/bin/env python3
"""This example shows how to use the Color2 Click wrapper of the LetMeCreate
library.

The Color2 Click must be plugged in Mikrobus 1 of Ci40.
"""

from letmecreate.core import i2c
from letmecreate.click import color2


i2c.init()
color2.enable()

measure = color2.get_color()
color2.disable()
i2c.release()

print('red  : {}'.format(measure[0]))
print('green: {}'.format(measure[1]))
print('blue : {}'.format(measure[2]))
