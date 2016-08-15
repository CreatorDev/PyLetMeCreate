#!/usr/bin/env python3
"""Python binding of Accel Click wrapper of LetMeCreate library.

This wrapper only supports SPI protocol to communicate with the click board.
You must initialise the SPI bus and select the right bus before using any of
these functions.
"""

import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable the Accel Click.

    Note: An exception is thrown if it fails to enable the sensor chip.
    """
    ret = _lib.accel_click_enable()
    if ret < 0:
        raise Exception("accel click enable failed")


def get_measure():
    """Returns a measure as a tuple.

    Note: An exception is thrown if it fails to get a measure.
    """
    accel_x = ctypes.c_float(0)
    accel_y = ctypes.c_float(0)
    accel_z = ctypes.c_float(0)
    ret = _lib.accel_click_get_measure(ctypes.byref(accel_x),
                                       ctypes.byref(accel_y),
                                       ctypes.byref(accel_z))
    if ret < 0:
        raise Exception("accel click get measure failed")
    return (accel_x.value, accel_y.value, accel_z.value)


def disable():
    """Disable the Accel Click.

    Note: An exception is thrown if it fails to disable the sensor chip.
    """
    ret = _lib.accel_click_disable()
    if ret < 0:
        raise Exception("accel click disable failed")
