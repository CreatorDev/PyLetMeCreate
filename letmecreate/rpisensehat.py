#!/usr/bin/env python3
"""Python binding of Raspberry PI sense HAT of LetMeCreate library.

This wrapper supports I2C protocol to communicate with the hat
You must initialise the I2C bus and select mikrobus 1 before using
any of these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_rpisensehat.so')

# Joystick states
JOYSTICK_LEFT = 0x10
JOYSTICK_RIGHT = 0x02
JOYSTICK_DOWN = 0x01
JOYSTICK_UP = 0x04
JOYSTICK_PRESSED = 0x08


def init():
    """Initialise all sensors on board.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.rpisensehat_init()
    if ret < 0:
        raise Exception("rpisensehat init failed")


def get_temperature():
    """Read the temperature from humidity sensor.

    Note: An exception is thrown if it fails.
    """
    temperature = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_temperature(ctypes.byref(temperature))
    if ret < 0:
        raise Exception("rpisensehat get temperature failed")
    return temperature.value


def get_humidity():
    """Read humidity measurement from humidity sensor.

    Note: An exception is thrown if it fails.
    """
    humidity = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_humidity(ctypes.byref(humidity))
    if ret < 0:
        raise Exception("rpisensehat get humidity failed")
    return humidity.value


def get_pressure():
    """ Read pressure measurement from pressure sensor.

    Note: An exception is thrown if it fails.
    """
    pressure = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_pressure(ctypes.byref(pressure))
    if ret < 0:
        raise Exception("rpisensehat get pressure failed")
    return pressure.value


def get_accelerometer_measure():
    """Read acccelerometer measurement from accel/mag/gyro sensor.

    Note: An exception is thrown if it fails.
    """
    accel_x = ctypes.c_float(0)
    accel_y = ctypes.c_float(0)
    accel_z = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_accelerometer_measure(ctypes.byref(accel_x),
                                                     ctypes.byref(accel_y),
                                                     ctypes.byref(accel_z))
    if ret < 0:
        raise Exception("rpisensehat get accelerometer measure failed")
    return (accel_x.value, accel_y.value, accel_z.value)


def get_gyroscope_measure():
    """Read gyroscope measurement from accel/mag/gyro sensor.

    Note: An exception is thrown if it fails.
    """
    gyro_x = ctypes.c_float(0)
    gyro_y = ctypes.c_float(0)
    gyro_z = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_gyroscope_measure(ctypes.byref(gyro_x),
                                                 ctypes.byref(gyro_y),
                                                 ctypes.byref(gyro_z))
    if ret < 0:
        raise Exception("rpisensehat get gyroscope measure failed")
    return (gyro_x.value, gyro_y.value, gyro_z.value)


def get_magnetometer_measure():
    """Read magnetometer measurement from accel/mag/gyro sensor.

    Note: An exception is thrown if it fails.
    """
    mag_x = ctypes.c_float(0)
    mag_y = ctypes.c_float(0)
    mag_z = ctypes.c_float(0)
    ret = _LIB.rpisensehat_get_magnetometer_measure(ctypes.byref(mag_x),
                                                    ctypes.byref(mag_y),
                                                    ctypes.byref(mag_z))
    if ret < 0:
        raise Exception("rpisensehat get magnetometer measure failed")
    return (mag_x.value, mag_y.value, mag_z.value)


def get_joystick_input():
    """Read joystick position.

    Note: An exception is thrown if it fails.
    """
    state = ctypes.c_uint8(0)
    ret = _LIB.rpisensehat_get_joystick_input(ctypes.byref(state))
    if ret < 0:
        raise Exception("rpisensehat get joystick input failed")
    return state.value


def set_leds_state(pixels):
    """Set LED's

    Layout of the array:

    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB
    RGB RGB RGB RGB RGB RGB RGB RGB

    The first 24 bytes of the array stores the first line of the LED's, the
    following 24 bytes stores the second line, etc.
    Each value of the array should not be greater than 0x1F.

    Note: An exception is thrown if it fails.
    """
    buffer = (ctypes.c_uint8 * len(pixels))(*pixels)
    ret = _LIB.rpisensehat_set_leds_state(buffer)
    if ret < 0:
        raise Exception("rpisensehat set leds state failed")


def display_rainbow():
    """Display a rainbow on the LED matrix.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.rpisensehat_display_rainbow()
    if ret < 0:
        raise Exception("rpisensehat display rainbow failed")


def release():
    """Power-down all sensors on board.

    Note: An exception is thrown if it fails.
    """
    ret = _LIB.rpisensehat_release()
    if ret < 0:
        raise Exception("rpisensehat released failed")
