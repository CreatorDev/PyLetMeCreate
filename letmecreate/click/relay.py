#!/usr/bin/env python3
"""Python binding of Relay Click wrapper of LetMeCreate library."""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable_relay_1(mikrobus_index):
    """Enable relay 1.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to enable relay 1.
    """
    ret = _LIB.relay_click_enable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay click enable relay 1 failed")


def disable_relay_1(mikrobus_index):
    """Disable relay 1.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to disable relay 1.
    """
    ret = _LIB.relay_click_disable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay click disable relay 1 failed")


def set_relay_1_state(mikrobus_index, state):
    """Set state of relay 1.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    state: 0: off, any other value: on

    Note: An exception is thrown if it fails to set state of relay 1.
    """
    ret = _LIB.relay_click_set_relay_1_state(mikrobus_index, state)
    if ret < 0:
        raise Exception("relay click set relay 1 state")


def get_relay_1_state(mikrobus_index):
    """Return state of relay 1. 0 if off, otherwise on

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to set state of relay 1.
    """
    state = ctypes.c_uint8(0)
    ret = _LIB.relay_click_get_relay_1_state(mikrobus_index,
                                             ctypes.byref(state))
    if ret < 0:
        raise Exception("relay click get relay 1 state")
    return state.value
