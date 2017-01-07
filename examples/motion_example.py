#!/usr/bin/env python3
"""This example shows how to use the Motion Click wrapper of the LetMeCreate
library.

Whenever the motion click detects an event, it flashes all LED's ten times.
The user must press Ctrl+C to terminate the program.

The Motion Click must be inserted in Mikrobus 1 before running this program.
"""

from letmecreate.core.common import MIKROBUS_1
from letmecreate.core import led
from letmecreate.click import motion


def flash_leds(arg):
    # Only flash LED's when motion starts getting detected.
    if arg != 1:
        return

    for i in range(10):
        led.switch_on(led.ALL_LEDS)
        sleep(0.1)
        led.switch_off(led.ALL_LEDS)
        sleep(0.1)


led.init()
motion.enable(MIKROBUS_1)
motion.attach_callback(MIKROBUS_1, flash_leds)

print("LED's will flash when Motion Click detects a movement.\n")
print("Press Ctrl+C to quit.\n")


while True:
    pass
