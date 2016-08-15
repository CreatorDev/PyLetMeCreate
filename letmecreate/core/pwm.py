#!/usr/bin/env python3

import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')


def init(mikrobus_index):
    ret = _lib.pwm_init(mikrobus_index)
    if ret < 0:
        raise Exception("pwm init failed")


def enable(mikrobus_index):
    ret = _lib.pwm_enable(mikrobus_index)
    if ret < 0:
        raise Exception("pwm enable failed")


def set_duty_cycle(mikrobus_index, percentage):
    ret = _lib.pwm_set_duty_cycle(mikrobus_index, percentage)
    if ret < 0:
        raise Exception("pwm set duty cycle failed")


def get_duty_cycle(mikrobus_index):
    percentage = ctypes.c_float(0)
    ret = _lib.pwm_get_duty_cycle(mikrobus_index, ctypes.byref(percentage))
    if ret < 0:
        raise Exception("pwm get duty cycle failed")
    return percentage.value


def set_frequency(mikrobus_index, frequency):
    ret = _lib.pwm_set_frequency(mikrobus_index, frequency)
    if ret < 0:
        raise Exception("pwm set frequency failed")


def get_frequency(mikrobus_index):
    frequency = ctypes.c_float(0)
    ret = _lib.gpio_get_frequency(mikrobus_index, ctypes.byref(frequency))
    if ret < 0:
        raise Exception("pwm get frequency failed")
    return frequency.value


def set_period(mikrobus_index, period):
    ret = _lib.pwm_set_period(mikrobus_index, period)
    if ret < 0:
        raise Exception("pwm set period failed")


def get_period(mikrobus_index):
    period = ctypes.c_uint32(0)
    ret = _lib.pwm_get_frequency(mikrobus_index, ctypes.byref(period))
    if ret < 0:
        raise Exception("pwm get period failed")
    return period.value


def disable(mikrobus_index):
    ret = _lib.pwm_disable(mikrobus_index)
    if ret < 0:
        raise Exception("pwm disable failed")


def release(mikrobus_index):
    ret = _lib.pwm_release(mikrobus_index)
    if ret < 0:
        raise Exception("pwm release failed")
