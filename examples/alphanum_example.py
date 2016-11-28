#!/usr/bin/env python3

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import spi
from letmecreate.click import alphanum
import time


spi.init()
alphanum.init(MIKROBUS_1)
alphanum.write('C', 'i')

while True:
    alphanum.select_left_display()
    time.sleep(0.01)
    alphanum.select_right_display()
    time.sleep(0.01)
