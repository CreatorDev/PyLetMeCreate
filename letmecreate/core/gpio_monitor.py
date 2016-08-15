#!/usr/bin/env python3

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = {}

# GPIO events
GPIO_RAISING = 0x01
GPIO_FALLING = 0x02
GPIO_EDGE = GPIO_RAISING | GPIO_FALLING


def init():
    global _CALLBACKS
    ret = _LIB.gpio_monitor_init()
    if ret < 0:
        raise Exception("gpio monitor init failed")
    _CALLBACKS = {}


def add_callback(gpio_pin, event_mask, callback):
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.gpio_monitor_add_callback(gpio_pin, event_mask, ptr)
    if ret < 0:
        raise Exception("gpio monitor add callback failed")
    _CALLBACKS[ret] = ptr


def remove_callback(callback_id):
    ret = _LIB.gpio_monitor_remove_callback(callback_id)
    if ret < 0:
        raise Exception("gpio monitor remove callback failed")
    del _CALLBACKS[callback_id]


def release():
    ret = _LIB.gpio_monitor_release()
    if ret < 0:
        raise Exception("gpio monitor release failed")
