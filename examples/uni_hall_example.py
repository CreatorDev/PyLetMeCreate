#!/usr/bin/env python3
"""This example shows how to use the UNI Hall Click binding of LetMeCreate.
"""

from letmecreate.click import uni_hall
from letmecreate.core.common import MIKROBUS_1
from letmecreate.core.gpio_monitor import GPIO_FALLING, GPIO_RAISING
from time import sleep


def print_hello(arg):
    if arg == GPIO_FALLING:
        print("Hello, starts dectecting north pole.")
    elif arg == GPIO_RAISING:
        print("Hello, stops dectecting north pole.")

uni_hall.attach_callback(MIKROBUS_1, print_hello)
print("Callback is now active for 15 seconds.")
print("Move the north pole of a magnet over the sensor to print \"hello\".")
sleep(15)
