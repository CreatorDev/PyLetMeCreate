#!/usr/bin/env python3

from letmecreate.core import spi
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import accel
from time import sleep

spi.init()
spi.select_bus(MIKROBUS_1)
accel.use_spi()
accel.enable()

while True:
	measure = accel.get_measure()
	print('{0:9.3f} {1:9.3f} {2:9.3f}'.format(measure[0], measure[1], measure[2]))
	sleep(0.1)

accel.disable()
spi.release()
