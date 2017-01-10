#!/usr/bin/env python3
"""Python binding of Relay2 Click Wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')

RELAY2_CLICK_RELAY_1 = 0
RELAY2_CLICK_RELAY_2 = 1
RELAY2_CLICK_RELAY_COUNT = 2


def enable_relay(mikrobus_index, relay):
    """Enable a relay (0 if off, 1 if on).

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    relay: must be 0 (RELAY2_CLICK_RELAY_1) or 1 (RELAY2_CLICK_RELAY_2)

    Note: An exception is throw if it fails to enable a relay.
    """
    ret = _LIB.relay2_click_enable_relay(mikrobus_index, relay)
    if ret < 0:
        raise Exception("relay2 click enable relay failed")


def disable_relay(mikrobus_index, relay):
    """Disable a relay (0 if off, 1 if on).

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    relay: must be 0 (RELAY2_CLICK_RELAY_1) or 1 (RELAY2_CLICK_RELAY_2)

    Note: An exception is throw if it fails to disable a relay.
    """
    ret = _LIB.relay2_click_disable_relay(mikrobus_index, relay)
    if ret < 0:
        raise Exception("relay2 click disable relay failed")


def set_relay_state(mikrobus_index, relay, state):
    """Set state of a relay (0 if off, 1 if on).

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    relay: must be 0 (RELAY2_CLICK_RELAY_1) or 1 (RELAY2_CLICK_RELAY_2)

    Note: An exception is throw if it fails to set the state of a relay.
    """
    ret = _LIB.relay2_click_set_relay_state(mikrobus_index, relay, state)
    if ret < 0:
        raise Exception("relay2 click set relay state failed")


def get_relay_state(mikrobus_index, relay):
    """Get state of a relay (0 if off, 1 if on).

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    relay: must be 0 (RELAY2_CLICK_RELAY_1) or 1 (RELAY2_CLICK_RELAY_2)

    Note: An exception is throw if it fails to get the state of a relay.
    """
    state = ctypes.c_uint8(0)
    ret = _LIB.relay2_click_get_relay_state(mikrobus_index,
                                            relay,
                                            ctypes.byref(state))
    if ret < 0:
        raise Exception("relay2 click get relay state failed")
    return state.value
