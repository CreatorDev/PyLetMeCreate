#!/usr/bin/env python3
"""This example shows how to display a number using the 7Seg Click on
Mikrobus 1.
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
