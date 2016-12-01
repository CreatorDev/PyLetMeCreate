#!/usr/bin/env python3

from letmecreate.core import i2c
from letmecreate.core import led
from letmecreate.click import joystick

OFFSET = 98
MAXIMUM = OFFSET * 2

def get_led_mask(perc):
	div = int((1. - perc) * led.LED_CNT)
	if div > led.LED_CNT:
		div = led.LED_CNT

	mask = 0
	for i in range(div):
		mask |= (1 << i)

	return mask

i2c.init()
led.init()

while True:
	pos = joystick.get_position()
	print('{} {}'.format(pos[0], pos[1]))
	mask = get_led_mask(float(pos[0] +  OFFSET)/float(MAXIMUM))
	led.switch_on(mask)
	led.switch_off(~mask)

i2c.release()
led.release()
