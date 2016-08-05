import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')

# SPI_SPEED
SPI_680K  = 680000
SPI_1M36  = 1360000
SPI_2M73  = 2730000
SPI_5M46  = 5460000
SPI_10M93 = 10930000
SPI_21M87 = 21870000
SPI_43M75 = 43750000


def init():
    ret = _lib.spi_init()
    if ret < 0:
        raise Exception("spi init failed")


def set_mode(mikrobus_index, mode):
    ret = _lib.spi_set_mode(mikrobus_index, mode)
    if ret < 0:
        raise Exception("spi set mode failed")


def set_speed(mikrobus_index, speed):
    ret = _lib.spi_set_speed(mikrobus_index, speed)
    if ret < 0:
        raise Exception("spi set speed failed")


def select_bus(mikrobus_index):
    _lib.spi_select_bus(mikrobus_index)


def get_current_bus():
    return _lib.spi_get_current_bus()


def transfer(tx_data):
    length = len(tx_data)
    tx_buffer = (ctypes.c_uint8 * length)(*tx_data)
    rx_buffer = (ctypes.c_uint8 * length)()
    ret = _lib.spi_transfer(tx_buffer, rx_buffer, length)
    if ret < 0:
        raise Exception("spi transfer failed")
    return [rx_buffer[i] for i in range(length)]


def release():
    ret = _lib.spi_release()
    if ret < 0:
        raise Exception("spi release failed")
