#!/usr/bin/env python3
"""Python binding of Light Click wrapper of LetMeCreate library.

If you choose to use SPI to communicate with the board, then you must
initialise the SPI bus and select the right bus before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def get_measure(mikrobus_index, use_spi):
    """Get a measure from Light Click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    use_spi: 1 if you use SPI (on board ADC) or 0 if you use ADC output
    directly.

    Note: An exception is thrown if it fails to get a measure from the Light
    Click.
    """
    measure = ctypes.c_uint16(0)
    ret = _LIB.light_click_get_measure(mikrobus_index,
                                       ctypes.byref(measure),
                                       use_spi)
    if ret < 0:
        raise Exception("light click get measure failed")
    return measure.value
