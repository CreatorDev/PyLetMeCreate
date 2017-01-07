#!/usr/bin/env python3
"""This example shows how to display a JPEG image using the EVE Click wrapper
of the LetMeCreate library.

It displays an image and exits after 10 seconds.

Before running this program:
  - the EVE Click must be inserted in Mikrobus 1
  - a WQVGA screen must be connected to the EVE Click.
"""

from letmecreate.core import spi
from letmecreate.core.common import MIKROBUS_1
from letmecreate.click import eve
from time import sleep

IMAGE_MEMORY_ADDRESS = 0
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 180

# Read image from file
image_file = open('/usr/bin/pyletmecreate_examples/data/image.jpg', 'rb')
data = list(image_file.read())
image_file.close()

spi.init()
spi.set_mode(MIKROBUS_1, 0)

eve.enable(MIKROBUS_1)

# First, the image must be decompressed by the FT800 chip and store in the
# memory of the FT800.
eve.load_image(IMAGE_MEMORY_ADDRESS,     # Address in memory to store decompressed image
               eve.FT800_OPT_RGB565,
               data)

eve.clear(0, 0, 0)

# This specifies where the image is stored in the memory of the FT800 chip.
# It must match with the first argument of eve.load_image
eve.draw(eve.FT800_BITMAP_SOURCE, [IMAGE_MEMORY_ADDRESS])

# Each pixel takes 2 bytes (5bits for red, 6bits for green and 5bits for
# blue). Hence, each line of the image takes 2*IMAGE_WIDTH bytes.
eve.draw(eve.FT800_BITMAP_LAYOUT, [eve.FT800_RGB565, IMAGE_WIDTH*2, IMAGE_HEIGHT])

# This configures which part of the image to draw and how to draw it.
# Since we display the entire image, the last two arguments are equal to
# the size of the image but they could be smaller or bigger
eve.draw(eve.FT800_BITMAP_SIZE, [eve.FT800_NEAREST, eve.FT800_BORDER, eve.FT800_BORDER, IMAGE_WIDTH, IMAGE_HEIGHT])

eve.draw(eve.FT800_BEGIN, [eve.FT800_BITMAPS])
eve.draw(eve.FT800_VERTEX2II,
               [100,    # x
               50,      # y
               0,       # handle
               0])      # cell

eve.draw(eve.FT800_END, [])

eve.draw(eve.FT800_TEXT,
        [240,                   # x
        26,                     # y
        23,                     # font
        eve.FT800_OPT_CENTER,   # options
        "Example 4".encode('utf-8')])

eve.draw(eve.FT800_TEXT,
        [240,                   # x
        245,                    # y
        20,                     # font
        eve.FT800_OPT_CENTER,   # options
        "J. M. W. Turner - The battle of Trafalgar (1822)".encode('utf-8')])

eve.display()

sleep(10)

eve.disable(MIKROBUS_1)
spi.release()
