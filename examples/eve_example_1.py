#!/usr/bin/env python3
"""This example shows some basic features of the EVE Click wrapper of the
LetMeCreate library.

It displays a green screen for three seconds, then displays some text for
another three seconds.

Before running this program:
  - the EVE Click must be inserted in Mikrobus 1
  - a WQVGA screen must be connected to the EVE Click.
"""

from letmecreate.core import spi
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import eve
from time import sleep

spi.init();
spi.set_mode(MIKROBUS_1, 0)

eve.enable(MIKROBUS_1)

# Display a green screen for 3 seconds
eve.clear(0, 255, 0)
eve.display()

sleep(3)

# Display some text
eve.clear(0, 0, 0)
eve.draw(eve.FT800_TEXT,
         [240,                              # x
          136,                               # y
          31,                                # font (31 is the largest font)
          eve.FT800_OPT_CENTER,              # options
          "Hello World !".encode('utf-8')])  # All strings must be encoded
eve.display()

sleep(3)

eve.disable(MIKROBUS_1)
spi.release()
