#!/usr/bin/env python3
"""Python binding of RTC Click wrapper of LetMeCreate library.

This clicks uses I2C to communicate with the board. You must initialise the I2C
 bus and select the right bus before using any of these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


class Date(ctypes.Structure):
    """Holds information about a specific date."""
    _fields_ = [
        ("year", ctypes.c_uint16),       # Must be in range year_offset..year_offset+3
        ("month", ctypes.c_uint8),       # Must be in range 0..11
        ("day", ctypes.c_uint8),         # Must be in range 1..31
        ("weekday", ctypes.c_uint8),     # Must be in range 0..6
        ("hour", ctypes.c_uint8),        # Must be in range 0..23
        ("minute", ctypes.c_uint8),      # Must be in range 0..59
        ("second", ctypes.c_uint8),      # Must be in range 0..59
    ]


def init(year_offset):
    """Initialise RTC click.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.rtc_click_init(year_offset)
    if ret < 0:
        raise Exception("rtc click init failed")


def get_date():
    """Reads the date from the RTC Click.

    Note: An exception is thrown if it fails.
    """
    date = Date()
    ret = _LIB.rtc_click_get_date(ctypes.byref(date))
    if ret < 0:
        raise Exception("rtc click get date failed")
    return date


def set_date(date):
    """Set the date of the RTC Click.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.rtc_click_set_date(date)
    if ret < 0:
        raise Exception("rtc click set date failed")
