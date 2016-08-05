import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')


def init():
    ret = _lib.i2c_init()
    if ret < 0:
        raise Exception("i2c init failed")


def select_bus(mikrobus_index):
    _lib.i2c_select_bus(mikrobus_index)


def get_current_bus():
    current_bus = ctypes.c_uint8(0)
    ret = _lib.i2c_get_current_bus(ctypes.byref(current_bus))
    if ret < 0:
        raise Exception("i2c get current bus failed")
    return current_bus.value


def write(slave_address, data):
    arr = (ctypes.c_uint8 * len(data))(*data)
    ret = _lib.i2c_write(slave_address, arr, len(data))
    if ret < 0:
        raise Exception("i2c write failed")


def read(slave_address, length):
    arr = (ctypes.c_uint8 * length)()
    ret = _lib.i2c_read(slave_address, arr, length)
    if ret < 0:
        raise Exception("i2c read failed")
    return [arr[i] for i in range(length)]


def write_byte(slave_address, data):
    ret = _lib.i2c_write_byte(slave_address, data)
    if ret < 0:
        raise Exception("i2c write byte failed")


def read_byte(slave_address):
    data = ctypes.c_uint8(0)
    ret = _lib.i2c_read_byte(slave_address, ctypes.byref(data))
    if ret < 0:
        raise Exception("i2c write byte failed")
    return data.value


def release():
    ret = _lib.i2c_release()
    if ret < 0:
        raise Exception("i2c release failed")
