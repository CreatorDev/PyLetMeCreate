#!/usr/bin/env python3
"""This examples shows how to use the Relay2 Click wrapper of the LetMeCreate
library.

It switches on/off relays in the following order:
    - relay 1 off, relay 2 off
    - relay 1 on, relay 2 off
    - relay 1 off, relay 2 on
    - relay 1 on, relay 2 on

Relay2 Click must be inserted in mikrobus 1 before running this program.
"""
from letmecreate.click import relay2
from letmecreate.click.relay2 import RELAY2_CLICK_RELAY_1, RELAY2_CLICK_RELAY_2
from letmecreate.core.common import MIKROBUS_1
from time import sleep


counter = 0
while True:
    tmp = counter % 4
    if tmp == 0:
        relay2.disable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_1)
        relay2.disable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_2)
    elif tmp == 1:
        relay2.enable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_1)
        relay2.disable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_2)
    elif tmp == 2:
        relay2.disable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_1)
        relay2.enable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_2)
    elif tmp == 3:
        relay2.enable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_1)
        relay2.enable_relay(MIKROBUS_1, RELAY2_CLICK_RELAY_2)

    sleep(1)
    counter = counter + 1
