#!/usr/bin/env python3

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = [None, None]


def enable(add_bit):
    ret = _LIB.thermo3_click_enable(add_bit)
    if ret < 0:
        raise Exception("thermo3 click enable failed")


def get_temperature():
    temperature = ctypes.c_float(0)
    ret = _LIB.thermo3_click_get_temperature(ctypes.byref(temperature))
    if ret < 0:
        raise Exception("thermo3 click get temperature failed")
    return temperature.value


def set_alarm(mikrobus_index, threshold, callback):
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.thermo3_click_set_alarm(mikrobus_index, threshold, ptr)
    if ret < 0:
        raise Exception("thermo3 click set alarm failed")
    _CALLBACKS[mikrobus_index] = callback


def disable():
    ret = _LIB.thermo3_click_disable()
    if ret < 0:
        raise Exception("thermo3 click disable failed")
