#!/usr/bin/env python3
"""This example shows how to use the Proximity Click wrapper of the LetMeCreate
library.

It reads one proximity measurement from the click and exits.

The Proximity Click must be inserted in Mikrobus 1 before running this program.
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
