#!/usr/bin/env python3
"""Python binding of ADC wrapper of LetMeCreate library."""

import ctypes

__author__ = "Francois Berder"
__copyright__ = "Copyright 2016, PyLetMeCreate"
__credits__ = ["Francois Berder"]
__license__ = "BSD"
__version__ = "1.0.1"
__maintainer__ = "Francois Berder"
__email__ = "fberder@outlook.fr"
__status__ = "Development"

_LIB = ctypes.CDLL('libletmecreate_core.so')


def get_value(mikrobus_index):
    """Reads voltage on ADC pin of a mikrobus.

    mikrobus_index: should be 0 for MIKROBUS_1 or 1 for MIKROBUS_2.

    Note: MIKROBUS_1 and MIKROBUS_2 constants are defined in
    letmecreate.core.common.
    """
    value = ctypes.c_float(0)
    ret = _LIB.adc_get_value(mikrobus_index, ctypes.byref(value))
    if ret < 0:
        raise Exception("adc get value failed")
    return value.value
