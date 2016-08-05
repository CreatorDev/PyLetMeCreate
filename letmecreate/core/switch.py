import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')
callback_type = ctypes.CFUNCTYPE(None)
callbacks = {}

SWITCH_1_PRESSED = 0x01
SWITCH_1_RELEASED = 0x02
SWITCH_2_PRESSED = 0x04
SWITCH_2_RELEASED = 0x08
SWITCH_ALL_EVENTS = 0x0F


def init():
    global callbacks
    ret = _lib.switch_init()
    if ret < 0:
        raise Exception("switch init failed")
    callbacks = {}


def add_callback(event_mask, callback):
    ptr = callback_type(callback)
    ret = _lib.switch_add_callback(event_mask, ptr)
    if ret < 0:
        raise Exception("switch add callback failed")
    callbacks[ret] = ptr


def remove_callback(callback_id):
    ret = _lib.switch_remove_callback(callback_id)
    if ret < 0:
        raise Exception("switch remove callback failed")
    del callbacks[callback_id]


def release():
    ret = _lib.switch_release()
    if ret < 0:
        raise Exception("switch release failed")
