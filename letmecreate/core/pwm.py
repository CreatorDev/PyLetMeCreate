#!/usr/bin/env python3
"""Python binding of PWM wrapper of LetMeCreate library."""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_core.so')


def init(mikrobus_index):
    """Initialise a PWM output on a mikrobus.

    Set the duty cycle to 50%, the frequency to 3kHz and disable the output.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if an error occurs during initialisation.
    """
    ret = _LIB.pwm_init(mikrobus_index)
    if ret < 0:
        raise Exception("pwm init failed")


def enable(mikrobus_index):
    """Enable output of one PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to enable the output.
    """
    ret = _LIB.pwm_enable(mikrobus_index)
    if ret < 0:
        raise Exception("pwm enable failed")


def set_duty_cycle(mikrobus_index, percentage):
    """Set the duty cycle of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    percentage: integer in range 0..100.

    Note: An exception is thrown if it fails to set the duty cycle.
    """
    ret = _LIB.pwm_set_duty_cycle(mikrobus_index, percentage)
    if ret < 0:
        raise Exception("pwm set duty cycle failed")


def get_duty_cycle(mikrobus_index):
    """Returns the current duty cycle of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to retrieve the duty cycle.
    """
    percentage = ctypes.c_float(0)
    ret = _LIB.pwm_get_duty_cycle(mikrobus_index, ctypes.byref(percentage))
    if ret < 0:
        raise Exception("pwm get duty cycle failed")
    return percentage.value


def set_frequency(mikrobus_index, frequency):
    """Set the frequency of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    frequency: Frequency in Hertz of the PWM output. The minimal frequency is
    2680.7Hz, and the maximum frequency is about 22Mhz.

    Note: An exception is thrown if it fails to set the frequency.
    """
    ret = _LIB.pwm_set_frequency(mikrobus_index, frequency)
    if ret < 0:
        raise Exception("pwm set frequency failed")


def get_frequency(mikrobus_index):
    """Returns the frequency of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to retrieve the frequency.
    """
    frequency = ctypes.c_float(0)
    ret = _LIB.gpio_get_frequency(mikrobus_index, ctypes.byref(frequency))
    if ret < 0:
        raise Exception("pwm get frequency failed")
    return frequency.value


def set_period(mikrobus_index, period):
    """Set the period of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    period: Period of the PWM output in nanoseconds. The minimal period is 45ns
    and the maximum period is 373028ns.

    Note: An exception is thrown if it fails to set the period.
    """
    ret = _LIB.pwm_set_period(mikrobus_index, period)
    if ret < 0:
        raise Exception("pwm set period failed")


def get_period(mikrobus_index):
    """Returns the period in nanoseconds of a PWM output.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to retrieve the period.
    """
    period = ctypes.c_uint32(0)
    ret = _LIB.pwm_get_frequency(mikrobus_index, ctypes.byref(period))
    if ret < 0:
        raise Exception("pwm get period failed")
    return period.value


def disable(mikrobus_index):
    """Disable output of a PWM.

    The PWM output on this mikrobus must be initialised before calling this
    function.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to disable a PWM output.
    """
    ret = _LIB.pwm_disable(mikrobus_index)
    if ret < 0:
        raise Exception("pwm disable failed")


def release(mikrobus_index):
    """Release PWM output on a mikrobus.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to release a PWM output.
    """
    ret = _LIB.pwm_release(mikrobus_index)
    if ret < 0:
        raise Exception("pwm release failed")
