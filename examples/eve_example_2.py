#!/usr/bin/env python3
"""This example shows features related to the touch screen of the EVE Click
wrapper of the LetMeCreate library.

It first performs calibration of the touch screen, then it prints the
coordinates of the touch event. Press Ctrl+C to exit program.

Before running this program:
  - the EVE Click must be inserted in Mikrobus 1
  - a WQVGA screen must be connected to the EVE Click.
"""

from letmecreate.core import spi
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import eve

touch_screen_event = False
last_event_x = 0
last_event_y = 0

def callback(x, y):
    global touch_screen_event
    global last_event_x, last_event_y
    last_event_x = x
    last_event_y = y
    touch_screen_event = True


spi.init()
spi.set_mode(MIKROBUS_1, 0)

eve.enable(MIKROBUS_1);

# Perform calibration of touch screen
eve.calibrate()

# Add your own callback after calibration, otherwise you might get
# incorrect coordinates.
eve.attach_touch_callback(callback)

eve.clear(0, 0, 0)
eve.draw(eve.FT800_TEXT,
       [240,
       136,
       31,
       eve.FT800_OPT_CENTER,
       "Tap on the screen".encode('utf-8')])
eve.display()

while True:

    # Wait until the user touches the screen or that it exits
    while not touch_screen_event:
        pass

    eve.clear(0, 0, 0)
    eve.draw(eve.FT800_TEXT,
             [240,
              136,
              25,
              eve.FT800_OPT_CENTER,
              "Touch event detected at:".encode('utf-8')])
    eve.draw(eve.FT800_TEXT,
            [240,
            180,
            25,
            eve.FT800_OPT_CENTER,
            "x: {}, y: {}".format(last_event_x, last_event_y).encode('utf-8')])
    eve.display()

eve.disable(MIKROBUS_1)
spi_release()
