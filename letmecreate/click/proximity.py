#!/usr/bin/env python3

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    ret = _LIB.proximity_click_enable()
    if ret < 0:
        raise Exception("proximity click enable failed")


def get_measure():
    measure = ctypes.c_uint16(0)
    ret = _LIB.proximity_click_get_measure(ctypes.byref(measure))
    if ret < 0:
        raise Exception("proximity click get measure failed")
    return measure.value


def disable():
    ret = _LIB.proximity_click_disable()
    if ret < 0:
        raise Exception("proximity click disable failed")
