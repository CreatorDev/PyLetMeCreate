import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')

# Baudrates
UART_BD_1200 = 1200
UART_BD_2400 = 2400
UART_BD_4800 = 4800
UART_BD_9600 = 9600
UART_BD_19200 = 19200
UART_BD_38400 = 38400
UART_BD_57600 = 57600


def init():
    ret = _lib.uart_init()
    if ret < 0:
        raise Exception("uart init failed")


def select_bus(mikrobus_index):
    _lib.uart_select_bus(mikrobus_index)


def get_current_bus():
    return  _lib.uart_get_current_bus()


def set_baudrate(baudrate):
    ret = _lib.uart_set_baudrate(baudrate)
    if ret < 0:
        raise Exception("uart set baudrate failed")


def get_baudrate():
    baudrate = ctypes.c_uint32(0)
    ret = _lib.uart_get_baudrate(ctypes.byref(baudrate))
    if ret < 0:
        raise Exception("uart get baudrate failed")
    return baudrate.value


def send(data):
    arr = (ctypes.c_uint8 * len(data))(*data)
    ret = _lib.uart_send(arr, len(data))
    if ret < 0:
        raise Exception("uart send failed")


def receive(length):
    arr = (ctypes.c_uint8 * length)()
    ret = _lib.uart_receive(arr, length)
    if ret < 0:
        raise Exception("uart receive failed")
    return [arr[i] for i in range(length)]


def release():
    ret = _lib.uart_release()
    if ret < 0:
        raise Exception("uart release failed")
