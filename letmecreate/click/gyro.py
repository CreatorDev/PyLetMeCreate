#!/usr/bin/env python3
"""Python binding of GYRO wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def use_spi():
    """Use SPI to communicate with the GYRO Click."""
    _LIB.gyro_click_use_spi()


def use_i2c(add_bit):
    """Use I2C to communicate with the GYRO Click.

    add_bit: Corresponds to the state of the jumper present on the board to
    change the address. Must be 0 or 1.
    """
    _LIB.gyro_click_use_i2c(add_bit)


def enable():
    """Enable the GYRO Click.

    By default, it uses I2C to communicate with the click board. I2C or SPI
    must be initialised and the right bus must be selected before attempting
    to call this function.

    Note: An exception is thrown if it fails to enable the GYRO Click.
    """
    ret = _LIB.gyro_click_enable()
    if ret < 0:
        raise Exception("gyro click enable failed")


def get_measure():
    """Read a measurement from the GYRO Click.

    Note: An exception is thrown if it fails to get a measure.
    """
    x = ctypes.c_float(0)
    y = ctypes.c_float(0)
    z = ctypes.c_float(0)
    ret = _LIB.gyro_click_get_measure(ctypes.byref(x),
                                      ctypes.byref(y),
                                      ctypes.byref(z))
    if ret < 0:
        raise Exception("gyro click get measure failed")

    return (x.value, y.value, z.value)


def disable():
    """Disable the GYRO Click.

    Note: An exception is thrown if it fails to disable the GYRO Click.
    """
    ret = _LIB.gyro_click_disable()
    if ret < 0:
        raise Exception("gyro click disable failed")
