#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')

# GPIO pin number
MIKROBUS_1_AN  = 22
MIKROBUS_1_RST = 23
MIKROBUS_1_PWM = 73
MIKROBUS_1_INT = 21
MIKROBUS_2_AN  = 25
MIKROBUS_2_RST = 27
MIKROBUS_2_PWM = 74
MIKROBUS_2_INT = 24
GPIO_14        = 14
GPIO_21        = 21
GPIO_22        = 22
GPIO_23        = 23
GPIO_24        = 24
GPIO_25        = 25
GPIO_27        = 27
GPIO_31        = 31
GPIO_73        = 73
GPIO_74        = 74
GPIO_75        = 75
GPIO_88        = 88
GPIO_89        = 89
GPIO_72        = 72
GPIO_80        = 80
GPIO_81        = 81
GPIO_82        = 82
GPIO_83        = 83
GPIO_84        = 84
GPIO_85        = 85

# GPIO direction
GPIO_OUTPUT = 0
GPIO_INPUT  = 1


def init(gpio_pin):
    ret = _lib.gpio_init(gpio_pin)
    if ret < 0:
        raise Exception("gpio init failed")


def set_direction(gpio_pin, direction):
    ret = _lib.gpio_set_direction(gpio_pin, direction)
    if ret < 0:
        raise Exception("gpio set direction failed")


def get_direction(gpio_pin):
    direction = ctypes.c_uint8(0)
    ret = _lib.gpio_get_direction(gpio_pin, ctypes.byref(direction))
    if ret < 0:
        raise Exception("gpio get direction failed")
    return direction.value


def set_value(gpio_pin, value):
    ret = _lib.gpio_set_value(gpio_pin, value)
    if ret < 0:
        raise Exception("gpio set value failed")


def get_value(gpio_pin):
    value = ctypes.c_uint8(0)
    ret = _lib.gpio_get_value(gpio_pin, ctypes.byref(value))
    if ret < 0:
        raise Exception("gpio get direction failed")
    return value.value


def release(gpio_pin):
    ret = _lib.gpio_release(gpio_pin)
    if ret < 0:
        raise Exception("gpio get direction failed")
