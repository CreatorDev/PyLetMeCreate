#!/usr/bin/env python3

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import spi
from letmecreate.click import bargraph
from time import sleep


spi.init()
bargraph.set_intensity(MIKROBUS_1, 100.0)

value = 1
for i in range(10):
	bargraph.set_value(value)
	value <<= 1
	value |= 1
	sleep(0.2)

spi.release()
