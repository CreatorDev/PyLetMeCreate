#!/usr/bin/env python3
"""This example shows how to use the Lora Click wrapper of the LetMeCreate to
send or receive data.

Depending on the mode selected, it either continuously sends a message every
second, or it waits for data and prints what it receives.
The user has to interrupt the program to exit it by pressing Ctrl+C.

To run the example in send mode:
$ ./lora_example.py s

To run the example in receive mode:
$ ./lora_example.py r

The Lora Click must be inserted in Mikrobus 1 before running this program.
"""

from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import lora
from letmecreate.core import uart
from letmecreate.core.uart import UART_BD_57600
from time import sleep
import sys

def receive():
    buffer = lora.receive(16)
    buffer = bytes(buffer).decode('utf-8')
    print(buffer)

def send(n):
    buffer = 'Hello, World! {}'.format(n)
    lora.send(buffer.encode('utf-8'))
    print(buffer)

if len(sys.argv) < 2:
    print('{} (r|s)'.format(sys.argv[0]))
    sys.exit(-1)

mode = sys.argv[1]
if mode != 'r' and mode != 's':
    print('Invalid mode.')
    sys.exit(-1)

print('Press Ctrl+C to exit program')

uart.init()
uart.select_bus(MIKROBUS_1)
uart.set_baudrate(UART_BD_57600)

config = lora.get_default_configuration()
lora.init(MIKROBUS_1, config)

n = 0
while True:
    if mode == 's':
        send(n)
        sleep(1)
    elif mode == 'r':
        receive()

    n += 1


uart.release()
