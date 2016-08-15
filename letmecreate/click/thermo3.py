#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')
callback_type = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
callbacks = [None, None]


def enable(add_bit):
    ret = _lib.thermo3_click_enable(add_bit)
    if ret < 0:
        raise Exception("thermo3 click enable failed")


def get_temperature():
    temperature = ctypes.c_float(0)
    ret = _lib.thermo3_click_get_temperature(ctypes.byref(temperature))
    if ret < 0:
        raise Exception("thermo3 click get temperature failed")
    return temperature.value


def set_alarm(mikrobus_index, threshold, callback):
    ptr = callback_type(callback)
    ret = _lib.thermo3_click_set_alarm(mikrobus_index, threshold, ptr)
    if ret < 0:
        raise Exception("thermo3 click set alarm failed")
    callbacks[mikrobus_index] = callback


def disable():
    ret = _lib.thermo3_click_disable()
    if ret < 0:
        raise Exception("thermo3 click disable failed")
