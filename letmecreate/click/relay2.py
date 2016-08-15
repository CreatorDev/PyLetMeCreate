#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def enable_relay_1(mikrobus_index):
    ret = _lib.relay2_click_enable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click enable relay 1 failed")


def disable_relay_1(mikrobus_index):
    ret = _lib.relay2_click_disable_relay_1(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click disable relay 1 failed")


def enable_relay_2(mikrobus_index):
    ret = _lib.relay2_click_enable_relay_2(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click enable relay 2 failed")


def disable_relay_2(mikrobus_index):
    ret = _lib.relay2_click_disable_relay_2(mikrobus_index)
    if ret < 0:
        raise Exception("relay2 click disable relay 2 failed")

