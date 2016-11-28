#!/usr/bin/env python3

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import i2c
from letmecreate.click import oled
import time


i2c.init()

oled.enable(MIKROBUS_1)
oled.write_text("Hello   Creator!")
time.sleep(3)
oled.disable()

i2c.release()
