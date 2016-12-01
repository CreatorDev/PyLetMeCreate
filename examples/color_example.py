#!/usr/bin/env python3

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
