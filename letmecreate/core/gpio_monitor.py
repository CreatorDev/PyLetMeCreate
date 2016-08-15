#!/usr/bin/env python3
"""Python binding of gpio_monitor wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint8)
_CALLBACKS = {}

# GPIO events
GPIO_RAISING = 0x01
GPIO_FALLING = 0x02
GPIO_EDGE = GPIO_RAISING | GPIO_FALLING


def init():
    """Initialise gpio_monitor.

    Note: If an error occurs during the initialisation, an exception is thrown.
    """
    global _CALLBACKS
    ret = _LIB.gpio_monitor_init()
    if ret < 0:
        raise Exception("gpio monitor init failed")
    _CALLBACKS = {}


def add_callback(gpio_pin, event_mask, callback):
    """Attach a callback to a GPIO. Returns the callback ID.

    gpio_pin: Index of the GPIO. Constants are defined in letmecreate.core.gpio.

    event_mask: should be 1 (GPIO_RAISING), 2 (GPIO_FALLING) or 3 (GPIO_EDGE).

    callback: Function to call

    Note: The GPIO must be configured as an input before calling this function.
    An exception is thrown if the callback cannot be attached to the GPIO.
    """
    ptr = _CALLBACK_TYPE(callback)
    ret = _LIB.gpio_monitor_add_callback(gpio_pin, event_mask, ptr)
    if ret < 0:
        raise Exception("gpio monitor add callback failed")
    _CALLBACKS[ret] = ptr


def remove_callback(callback_id):
    """Detach callback from GPIO.

    callback_id: ID of the callback to detach. Must be a positive integer,
    returned from a previous call to add_callback.

    Note: An exception is thrown if the callback cannot be removed.
    """
    ret = _LIB.gpio_monitor_remove_callback(callback_id)
    if ret < 0:
        raise Exception("gpio monitor remove callback failed")
    del _CALLBACKS[callback_id]


def release():
    """Release gpio_monitor.

    Deletes all callbacks currently attached to GPIO's.
    """
    ret = _LIB.gpio_monitor_release()
    if ret < 0:
        raise Exception("gpio monitor release failed")
