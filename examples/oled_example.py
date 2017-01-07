#!/usr/bin/env python3
"""This example shows how to use the OLED Click wrapper of the LetMeCreate library.

It displays some text for three seconds and then, it exits.

The OLED Click must be inserted in Mikrobus 1 before running this program.
In addition, the OLED Click must be configured to use I2C.
"""

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
