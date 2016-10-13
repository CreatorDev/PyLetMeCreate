#!/usr/bin/env python3
"""Python binding of CO Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_measure(mikrobus_index):
    """Measure the CO concentration in the air using the CO click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to communicate with the CO click.
    """
    value = ctypes.c_uint16_t(0)
    ret = _LIB.co_click_get_measure(mikrobus_index, ctypes.byref(value))
    if ret < 0:
        raise Exception("co click read ppm failed")
    return value.value
