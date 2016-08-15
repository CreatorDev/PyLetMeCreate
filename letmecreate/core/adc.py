#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')


def get_value(mikrobus_index):
    value = ctypes.c_float(0)
    ret = _lib.adc_get_value(mikrobus_index, ctypes.byref(value))
    if ret < 0:
        raise Exception("adc get value failed")
    return value.value
