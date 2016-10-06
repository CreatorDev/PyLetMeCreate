#!/usr/bin/env python3
"""Python binding of Relay2 Click Wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable_relay_1(mikrobus_index):
    """Enable relay 1.

    Note: An exception is thrown if it fails to enable relay 1.
    """
    ret = _LIB.relay2_click_enable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click enable relay 1 failed")


def disable_relay_1(mikrobus_index):
    """Disable relay 1.

    Note: An exception is thrown if it fails to disable relay 1.
    """
    ret = _LIB.relay2_click_disable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click disable relay 1 failed")


def enable_relay_2(mikrobus_index):
    """Enable relay 2.

    Note: An exception is thrown if it fails to enable relay 2.
    """
    ret = _LIB.relay2_click_enable_relay_2(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click enable relay 2 failed")


def disable_relay_2(mikrobus_index):
    """Disable relay 2.

    Note: An exception is thrown if it fails to disable relay 2.
    """
    ret = _LIB.relay2_click_disable_relay_2(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click disable relay 2 failed")
