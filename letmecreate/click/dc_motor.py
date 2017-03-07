#!/usr/bin/env python3
"""Python binding of DC motor Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def init(mikrobus_index):
    ret = _LIB.dc_motor_click_init(mikrobus_index)
    if ret < 0:
        raise Exception("dc motor click init failed")


def set_direction(mikrobus_index, direction):
    ret = _LIB.dc_motor_click_set_direction(mikrobus_index, direction)
    if ret < 0:
        raise Exception("dc motor click set direction failed")


def get_direction(mikrobus_index):
    direction = ctypes.c_uint8()
    ret = _LIB.dc_motor_click_set_direction(mikrobus_index, ctypes.byref(direction))
    if ret < 0:
        raise Exception("dc motor click get direction failed")
    return direction.value


def set_speed(mikrobus_index, speed):
    ret = _LIB.dc_motor_click_set_speed(mikrobus_index, speed)
    if ret < 0:
        raise Exception("dc motor click set speed failed")


def get_speed(mikrobus_index):
    speed = ctypes.c_float()
    ret = _LIB.dc_motor_click_get_speed(mikrobus_index, ctypes.byref(speed))
    if ret < 0:
        raise Exception("dc motor click get speed failed")
    return speed.value


def release(mikrobus_index):
    ret = _LIB.dc_motor_click_release(mikrobus_index)
    if ret < 0:
        raise Exception("dc motor click release failed")
