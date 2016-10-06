#!/usr/bin/env python3
"""Python binding of 7Seg Click wrapper of LetMeCreate library.

You must initialise the SPI bus and select the right one before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def display_decimal_number(dec_num):
    """Display a decimal number on the 7Seg Click.

    dec_num: Number to display, must be in range 0-99.

    Note: An exception is thrown if it fails to display the number.
    """
    ret = _LIB.seven_seg_click_display_decimal_number(dec_num)
    if ret < 0:
        raise Exception("display decimal number on 7seg click failed")


def display_hex_number(hex_num):
    """Display a number as hexadecimal on the 7Seg Click.

    hex_num: Number to display, must be in range 0-255 (0xFF).

    Note: An exception is thrown if it fails to display the number.
    """
    ret = _LIB.seven_seg_click_display_hex_number(hex_num)
    if ret < 0:
        raise Exception("display hex number on 7seg click failed")


def set_intensity(mikrobus_index, intensity):
    """Set the intensity of the LED's of the 7Seg Click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    intensity: Percentage of the intensity of the LED's, must be in range
    0.0-100.0

    Note: An exception is thrown if it fails to set the intensity.
    """
    ret = _LIB.seven_seg_click_set_intensity(mikrobus_index,
                                             ctypes.c_float(intensity))
    if ret < 0:
        raise Exception("set intensity of 7seg click failed")
