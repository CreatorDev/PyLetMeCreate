#!/usr/bin/env python3
"""This example shows how to use the Alphanum Click wrapper of the LetMeCreate
to display characters.

It displays "Ci" using both displays by enabling them one after the other at
100Hz to give the illusion that both characters are displayed at the same
time. The user has to interrupt the program to exit it by pressing Ctrl+C.
 *
The Alphanum Click must be inserted in Mikrobus 1 before running this
program.
""""

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
