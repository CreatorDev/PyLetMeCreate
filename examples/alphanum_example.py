#!/usr/bin/env python3
"""This example shows how to use the Alphanum Click wrapper of the LetMeCreate
to display characters.

It displays "Ci" during 5 seconds

The Alphanum Click must be inserted in Mikrobus 1 before running this
program.
"""

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import spi
from letmecreate.click import alphanum
from time import sleep


spi.init()
alphanum.init(MIKROBUS_1)
alphanum.write('C', 'i')

sleep(5)

alphanum.release()
spi.release()
