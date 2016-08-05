import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')


def get_x():
    x = ctypes.c_int8(0)
    ret = _lib.joystick_click_get_x(ctypes.byref(x))
    if ret < 0:
        raise Exception("joystick click get x failed")
    return x.value


def get_y():
    y = ctypes.c_int8(0)
    ret = _lib.joystick_click_get_y(ctypes.byref(y))
    if ret < 0:
        raise Exception("joystick click get y failed")
    return y.value


def get_position():
    x = ctypes.c_int8(0)
    y = ctypes.c_int8(0)
    ret = _lib.joystick_click_get_position(ctypes.byref(x), ctypes.byref(y))
    if ret < 0:
        raise Exception("joystick click get position failed")
    return (x.value, y.value)
