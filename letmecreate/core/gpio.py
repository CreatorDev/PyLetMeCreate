#!/usr/bin/env python3
"""Python binding of gpio wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')

# Pin type
TYPE_AN = 0
TYPE_RST = 1
TYPE_PWM = 2
TYPE_INT = 3
TYPE_COUNT = 4

# GPIO pin number
MIKROBUS_1_AN = 22
MIKROBUS_1_RST = 23
MIKROBUS_1_PWM = 73
MIKROBUS_1_INT = 21
MIKROBUS_2_AN = 25
MIKROBUS_2_RST = 27
MIKROBUS_2_PWM = 74
MIKROBUS_2_INT = 24
GPIO_14 = 14
GPIO_21 = 21
GPIO_22 = 22
GPIO_23 = 23
GPIO_24 = 24
GPIO_25 = 25
GPIO_27 = 27
GPIO_31 = 31
GPIO_73 = 73
GPIO_74 = 74
GPIO_75 = 75
GPIO_88 = 88
GPIO_89 = 89
GPIO_72 = 72
GPIO_80 = 80
GPIO_81 = 81
GPIO_82 = 82
GPIO_83 = 83
GPIO_84 = 84
GPIO_85 = 85

# GPIO direction
GPIO_OUTPUT = 0
GPIO_INPUT = 1


def init(gpio_pin):
    """Initialise a GPIO.

    Export the GPIO and configure it as an input.

    Note: An exception is thrown if the gpio cannot be initialised.
    """
    ret = _LIB.gpio_init(gpio_pin)
    if ret < 0:
        raise Exception("gpio init failed")


def get_pin(mikrobus_index, pin_type):
    """Returns GPIO index of a pin on provided mikrobus

    Note: An exception is thrown if the gpio cannot be found.
    """
    pin = ctypes.c_uint8(0)
    ret = _LIB.gpio_get_pin(mikrobus_index, pin_type, ctypes.byref(pin))
    if ret < 0:
        raise Exception("gpio get pin failed")
    return pin.value


def get_type(gpio_pin):
    """Returns the type of the GPIO

    Some GPIO's on the Mikrobus has some type (AN, PWM, INT, RST or CS). Other
    GPIO's don't have a type.

    Note: An exception is thrown if the type of the gpio cannot be found.
    """
    pin_type = ctypes.c_uint8(0)
    ret = _LIB.gpio_get_type(gpio_pin, ctypes.byref(pin_type))
    if ret < 0:
        raise Exception("gpio get type failed")
    return pin_type.value


def set_direction(gpio_pin, direction):
    """Configure GPIO as an input or an output.

    gpio_pin: Index of the GPIO.

    direction: must be 0 (GPIO_OUTPUT) or 1 (GPIO_INPUT).

    Note: An exception is thrown if it fails to set the direction of a GPIO.
    """
    ret = _LIB.gpio_set_direction(gpio_pin, direction)
    if ret < 0:
        raise Exception("gpio set direction failed")


def get_direction(gpio_pin):
    """Returns the direction of a GPIO (0 or 1).

    gpio_pin: Index of the GPIO.

    Note: An exception is thrown if it fails to get the current direction of a
    GPIO.
    """
    direction = ctypes.c_uint8(0)
    ret = _LIB.gpio_get_direction(gpio_pin, ctypes.byref(direction))
    if ret < 0:
        raise Exception("gpio get direction failed")
    return direction.value


def set_value(gpio_pin, value):
    """Sets the GPIO as high or low.

    The GPIO must be configured as an output before calling this function.

    gpio_pin: Index of the GPIO.

    value: 0 for low, any other positive integer for high.

    Note: An exception is thrown if it fails to set the value of a GPIO.
    """
    ret = _LIB.gpio_set_value(gpio_pin, value)
    if ret < 0:
        raise Exception("gpio set value failed")


def get_value(gpio_pin):
    """Reads the current value of a GPIO (0: low, 1: high)

    gpio_pin: Index of the GPIO.

    Note: An exception is thrown if it fails to read the value of a GPIO.
    """
    value = ctypes.c_uint8(0)
    ret = _LIB.gpio_get_value(gpio_pin, ctypes.byref(value))
    if ret < 0:
        raise Exception("gpio get direction failed")
    return value.value


def release(gpio_pin):
    """Release a GPIO.

    gpio_pin: Index of the GPIO.

    Note: An exception is thrown if it fails to release the GPIO.
    """
    ret = _LIB.gpio_release(gpio_pin)
    if ret < 0:
        raise Exception("gpio get direction failed")
