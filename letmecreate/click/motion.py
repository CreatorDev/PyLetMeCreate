#!/usr/bin/env python3
"""Python binding of Motion Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = [None, None]


def enable(mikrobus_index):
    """Enable the motion click.

    Configures the EN pin as an output and set it to high.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to enable the Motion Click.
    """
    ret = _LIB.motion_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("motion click enable failed")


def attach_callback(mikrobus_index, callback):
    """Attach a callback triggered if an event is detected.

    Returns the callback ID. The callback must be removed by calling
    letmecreate.core.gpio_monitor.remove_callback().

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    callback: function must have one argument which can be safely ignored. This
    argument indicates if the GPIO is on a falling or raising edge. In this
    case, it triggers an event only if the INT pin is raising so this argument
    will always be equal to 1.

    Note: An exception is thrown if it fails to attach a callback.
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.motion_click_attach_callback(mikrobus_index, ptr)
    if ret < 0:
        raise Exception("motion click attach callback failed")
    _CALLBACKS[mikrobus_index] = ptr


def disable(mikrobus_index):
    """Disable the Motion Click.

    Note: An exception is thrown if it fails to disable the Motion Click.
    """
    ret = _LIB.motion_click_disable(mikrobus_index)
    if ret < 0:
        raise Exception("motion click disable failed")
