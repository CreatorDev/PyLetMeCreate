#!/usr/bin/env python3
"""This example shows how to use the 7Seg Click wrapper of the LetMeCreate library.
It displays number from 0 to 99 in 10 seconds.
It assumes that the 7Seg Click is inserted in Mikrobus 1.
"""

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import spi
from letmecreate.click import seven_seg
from time import sleep

spi.init()
seven_seg.set_intensity(MIKROBUS_1, 100.0)
for i in range(100):
    seven_seg.display_decimal_number(i)
    sleep(0.1)
spi.release()
