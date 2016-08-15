#!/usr/bin/env python3
"""This example shows how to read the temperature using a Thermo3 Click
on Mikrobus 1.
"""

from letmecreate.core import i2c
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import thermo3


# Initialise I2C on Mikrobus 1
i2c.init()
i2c.select_bus(MIKROBUS_1)

# Read temperature
thermo3.enable(0)
print('{} degrees celsius'.format(thermo3.get_temperature()))
thermo3.disable()

# Release I2C
i2c.release()
