#!/usr/bin/env python3
"""Python binding of Air quality Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_measure(mikrobus_index):
    """Measure in the air using the Air Quality click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to communicate with the air
    quality click.
    """
    value = ctypes.c_uint16(0)
    ret = _LIB.air_quality_click_get_measure(mikrobus_index, ctypes.byref(value))
    if ret < 0:
        raise Exception("air quality click read ppm failed")
    return value.value
