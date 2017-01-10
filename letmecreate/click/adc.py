#!/usr/bin/env python3
"""Python binding of ADC Click Wrapper of LetMeCreate library.

You must initialise the SPI bus and select the right one before calling
get_raw_value.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')

ADC_CLICK_CHANNEL_1 = 0
ADC_CLICK_CHANNEL_2 = 1
ADC_CLICK_CHANNEL_3 = 2
ADC_CLICK_CHANNEL_4 = 3
ADC_CLICK_CHANNEL_COUNT = 4


def get_raw_value(channel):
    """Read raw value from ADC Click in range 0..4095

    channel: must be in range 0-3. Channel 2 is not available on Ci40.

    Note: An exception is thrown if it fails to communicate with the click.
    """
    value = ctypes.c_uint16(0)
    ret = _LIB.adc_click_get_raw_value(channel, ctypes.byref(value))
    if ret < 0:
        raise Exception("adc click get raw value failed")
    return value.value
