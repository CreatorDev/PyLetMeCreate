#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')
callback_type = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
callbacks = {}

# GPIO events
GPIO_RAISING = 0x01
GPIO_FALLING = 0x02
GPIO_EDGE = GPIO_RAISING | GPIO_FALLING


def init():
    global callbacks
    ret = _lib.gpio_monitor_init()
    if ret < 0:
        raise Exception("gpio monitor init failed")
    callbacks = {}


def add_callback(gpio_pin, event_mask, callback):
    ptr = callback_type(callback)
    ret = _lib.gpio_monitor_add_callback(gpio_pin, event_mask, ptr)
    if ret < 0:
        raise Exception("gpio monitor add callback failed")
    callbacks[ret] = ptr


def remove_callback(callback_id):
    ret = _lib.gpio_monitor_remove_callback(callback_id)
    if ret < 0:
        raise Exception("gpio monitor remove callback failed")
    del callbacks[callback_id]


def release():
    ret = _lib.gpio_monitor_release()
    if ret < 0:
        raise Exception("gpio monitor release failed")
