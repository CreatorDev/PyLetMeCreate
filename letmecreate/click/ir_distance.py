#!/usr/bin/env python3
"""Python binding of IR distance Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable(mikrobus_index):
    """Enable IR distance Click.

    Note: An exception is thrown if it fails to enable the device.
    """
    ret = _LIB.ir_distance_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("ir distance click enable failed")


def get_measure(mikrobus_index):
    """Read a measure from IR distance Click.

    The click board must be enabled before calling this function.

    Note: An exception is thrown if it fails to read a measure from the click.
    """
    measure = ctypes.c_uint16(0)
    ret = _LIB.ir_distance_click_get_measure(mikrobus_index,
                                             ctypes.byref(measure))
    if ret < 0:
        raise Exception("ir distance click get measure failed")
    return measure.value


def disable(mikrobus_index):
    """Disable IR distance Click.

    Note: An exception is thrown if it fails to disable the device.
    """
    ret = _LIB.ir_distance_click_disable(mikrobus_index)
    if ret < 0:
        raise Exception("ir distance click disable failed")
