#!/usr/bin/env python3
"""Python binding of Alphanum Click wrapper of LetMeCreate library.

This wrapper only supports SPI protocol to communicate with the click board.
You must initialise the SPI bus and select the right bus before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def init(mikrobus_index):
    """Initialise the Alphanum Click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to initialise the click board.
    """
    ret = _LIB.alphanum_click_init(mikrobus_index)
    if ret < 0:
        raise Exception("alphanum click init failed")


def get_char(c):
    """Convert a character to a 16bit value.

    c: Character to convert. Must be a letter or a number of any of these
    characters: -./:;<=>?@[]\^_

    Note: An exception is thrown if it fails to convert the character.
    """
    value = ctypes.c_uint16(0)
    ret = _LIB.alphanum_click_get_char(c, ctypes.byref(value))
    if ret < 0:
        raise Exception("alphanum click get char failed")
    return value.measure


def write(a, b):
    """Write two characters.

    a: Character on left display

    b: Character on right display

    Note: An exception is thrown if it fails to write these two characters.
    """
    ret = _LIB.alphanum_click_write(a, b)
    if ret < 0:
        raise Exception("alphanum click write failed")


def raw_write(a, b):
    """Write two 16bit value

    a: Value on left display

    b: Value on right display

    Note: An exception is thrown if it fails to write these two values.
    """
    ret = _LIB.alphanum_click_raw_write(a, b)
    if ret < 0:
        raise Exception("alphanum click raw write failed")


def select_left_display():
    """Select left display.

    This function will enable the left display and disable the right display.

    Note: An exception is thrown if it fails to select the left display.
    """
    ret = _LIB.alphanum_click_select_left_display()
    if ret < 0:
        raise Exception("alphanum click select left display failed")


def select_right_display():
    """Select right display.

    This function will enable the right display and disable the left display.

    Note: An exception is thrown if it fails to select the right display.
    """
    ret = _LIB.alphanum_click_select_right_display()
    if ret < 0:
        raise Exception("alphanum click select right display failed")
