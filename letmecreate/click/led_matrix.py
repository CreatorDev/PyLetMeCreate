#!/usr/bin/env python3
"""Python binding of 8x8R Click wrapper of LetMeCreate library.

You must initialise the SPI bus and select the right one before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def enable():
    """Enable the Led Matrix.

    Switch off all LED's and set the intensity to its maximum.

    Note: An exception is thrown if it fails to enable the chip.
    """
    ret = _LIB.led_matrix_click_enable()
    if ret < 0:
        raise Exception("led matrix click enable failed")


def set_intensity(intensity):
    """Sets the intensity of the led matrix.

    intensity: must be in range 0-15.

    Note: An exception is thrown if it fails to set the intensity.
    """
    ret = _LIB.led_matrix_click_set_intensity(intensity)
    if ret < 0:
        raise Exception("led matrix click set intensity failed")


def set_column(column_index, data):
    """Switch on/off LED's of one column.

    column_index: must be in range 0-7.

    data: A 8-bit integer. data is interpreted as a bit string. LED's, whose
    corresponding bits are 1, are switched on, otherwise they are switched off.

    Note: An exception is thrown if it fails to switch on/off LED's of a
    column.
    """
    ret = _LIB.led_matrix_click_set_column(column_index, data)
    if ret < 0:
        raise Exception("led matrix click set column failed")


def display_number(number):
    """Displays a decimal number on the LED matrix.

    number: must be in range 0-99

    Note: An exception is thrown if it fails to display the number.
    """
    ret = _LIB.led_matrix_click_display_number(number)
    if ret < 0:
        raise Exception("led matrix click display number failed")


def set_columns(columns):
    """Switch on/off LED's of the LED matrix.

    columns: A list of bytes of length 8. Each element is an integer
    interpreted as a bit string. LED's, whose corresponding bits are set to 1,
    are switched on, otherwise they are switched off.

    Note: An exception is thrown if it fails to switch on/off LED's.
    """
    data = (ctypes.c_uint8 * len(columns))(*columns)
    ret = _LIB.led_matrix_click_set(data)
    if ret < 0:
        raise Exception("led matrix click set columns failed")


def disable():
    """Disables the LED matrix.

    All LED's are switched off.

    Note: An exception is thrown if it fails to disable the LED matrix.
    """
    ret = _LIB.led_matrix_click_disable()
    if ret < 0:
        raise Exception("led matrix click disable failed")
