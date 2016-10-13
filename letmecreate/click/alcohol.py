#!/usr/bin/env python3
"""Python binding of Alcohol Click wrapper of LetMeCreate library."""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_measure(mikrobus_index):
    """Returns a 16-bit integer from the Accel Click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to get a measure from the click.
    """
    measure = ctypes.c_uint16(0)
    ret = _LIB.alcohol_click_get_measure(mikrobus_index, ctypes.byref(measure))
    if ret < 0:
        raise Exception("alcohol click get measure failed")
    return measure.value
