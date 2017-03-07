#!/usr/bin/env python3
"""Python binding of DC motor Click wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')


def init(mikrobus_index):
    """Initialise the DC motor click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to initialise the board.
    """
    ret = _LIB.dc_motor_click_init(mikrobus_index)
    if ret < 0:
        raise Exception("dc motor click init failed")


def set_direction(mikrobus_index, direction):
    """Change the direction of the motor.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    direction: must be 0 (reverse) or 1 (forward

    Note: An exception is thrown if it fails to change the direction.
    """
    ret = _LIB.dc_motor_click_set_direction(mikrobus_index, direction)
    if ret < 0:
        raise Exception("dc motor click set direction failed")


def get_direction(mikrobus_index):
    """Returns the direction of the motor.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to get the direction.
    """
    direction = ctypes.c_uint8()
    ret = _LIB.dc_motor_click_set_direction(mikrobus_index,
                                            ctypes.byref(direction))
    if ret < 0:
        raise Exception("dc motor click get direction failed")
    return direction.value


def set_speed(mikrobus_index, speed):
    """Change the speed of the motor.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)
    speed: floating point value in range 0..100

    Note: An exception is thrown if it fails to change the speed.
    """
    ret = _LIB.dc_motor_click_set_speed(mikrobus_index, speed)
    if ret < 0:
        raise Exception("dc motor click set speed failed")


def get_speed(mikrobus_index):
    """Returns the speed of the motor.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to get the speed.
    """
    speed = ctypes.c_float()
    ret = _LIB.dc_motor_click_get_speed(mikrobus_index, ctypes.byref(speed))
    if ret < 0:
        raise Exception("dc motor click get speed failed")
    return speed.value


def release(mikrobus_index):
    """Release the DC motor click.

    Stops the motor.

    Note: An exception is thrown if it fails to release
    """
    ret = _LIB.dc_motor_click_release(mikrobus_index)
    if ret < 0:
        raise Exception("dc motor click release failed")
