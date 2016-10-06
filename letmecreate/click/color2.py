#!/usr/bin/env python3
"""Python binding of Color2 Click wrapper of LetMeCreate library."""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable the Color2 Click.

    Note: An exception is thrown if it fails to enable the chip.
    """
    ret = _LIB.color2_click_enable()
    if ret < 0:
        raise Exception("color2 click enable failed")


def get_color():
    """Returns the rgb color measurement as a tuple.

    Note: An exception is thrown if it fails to get a measurement from
    the click.
    """
    red = ctypes.c_uint16(0)
    green = ctypes.c_uint16(0)
    blue = ctypes.c_uint16(0)
    ret = _LIB.color2_click_get_color(ctypes.byref(red),
                                      ctypes.byref(green),
                                      ctypes.byref(blue))
    if ret < 0:
        raise Exception("color2 click get color failed")
    return (red.value, green.value, blue.value)


def disable():
    """Disable the Color2 Click.

    Note: An exception is thrown if it fails to disable the chip.
    """
    ret = _LIB.color2_click_disable()
    if ret < 0:
        raise Exception("color2 click disable failed")
