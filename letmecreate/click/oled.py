#!/usr/bin/env python3
"""Python binding of OLED Click wrapper of LetMeCreate library.

If you choose to use SPI (or I2C) to communicate with the board, then you must
initialise the SPI (or I2C) bus and select the right bus before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def use_spi():
    """Configure wrapper to use SPI."""
    _LIB.oled_click_use_spi()


def use_i2c():
    """Configure wrapper to use I2C."""
    _LIB.oled_click_use_i2c()


def enable(mikrobus_index):
    """Enable the OLED click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to enable the OLED Click.
    """
    ret = _LIB.oled_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("oled click enable failed")


def set_contrast(contrast):
    """Set the contrast

    contrast: 0 means no contrast, 255 means maximum contrast

    Note: An exception is thrown if it fails to set the contrast.
    """
    ret = _LIB.oled_click_set_contrast(contrast)
    if ret < 0:
        raise Exception("oled click set contrast failed")


def raw_write(data):
    """Write a pixel buffer on the Oled display.

    Each bit of the array represents the state of a pixel. The first 96 bytes
    represent the first page (96x8 pixels), the following 96 bytes represent
    the second page...

    data: Array of bytes of length 384 (96x4).

    Note: An exception is thrown if it fails to display the pixel buffer.
    """
    buf = (ctypes.c_uint8 * 384)(*data)
    ret = _LIB.oled_click_raw_write(buf)
    if ret < 0:
        raise Exception("oled click raw write failed")


def write_text(text):
    """Write some text on the Oled display.

    text: The string must be less or equal than 16 characters.

    Note: An exception is thrown if it fails to write some text.
    """
    ret = _LIB.oled_click_write_text(ctypes.c_char_p(text.encode('utf-8')))
    if ret < 0:
        raise Exception("oled click write text failed")


def get_char(c):
    """Convert a character into an array of 22 bytes.

    c: character to convert (must be between '!' and '~' in the ASCII table)

    Note: An exception is thrown is it fails to convert the character.
    """
    data = (ctypes.c_uint8 * 22)()
    ret = _LIB.oled_click_get_char(c, ctypes.byref(data))
    if ret < 0:
        raise Exception("oled click get char failed")
    return [data[i] for i in range(22)]


def disable():
    """Disable the OLED click.

    Note: An exception is thrown if it fails to disable the oled click.
    """
    ret = _LIB.oled_click_disable()
    if ret < 0:
        raise Exception("oled click disable failed")
