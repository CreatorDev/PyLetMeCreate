#!/usr/bin/env python3
"""Python binding of Relay4 Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable(relay_0_pin, relay_1_pin, relay_2_pin, relay_3_pin):
    ret = _LIB.relay4_click_enable(relay_0_pin,
                                   relay_1_pin,
                                   relay_2_pin,
                                   relay_3_pin)
    if ret < 0:
        raise Exception("relay4 click enable failed")


def disable():
    ret = _LIB.relay4_click_disable()
    if ret < 0:
        raise Exception("relay4 click disable failed")


def set_state(index, state):
    ret = _LIB.relay4_click_set_state(index, state)
    if ret < 0:
        raise Exception("relay4 click set state failed")


def get_state(index):
    state = ctypes.c_uint8(0)
    ret = _LIB.relay4_click_get_state(index, ctypes.byref(state))
    if ret < 0:
        raise Exception("relay4 click get state failed")
    return state.value


def toggle(index):
    ret = _LIB.relay4_click_toggle(index)
    if ret < 0:
        raise Exception("relay4 click toggle failed")
