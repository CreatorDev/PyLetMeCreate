#!/usr/bin/env python3
"""Python binding of Proximity Click wrapper of LetMeCreate library.

You must configure and select the right I2C bus before using any of these
functions.
"""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable the Proximity Click.

    Note: An exception is thrown if it fails to enable the sensor.
    """
    ret = _LIB.proximity_click_enable()
    if ret < 0:
        raise Exception("proximity click enable failed")


def get_measure():
    """Returns a measure read from Proximity Click.

    Note: An exception is thrown if it fails to get a measure from the
    Proximity Click.
    """
    measure = ctypes.c_uint16(0)
    ret = _LIB.proximity_click_get_measure(ctypes.byref(measure))
    if ret < 0:
        raise Exception("proximity click get measure failed")
    return measure.value


def disable():
    """Disables the Proximity Click.

    Note: An exception is thrown if it fails to disable the sensor.
    """
    ret = _LIB.proximity_click_disable()
    if ret < 0:
        raise Exception("proximity click disable failed")
