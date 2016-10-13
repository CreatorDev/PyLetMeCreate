#!/usr/bin/env python3
"""Python binding of Bargraph Click wrapper of LetMeCreate library.

You must configure and select the right SPI bus before using any of these
functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def set_value(value):
    """Switch on/off LED's of the Bargraph Click.

    value: 8-bit integer used as a bit string. Least significant bit
    controls the left-most LED.

    Note: An exception is thrown if it fails to switch on/off LED's.
    """
    ret = _LIB.bargraph_click_set_value(value)
    if ret < 0:
        raise Exception("bargrah click set value failed")


def set_intensity(mikrobus_index, intensity):
    """Control the brightness of the LED's of the Bargraph Click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    intensity: Percentage of intensity of the LED's, must be in range 0.0-10.0

    Note: An exception is thrown if it fails to switch on/off LED's.
    """
    ret = _LIB.bargraph_click_set_intensity(mikrobus_index,
                                            ctypes.c_float(intensity))
    if ret < 0:
        raise Exception("bargrah click set intensity failed")
