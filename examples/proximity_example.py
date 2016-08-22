#!/usr/bin/env python3
"""This example shows how to read a measure from the Proximity Click inserted
in Mikrobus 1.
"""

from letmecreate.core import i2c
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import proximity


# Initialise I2C on Mikrobus 1
i2c.init()
i2c.select_bus(MIKROBUS_1)

# Read measure from Proximity Click
proximity.enable()
print('measure: {}'.format(proximity.get_measure()))
proximity.disable()

# Release I2C
i2c.release()
