#!/usr/bin/env python3
"""Python binding of UNI HALL Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = [None, None]


def attach_callback(mikrobus_index, callback):
    """Call function when north pole is detected.

    mikrobus_index: 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.uni_hall_click_attach_callback(mikrobus_index, ptr)
    if ret < 0:
        raise Exception("UNI HALL attach callback failed")
    _CALLBACKS[mikrobus_index] = ptr
