import ctypes

_lib = ctypes.CDLL('libletmecreate_click.so')
callback_type = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
callbacks = [None, None]


def enable(mikrobus_index):
    ret = _lib.motion_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("motion click enable failed")


def attach_callback(mikrobus_index, callback):
    ptr = callback_type(callback)
    ret = _lib.motion_click_attach_callback(mikrobus_index, ptr)
    if ret < 0:
        raise Exception("motion click attach callback failed")
    callbacks[mikrobus_index] = ptr;


def disable(mikrobus_index):
    ret = _lib.motion_click_disable(mikrobus_index)
    if ret < 0:
        raise Exception("motion click disable failed")
