#!/usr/bin/env python3
"""Python binding of Joystick wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_x():
    """Returns the X position of the joystick.

    Note: An exception is thrown if it fails to read the X position from the
    chip.
    """
    pos_x = ctypes.c_int8(0)
    ret = _LIB.joystick_click_get_x(ctypes.byref(pos_x))
    if ret < 0:
        raise Exception("joystick click get x failed")
    return pos_x.value


def get_y():
    """Returns the Y position of the joystick.

    Note: An exception is thrown if it fails to read the Y position from the
    chip.
    """
    pos_y = ctypes.c_int8(0)
    ret = _LIB.joystick_click_get_y(ctypes.byref(pos_y))
    if ret < 0:
        raise Exception("joystick click get y failed")
    return pos_y.value


def get_position():
    """Returns the X position of the joystick.

    Note: An exception is thrown if it fails to read the position from the
    chip.
    """
    pos_x = ctypes.c_int8(0)
    pos_y = ctypes.c_int8(0)
    ret = _LIB.joystick_click_get_position(ctypes.byref(pos_x),
                                           ctypes.byref(pos_y))
    if ret < 0:
        raise Exception("joystick click get position failed")
    return (pos_x.value, pos_y.value)
