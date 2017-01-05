#!/usr/bin/env python3

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
