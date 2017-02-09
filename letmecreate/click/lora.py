#!/usr/bin/env python3
"""Python binding of Lora wrapper of LetMeCreate library."""

import ctypes

LORA_CLICK_AUTO_FREQ_BAND_250KHZ = 0
LORA_CLICK_AUTO_FREQ_BAND_125KHZ = 1
LORA_CLICK_AUTO_FREQ_BAND_62_5KHZ = 2
LORA_CLICK_AUTO_FREQ_BAND_31_3KHZ = 3
LORA_CLICK_AUTO_FREQ_BAND_15_6KHZ = 4
LORA_CLICK_AUTO_FREQ_BAND_7_8KHZ = 5
LORA_CLICK_AUTO_FREQ_BAND_3_9KHZ = 6
LORA_CLICK_AUTO_FREQ_BAND_200KHZ = 7
LORA_CLICK_AUTO_FREQ_BAND_100KHZ = 8
LORA_CLICK_AUTO_FREQ_BAND_50KHZ = 9
LORA_CLICK_AUTO_FREQ_BAND_25KHZ = 10
LORA_CLICK_AUTO_FREQ_BAND_12_5KHZ = 11
LORA_CLICK_AUTO_FREQ_BAND_6_3KHZ = 12
LORA_CLICK_AUTO_FREQ_BAND_3_1KHZ = 13
LORA_CLICK_AUTO_FREQ_BAND_166_7KHZ = 14
LORA_CLICK_AUTO_FREQ_BAND_83_3KHZ = 15
LORA_CLICK_AUTO_FREQ_BAND_41_7KHZ = 16
LORA_CLICK_AUTO_FREQ_BAND_20_8KHZ = 17
LORA_CLICK_AUTO_FREQ_BAND_10_4KHZ = 18
LORA_CLICK_AUTO_FREQ_BAND_5_2KHZ = 19
LORA_CLICK_AUTO_FREQ_BAND_2_6KHZ = 20
LORA_CLICK_AUTO_FREQ_BAND_COUNT = 21

LORA_CLICK_CODING_RATE_4_5 = 0
LORA_CLICK_CODING_RATE_4_6 = 1
LORA_CLICK_CODING_RATE_4_7 = 2
LORA_CLICK_CODING_RATE_4_8 = 3
LORA_CLICK_CODING_RATE_COUNT = 4

LORA_CLICK_BANDWIDTH_125KHZ = 0
LORA_CLICK_BANDWIDTH_250KHZ = 1
LORA_CLICK_BANDWIDTH_500KHZ = 2

class LoraClickConfig(ctypes.Structure):
    """Lora Click configuration"""
    _fields_ = [
        ("frequency", ctypes.c_uint32),
        ("spreading_factor", ctypes.c_uint8),
        ("auto_freq_band", ctypes.c_uint),
        ("coding_rate", ctypes.c_uint),
        ("bandwidth", ctypes.c_uint),
        ("power", ctypes.c_int8),
        ("bitrate", ctypes.c_uint16),
        ("freq_deviation", ctypes.c_uint16),
        ("preamble_length", ctypes.c_uint16),
        ("enable_crc_header", ctypes.c_bool)]

_LIB = ctypes.CDLL('libletmecreate_click.so')

_LIB.lora_click_get_default_configuration.restype = LoraClickConfig

def get_default_configuration():
    """Returns default configuration:

        frequency = 868000000
        spreading_factor = 12
        auto_freq_band = LORA_CLICK_AUTO_FREQ_BAND_125KHZ
        coding_rate = LORA_CLICK_CODING_RATE_4_8
        bandwidth = LORA_CLICK_BANDWIDTH_250KHZ
        power = 14
        bitrate = 5000
        freq_deviation = 5000
        preamble_length = 8
        enable_crc_header = true
    """
    return _LIB.lora_click_get_default_configuration()


def init(mikrobus_index, config):
    """Initialize the Lora Click and configure it.

    mikrobus_index: 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    config: Configuration of the Lora Click

    Note: An exception is thrown if it fails to initialize the Lora Click.
    """
    ret = _LIB.lora_click_init(mikrobus_index, config)
    if ret < 0:
        raise Exception("")


def configure(config):
    """Configure the Lora Click

    config: Configuration of the Lora Click

    Note: An exception is thrown if it fails to configure the Lora Click.
    """
    ret = _LIB.lora_click_configure(config)
    if ret < 0:
        raise Exception("")


def send(data):
    """Send a list of bytes

    data: list of bytes

    This is a blocking call.

    Note: An exception is thrown if it fails to send all bytes.
    """
    length = len(data)
    tx_buffer = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.lora_click_send(tx_buffer, length)
    if ret < 0:
        raise Exception("")


def receive(length):
    """Receive a list of bytes

    length: Number of bytes to receive

    This is a blocking call, it will not return until the number of requested
    bytes has been received.

    Note: An exception is thrown if it fails to receive all bytes.
    """
    rx_buffer = (ctypes.c_uint8 * length)()
    ret = _LIB.lora_click_receive(rx_buffer, length)
    if ret < 0:
        raise Exception("")
    return [rx_buffer[i] for i in range(length)]


def write_eeprom(start_address, data):
    """Write some bytes in EEPROM

    start_address: Must be in range 0x300-0x3FF
    data: A list of bytes to write

    Note: An exception is thrown if it fails to write bytes to the EEPROM.
    """
    length = len(data)
    tmp = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.lora_click_write_eeprom(start_address, tmp, length)
    if ret < 0:
        raise Exception("")


def read_eeprom(start_address, length):
    """Read a list of bytes from EEPROM

    start_address: Must be in range 0x300-0x3FF
    length: Number of bytes to read

    Note: An exception is thrown if it fails to read bytes from the EEPROM.
    """
    data = (ctypes.c_uint8 * length)()
    ret = _LIB.lora_click_read_eeprom(start_address, data, length)
    if ret < 0:
        raise Exception("")
    return [data[i] for i in range(length)]


def get_eui():
    """Read the EUI from the Lora Click

    This function returns a list of 8 bytes representing the EUI of the
    device.

    Note: An exception is thrown if it fails to read the EUI.
    """
    eui = (ctypes.c_uint8 * 8)()
    ret = _LIB.lora_click_get_eui(eui)
    if ret < 0:
        raise Exception("")
    return [eui[i] for i in range(8)]
