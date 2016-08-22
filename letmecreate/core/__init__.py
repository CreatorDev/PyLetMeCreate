"""Python binding of the core part of the LetMeCreate library.

It defines binding for the following interface:
  - adc
  - gpio and gpio_monitor
  - switch
  - UART
  - I2C
  - SPI
  - PWM
  - led
"""

__all__ = ['led', 'switch', 'gpio', 'gpio_monitor', 'common', 'adc', 'pwm',
           'uart', 'i2c', 'spi']
