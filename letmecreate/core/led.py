#!/usr/bin/env python3
"""Python binding of LED wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')

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
    """Initialise all LED's.

    ALL LED's are switched off and configured in ON_OFF_MODE.

    Note: An exception is thrown if an error occurs during the intialisation.
    """
    ret = _LIB.led_init()
    if ret != 0:
        raise Exception("led init failed")


def switch_on(mask):
    """Switch on some LED's.

    The LED's must be initialised before calling this function and configured
    in ON_OFF_MODE.

    mask: 8-bit integer. Only LED's whose corresponding bits are set to 1 are
    switched on.

    Note: An exception is thrown if it fails to switch on LED's.
    """
    ret = _LIB.led_switch_on(mask)
    if ret < 0:
        raise Exception("led switch_on failed")


def switch_off(mask):
    """Switch off some LED's.

    The LED's must be initialised before calling this function and configured
    in ON_OFF_MODE.

    mask: 8-bit integer. Only LED's whose corresponding bits are set to 1 are
    switched off.

    Note: An exception is thrown if it fails to switch on LED's.
    """
    ret = _LIB.led_switch_off(mask)
    if ret < 0:
        raise Exception("led switch_off failed")


def set_value(mask, value):
    """Switch on/off some LED's.

    The LED's must be initialised before calling this function and configured
    in ON_OFF_MODE.

    mask: 8-bit integer. LED's whose corresponding bits are set to 1 might be
    switched on/off by this function.

    value: 8-bit integer. LED's whose corresponding bits are set to 1 are
    switched on, 0, switched off.

    Note: An exception is thrown if it fails to switch on/off LED's.
    """
    ret = _LIB.led_set(mask, value)
    if ret < 0:
        raise Exception("led set value failed")


def configure_on_off_mode(mask):
    """Configure some LED's as ON_OFF_MODE.

    The LED's must be initialised before calling this function.

    mask: 8-bit integer. LED's whose corresponding bits are set to 1 are
    configured in ON_OFF_MODE.

    Note: An exception is thrown if it fails to configure LED's.
    """
    ret = _LIB.led_configure_on_off_mode(mask)
    if ret < 0:
        raise Exception("led configure_on_off_mode failed")


def configure_timer_mode(mask):
    """Configure some LED's as TIMER_MODE.

    The LED's must be initialised before calling this function.

    mask: 8-bit integer. LED's whose corresponding bits are set to 1 are
    configured in TIMER_MODE.

    Note: An exception is thrown if it fails to configure LED's.
    """
    ret = _LIB.led_configure_timer_mode(mask)
    if ret < 0:
        raise Exception("led configure_timer_mode failed")


def get_mode(index):
    """Returns the mode of a LED.

    The LED must be initialised before calling this function.

    index: must be an integer in range 0..7

    Note: An exception is thrown if it fails to retrieve the mode of a LED.
    """
    mode = ctypes.c_uint8(0)
    ret = _LIB.led_get_mode(index, ctypes.byref(mode))
    if ret < 0:
        raise Exception("led get mode failed")
    return mode.value


def set_delay(mask, delay_on, delay_off):
    """Set the on/off delay of some LED's.

    The LED's must be initialised before calling this function and configured
    in TIMER_MODE.

    mask: Only LED's, whose corresponding bits are set to 1, have their settings
    changed by this function.

    delay_on: Time in milliseconds when LED's are on.

    delay_off: Time in milliseconds when LED's are off.

    Note: An exception is thrown if it fails to set the
    """
    ret = _LIB.led_set_delay(mask, delay_on, delay_off)
    if ret < 0:
        raise Exception("led set delay failed")


def release():
    """Release all LED's.

    Switch off all LED's.

    Note: If it fails to release LED's, an exception is thrown.
    """
    ret = _LIB.led_release()
    if ret < 0:
        raise Exception("led release failed")
