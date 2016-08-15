#!/usr/bin/env python3

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None)
_CALLBACKS = {}

SWITCH_1_PRESSED = 0x01
SWITCH_1_RELEASED = 0x02
SWITCH_2_PRESSED = 0x04
SWITCH_2_RELEASED = 0x08
SWITCH_ALL_EVENTS = 0x0F


def init():
    global _CALLBACKS
    ret = _LIB.switch_init()
    if ret < 0:
        raise Exception("switch init failed")
    _CALLBACKS = {}


def add_callback(event_mask, callback):
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.switch_add_callback(event_mask, ptr)
    if ret < 0:
        raise Exception("switch add callback failed")
    _CALLBACKS[ret] = ptr


def remove_callback(callback_id):
    ret = _LIB.switch_remove_callback(callback_id)
    if ret < 0:
        raise Exception("switch remove callback failed")
    del _CALLBACKS[callback_id]


def release():
    ret = _LIB.switch_release()
    if ret < 0:
        raise Exception("switch release failed")
