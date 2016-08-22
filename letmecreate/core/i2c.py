#!/usr/bin/env python3
"""Python binding of I2C wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')


def init():
    """Initialise I2C bus on both mikrobus.

    The current I2C bus is set to MIKROBUS_1.

    Note: If an error occurs during the initialisation, an exception is thrown.
    """
    ret = _LIB.i2c_init()
    if ret < 0:
        raise Exception("i2c init failed")


def select_bus(mikrobus_index):
    """Selects the I2C bus.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2). If any other value
    is given, this function does nothing.
    """
    _LIB.i2c_select_bus(mikrobus_index)


def get_current_bus():
    """Returns the current I2C bus active: 0 for MIKROBUS_1 or 1 for MIKROBUS_2.

    Note: An exception is thrown if it fails to get the current bus.
    """
    current_bus = ctypes.c_uint8(0)
    ret = _LIB.i2c_get_current_bus(ctypes.byref(current_bus))
    if ret < 0:
        raise Exception("i2c get current bus failed")
    return current_bus.value


def write(slave_address, data):
    """Sends data to I2C slave on the current mikrobus.

    slave_address: 7-bit or 12-bit address of I2C slave.

    data: A list of bytes.

    Note: If an error occurs while sending data, an exception is thrown.
    """
    arr = (ctypes.c_uint8 * len(data))(*data)
    ret = _LIB.i2c_write(slave_address, arr, len(data))
    if ret < 0:
        raise Exception("i2c write failed")


def read(slave_address, length):
    """Returns a list of bytes from the I2C slave on the current mikrobus.

    slave_address: 7-bit or 12-bit address of I2C slave.

    length: Number of bytes to read.

    Note: If an error occurs while receiving data, an exception is thrown.
    """
    arr = (ctypes.c_uint8 * length)()
    ret = _LIB.i2c_read(slave_address, arr, length)
    if ret < 0:
        raise Exception("i2c read failed")
    return [arr[i] for i in range(length)]


def write_byte(slave_address, data):
    """Send one byte to I2C slave on the current mikrobus.

    slave_address: 7-bit or 12-bit address of I2C slave.

    data: 8-bit integer to send.

    Note: If an error occurs while sending data, an exception is thrown.
    """
    ret = _LIB.i2c_write_byte(slave_address, data)
    if ret < 0:
        raise Exception("i2c write byte failed")


def read_byte(slave_address):
    """Reads one byte from I2C slave on the current mikrobus.

    slave_address: 7-bit or 12-bit address of I2C slave.

    Note: If an error occurs while receiving data, an exception is thrown.
    """
    data = ctypes.c_uint8(0)
    ret = _LIB.i2c_read_byte(slave_address, ctypes.byref(data))
    if ret < 0:
        raise Exception("i2c write byte failed")
    return data.value


def release():
    """Release I2C bus on both mikrobus.

    Note: An exception is thrown if it fails to release I2C buses.
    """
    ret = _LIB.i2c_release()
    if ret < 0:
        raise Exception("i2c release failed")
