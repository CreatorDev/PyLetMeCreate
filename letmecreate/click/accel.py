#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def enable():
    ret = _lib.accel_click_enable()
    if ret < 0:
        raise Exception("accel click enable failed")


def get_measure():
    accel_x = ctypes.c_float(0)
    accel_y = ctypes.c_float(0)
    accel_z = ctypes.c_float(0)
    ret = _lib.accel_click_get_measure(ctypes.byref(accel_x),
                                       ctypes.byref(accel_y),
                                       ctypes.byref(accel_z))
    if ret < 0:
        raise Exception("accel click get measure failed")
    return (accel_x.value, accel_y.value, accel_z.value)


def disable():
    ret = _lib.accel_click_disable()
    if ret < 0:
        raise Exception("accel click disable failed")
