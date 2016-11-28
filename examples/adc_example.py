#!/usr/bin/env python3

from letmecreate.core import spi
from letmecreate.click import adc


spi.init()

for i in range(adc.ADC_CLICK_CHANNEL_COUNT):
    print('channel {} value: {}'.format(i, adc.get_raw_value(i)))

spi.release()
