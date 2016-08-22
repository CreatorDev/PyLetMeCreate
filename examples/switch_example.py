#!/usr/bin/env python3
"""This example shows how to add/remove callbacks to particular switch events.
"""

from letmecreate.core import switch
from letmecreate.core.switch import SWITCH_1_PRESSED, SWITCH_2_PRESSED
from letmecreate.core.switch import SWITCH_1_RELEASED, SWITCH_2_RELEASED
from time import sleep


def switch_pressed():
    print("A switch has been pressed")


def switch_released():
    print("A switch has been released")


# Initialise the switch and attach two callbacks
switch.init()
callback_id_pressed = switch.add_callback(SWITCH_1_PRESSED | SWITCH_2_PRESSED,
                                          switch_pressed)
callback_id_released = switch.add_callback(SWITCH_1_RELEASED|SWITCH_2_RELEASED,
                                           switch_released)

# Sleep main thread during 15 seconds.
# The switch wrapper lives in another thread and will call switch_pressed
# and switch_released
print("Callbacks are now active for 15 seconds.")
sleep(15)

# Remove callbacks and release switch
# In this case, it is not necessary to call switch.remove_callback()
# since callbacks would get destroyed in switch.release().
switch.remove_callback(callback_id_pressed)
switch.remove_callback(callback_id_released)
switch.release()
