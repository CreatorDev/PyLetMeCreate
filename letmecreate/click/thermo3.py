#!/usr/bin/env python3
"""Python binding of Thermo3 Click wrapper of LetMeCreate library.

You must configure and select the right I2C bus before using any of these
functions.
"""
import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = [None, None]


def enable(add_bit):
    """Enable Thermo3 Click.

    add_bit: A jumper is present on the Thermo3 Click which modifies the I2C
    slave address of the chip. Set this variable to 0 or 1 according to the
    state of the jumper.

    Note: An exception is thrown if it fails to enable the Thermo3 Click.
    """
    ret = _LIB.thermo3_click_enable(add_bit)
    if ret < 0:
        raise Exception("thermo3 click enable failed")


def get_temperature():
    """Returns temperature measure.

    Note: An exception is thrown if it fails to read the temperature from the
    chip.
    """
    temperature = ctypes.c_float(0)
    ret = _LIB.thermo3_click_get_temperature(ctypes.byref(temperature))
    if ret < 0:
        raise Exception("thermo3 click get temperature failed")
    return temperature.value


def set_alarm(mikrobus_index, threshold, callback):
    """Triggers a callback if the temperature exceeds a threshold.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    threshold: Floating point variable.

    callback: Function to call if temperature is over threshold.

    Note: An exception is thrown if it fails to set the alarm.
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.thermo3_click_set_alarm(mikrobus_index, threshold, ptr)
    if ret < 0:
        raise Exception("thermo3 click set alarm failed")
    _CALLBACKS[mikrobus_index] = callback


def disable():
    """Disable Thermo3 Click.

    Note: An exception is thrown if it fails to disable the chip.
    """
    ret = _LIB.thermo3_click_disable()
    if ret < 0:
        raise Exception("thermo3 click disable failed")
