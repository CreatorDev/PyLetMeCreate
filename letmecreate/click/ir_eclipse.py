#!/usr/bin/env python3
"""Python binding of IR eclipse Click wrapper of LetMeCreate library."""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = [None, None]


def add_callback(mikrobus_index, callback):
    """Attach a callback.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    callback: Function to call if an event gets detected.

    Note: An exception is thrown if it fails to attach the callback.
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.motion_click_attach_callback(mikrobus_index, ptr)
    if ret < 0:
        raise Exception("motion click attach callback failed")
    _CALLBACKS[mikrobus_index] = ptr
