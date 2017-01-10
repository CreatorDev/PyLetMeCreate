#!/usr/bin/env python3
"""Python binding of LIN HALL Click wrapper of LetMeCreate library.

This wrapper uses SPI to communicate with the click board.
You must initialise the SPI bus and select the right bus before using
any of these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_measure():
    """Read 12bit measurement from LIN Hall Click.

    Note: An exception is thrown if it fails.
    """
    measure = ctypes.c_uint16(0)
    ret = _LIB.lin_hall_click_get_measure(ctypes.byref(measure))
    if ret < 0:
        raise Exception("LIN HALL get measure failed")
    return measure.value
