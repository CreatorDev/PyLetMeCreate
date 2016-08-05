import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def enable():
    ret = _lib.color_click_enable()
    if ret < 0:
        raise Exception("color click enable failed")


def get_color():
    clear = ctypes.c_uint16(0)
    red = ctypes.c_uint16(0)
    green = ctypes.c_uint16(0)
    blue = ctypes.c_uint16(0)
    ret = _lib.color_click_get_color(ctypes.byref(clear),
                                     ctypes.byref(red),
                                     ctypes.byref(green),
                                     ctypes.byref(blue))
    if ret < 0:
        raise Exception("color click get color failed")

    return (clear.value, red.value, green.value, blue.value)


def disable():
    ret = _lib.color_click_disable()
    if ret < 0:
        raise Exception("color click disable failed")
