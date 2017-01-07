#!/usr/bin/env python3
"""This example shows how to use the ADC Click wrapper of the LetMeCreate
library.

It reads ADC values from the four channels. Each value should be in range
0..4095. If no wires are connected to the channels of the ADC Click, then
the values should be random.

The ADC Click must be inserted in Mikrobus 1 before running the program.
"""
from letmecreate.core import spi
from letmecreate.click import adc


spi.init()

for i in range(adc.ADC_CLICK_CHANNEL_COUNT):
    print('channel {} value: {}'.format(i, adc.get_raw_value(i)))

spi.release()
