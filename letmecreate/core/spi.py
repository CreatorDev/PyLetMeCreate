#!/usr/bin/env python3
"""Python binding of SPI wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')

# SPI_SPEED
SPI_680K = 680000
SPI_1M36 = 1360000
SPI_2M73 = 2730000
SPI_5M46 = 5460000
SPI_10M93 = 10930000
SPI_21M87 = 21870000
SPI_43M75 = 43750000


def init():
    """Initialise SPI on all mikrobus.

    ALL SPI buses are configured as:
      - 8 bits per word
      - 2.73MHz
      - Mode 3

    The current SPI bus is set to MIKROBUS_1.

    Note: An exception is thrown if an error occurs during initialisation.
    """
    ret = _LIB.spi_init()
    if ret < 0:
        raise Exception("spi init failed")


def set_mode(mikrobus_index, mode):
    """Set the spi mode of the current SPI bus.

    The SPI bus must be initialised before calling this function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    mode: must be 0, 1, 2 or 3.

    Note: An exception is thrown if it fails to set the mode.
    """
    ret = _LIB.spi_set_mode(mikrobus_index, mode)
    if ret < 0:
        raise Exception("spi set mode failed")


def set_speed(mikrobus_index, speed):
    """Set the clock speed of the current SPI bus.

    The SPI bus must be initialised before calling this function. The SPI driver
    has only seven different speeds available, defined in #SPI_SPEED. If you try
    to set a speed that is not supported by the driver, it will find the closest
    speed without exceeding it.
    For instance, if you try to set the speed to 3MHz, the actual speed will be
    set to 2.73MHz.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    speed: Clock speed in Hz of the current SPI bus.

    Note: An exception is thrown if it fails to set the mode.
    """
    ret = _LIB.spi_set_speed(mikrobus_index, speed)
    if ret < 0:
        raise Exception("spi set speed failed")


def select_bus(mikrobus_index):
    """Select the SPI bus

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    """
    _LIB.spi_select_bus(mikrobus_index)


def get_current_bus():
    """Returns the currently selected SPI bus."""
    return _LIB.spi_get_current_bus()


def transfer(tx_data):
    """Transfers data using the current SPI bus. Returns a list of bytes.

    tx_data: A list of bytes to send.

    Note: An exception is thrown if an error occurs during the transfer.
    """
    length = len(tx_data)
    tx_buffer = (ctypes.c_uint8 * length)(*tx_data)
    rx_buffer = (ctypes.c_uint8 * length)()
    ret = _LIB.spi_transfer(tx_buffer, rx_buffer, length)
    if ret < 0:
        raise Exception("spi transfer failed")
    return [rx_buffer[i] for i in range(length)]


def release():
    """Release all SPI bus.

    Note: An exception is thrown if it fails to release all SPI bus.
    """
    ret = _LIB.spi_release()
    if ret < 0:
        raise Exception("spi release failed")
