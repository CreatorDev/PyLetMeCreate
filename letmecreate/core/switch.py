#!/usr/bin/env python3
"""Python binding of SWITCH wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None)
_CALLBACKS = {}

SWITCH_1_PRESSED = 0x01
SWITCH_1_RELEASED = 0x02
SWITCH_2_PRESSED = 0x04
SWITCH_2_RELEASED = 0x08
SWITCH_ALL_EVENTS = 0x0F


def init():
    """Initialise the switch.

    Note: An exception is thrown if an error occurs during initialisation.
    """
    global _CALLBACKS
    ret = _LIB.switch_init()
    if ret < 0:
        raise Exception("switch init failed")
    _CALLBACKS = {}


def add_callback(event_mask, callback):
    """Add a callback. Returns a callback ID.

    event_mask: must be in range 1..15.

    callback: Function to call if event happens.

    Note: An exception is thrown if it fails to add the callback.
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.switch_add_callback(event_mask, ptr)
    if ret < 0:
        raise Exception("switch add callback failed")
    _CALLBACKS[ret] = ptr


def remove_callback(callback_id):
    """Removes callback

    callback_id: must be a positive integer returned by a previous call to
    add_callback.

    Note: An exception is thrown if it fails to remove the callback.
    """
    ret = _LIB.switch_remove_callback(callback_id)
    if ret < 0:
        raise Exception("switch remove callback failed")
    del _CALLBACKS[callback_id]


def release():
    """Release the switch wrapper.

    All callbacks are destroyed.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.switch_release()
    if ret < 0:
        raise Exception("switch release failed")
