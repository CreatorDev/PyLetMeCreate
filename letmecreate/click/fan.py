#!/usr/bin/env python3
"""Python binding of Fan Click wrapper of LetMeCreate library.

You must configure and select the right I2C bus before using any of these
functions.
"""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def init():
    """Initialise the Fan Click.

    Note: An exception is thrown if it fails to initialise the click board.
    """
    ret = _LIB.fan_click_init()
    if ret < 0:
        raise Exception("fan click init failed")


def set_speed(rpm):
    """Set speed of fan.

    rpm: target speed of fan in rpm, must be in range 600..2500

    Note: An exception is thrown if it fails to set the speed.
    """
    ret = _LIB.fan_click_set_speed(rpm)
    if ret < 0:
        raise Exception("fan click set speed failed")
