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
