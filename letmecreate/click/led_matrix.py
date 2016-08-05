import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def enable():
    ret = _lib.led_matrix_click_enable()
    if ret < 0:
        raise Exception("led matrix click enable failed")


def set_intensity(intensity):
    ret = _lib.led_matrix_click_set_intensity(intensity)
    if ret < 0:
        raise Exception("led matrix click set intensity failed")


def set_column(column_index, data):
    ret = _lib.led_matrix_click_set_column(column_index, data)
    if ret < 0:
        raise Exception("led matrix click set column failed")


def display_number(number):
    ret = _lib.led_matrix_click_display_number(number)
    if ret < 0:
        raise Exception("led matrix click display number failed")


def set_columns(columns):
    data = (ctypes.c_uint8 * len(columns))(*columns)
    ret = _lib.led_matrix_click_set(data)
    if ret < 0:
        raise Exception("led matrix click set columns failed")


def disable():
    ret = _lib.led_matrix_click_disable()
    if ret < 0:
        raise Exception("led matrix click disable failed")
