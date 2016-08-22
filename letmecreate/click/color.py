#!/usr/bin/env python3
"""Python binding of Color Click wrapper of LetMeCreate library.

You must initialise and select the right I2C bus before using any of these
functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable the Color Click.

    Note: An exception is thrown if it fails to enable the sensor.
    """
    ret = _LIB.color_click_enable()
    if ret < 0:
        raise Exception("color click enable failed")


def get_color():
    """Returns the color measurement as a tuple.

    The Color Click measures the intensity of the light by component and also
    the general intensity. The Color Click must be enabled before calling this
    function.

    Note: An exception is thrown if it fails to measure the color intensity.
    """
    clear = ctypes.c_uint16(0)
    red = ctypes.c_uint16(0)
    green = ctypes.c_uint16(0)
    blue = ctypes.c_uint16(0)
    ret = _LIB.color_click_get_color(ctypes.byref(clear),
                                     ctypes.byref(red),
                                     ctypes.byref(green),
                                     ctypes.byref(blue))
    if ret < 0:
        raise Exception("color click get color failed")

    return (clear.value, red.value, green.value, blue.value)


def disable():
    """Disable the Color Click.

    Note: An exception is thrown if it fails to disable the sensor.
    """
    ret = _LIB.color_click_disable()
    if ret < 0:
        raise Exception("color click disable failed")
