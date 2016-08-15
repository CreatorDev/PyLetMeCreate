#!/usr/bin/env python3
"""Python binding of UART wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')

# Baudrates
UART_BD_1200 = 1200
UART_BD_2400 = 2400
UART_BD_4800 = 4800
UART_BD_9600 = 9600
UART_BD_19200 = 19200
UART_BD_38400 = 38400
UART_BD_57600 = 57600


def init():
    """Initialise UART on all mikrobus.

    UART buses are configured:
      - baudrate: 9600
      - one stop bit
      - no parity bit

    The current bus is set to MIKROBUS_1.

    Note: An exception is thrown if an error occurs during initialisation.
    """
    ret = _LIB.uart_init()
    if ret < 0:
        raise Exception("uart init failed")


def select_bus(mikrobus_index):
    """Selects the current UART bus.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: If the mikrobus index is invalid, then this function does not nothing.
    """
    _LIB.uart_select_bus(mikrobus_index)


def get_current_bus():
    """Returns the current UART bus: 0 (MIKROBUS_1) or 1 (MIKROBUS_2)."""
    return  _LIB.uart_get_current_bus()


def set_baudrate(baudrate):
    """"Set the baudrate of the current UART bus.

    baudrate: Must be one of the predefined baudrates.

    Note: An exception is thrown, if it fails to set the baudrate.
    """
    ret = _LIB.uart_set_baudrate(baudrate)
    if ret < 0:
        raise Exception("uart set baudrate failed")


def get_baudrate():
    """Returns the baudrate of the current UART bus.

    Note: An exception is thrown if it fails to retrieve the baudrate.
    """
    baudrate = ctypes.c_uint32(0)
    ret = _LIB.uart_get_baudrate(ctypes.byref(baudrate))
    if ret < 0:
        raise Exception("uart get baudrate failed")
    return baudrate.value


def send(data):
    """Sends data using the current UART bus.

    data: A list of bytes.

    Note: An exception is thrown if an error occurs during the transmission.
    """
    arr = (ctypes.c_uint8 * len(data))(*data)
    ret = _LIB.uart_send(arr, len(data))
    if ret < 0:
        raise Exception("uart send failed")


def receive(length):
    """Returns a list of bytes.

    This function is blocking and will not returned until length bytes have
    been received.

    length: Number of bytes to receive.

    Note: An exception is thrown if it fails to receive data.
    """
    arr = (ctypes.c_uint8 * length)()
    ret = _LIB.uart_receive(arr, length)
    if ret < 0:
        raise Exception("uart receive failed")
    return [arr[i] for i in range(length)]


def release():
    """Releases all UART bus.

    Note: An exception is thrown if it fails to release all UART buses.
    """
    ret = _LIB.uart_release()
    if ret < 0:
        raise Exception("uart release failed")
