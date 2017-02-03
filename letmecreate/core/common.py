#!/usr/bin/env python3
"""Define constants for mikrobus index."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')

MIKROBUS_1 = 0
MIKROBUS_2 = 1
MIKROBUS_COUNT = 2


def check_valid_mikrobus(mikrobus_index):
    """Check if mikrobus exists
        Returns 0 if succesful, -1 otherwise.
    """
    return _LIB.check_valid_mikrobus(mikrobus_index)
