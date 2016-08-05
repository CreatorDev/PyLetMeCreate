import ctypes

_lib = ctypes.CDLL('libletmecreate_core.so')

LED_0 = 0x01
LED_1 = 0x02
LED_2 = 0x04
LED_3 = 0x08
LED_4 = 0x10
LED_5 = 0x20
LED_6 = 0x40
LED_HEARTBEAT = LED_7 = 0x80
ALL_LEDS = 0xFF

LED_CNT = 8

ON_OFF_MODE = 0
TIMER_MODE = 1


def init():
    ret = _lib.led_init()
    if ret != 0:
        raise Exception("led init failed")


def switch_on(mask):
    ret = _lib.led_switch_on(mask)
    if ret < 0:
        raise Exception("led switch_on failed")


def switch_off(mask):
    ret = _lib.led_switch_off(mask)
    if ret < 0:
        raise Exception("led switch_off failed")


def set_value(mask, value):
    ret = _lib.led_set(mask, value)
    if ret < 0:
        raise Exception("led set value failed")


def configure_on_off_mode(mask):
    ret = _lib.led_configure_on_off_mode(mask)
    if ret < 0:
        raise Exception("led configure_on_off_mode failed")


def configure_timer_mode(mask):
    ret = _lib.led_configure_timer_mode(mask)
    if ret < 0:
        raise Exception("led configure_timer_mode failed")


def get_mode(index):
    mode = ctypes.c_uint8(0)
    ret = _lib.led_get_mode(index, ctypes.byref(mode))
    if ret < 0:
        raise Exception("led get mode failed")
    return mode.value


def set_delay(mask, delay_on, delay_off):
    ret = _lib.led_set_delay(mask, delay_on, delay_off)
    if ret < 0:
        raise Exception("led set delay failed")


def release():
    ret = _lib.led_release()
    if ret < 0:
        raise Exception("led release failed")
