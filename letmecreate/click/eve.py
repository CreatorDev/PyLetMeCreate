#!/usr/bin/env python3
"""Python binding of EVE Click wrapper of LetMeCreate library.

For a more complete documentation, look at the documentation of the EVE click
wrapper of the LetMeCreate available at:
https://github.com/francois-berder/LetMeCreate/blob/master/include/letmecreate/click/eve.h

Also, FTDI documentation is available at:
http://www.ftdichip.com/Support/Documents/DataSheets/ICs/DS_FT800.pdf
http://www.ftdichip.com/Support/Documents/ProgramGuides/FT800%20Programmers%20Guide.pdf

This wrapper only supports SPI protocol to communicate with the click board.
You must initialise the SPI bus and select the right bus before using any of
these functions.
"""

import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint16, ctypes.c_uint16)
_CALLBACK_EVENT_TYPE = ctypes.CFUNCTYPE(None)
_CALLBACK = None
_EVENT_CALLBACK = None

# Display list opcodes
FT800_ALPHA_FUNC = (0x09 << 24)
FT800_BEGIN = (0x1F << 24)
FT800_BITMAP_HANDLE = (0x05 << 24)
FT800_BITMAP_LAYOUT = (0x07 << 24)
FT800_BITMAP_SIZE = (0x08 << 24)
FT800_BITMAP_SOURCE = (0x01 << 24)
FT800_BITMAP_TRANSFORM_A = (0x15 << 24)
FT800_BITMAP_TRANSFORM_B = (0x16 << 24)
FT800_BITMAP_TRANSFORM_C = (0x17 << 24)
FT800_BITMAP_TRANSFORM_D = (0x18 << 24)
FT800_BITMAP_TRANSFORM_E = (0x19 << 24)
FT800_BITMAP_TRANSFORM_F = (0x1F << 24)
FT800_BLEND_FUNC = (0x0B << 24)
FT800_CALL = (0x1D << 24)
FT800_CELL = (0x06 << 24)
FT800_CLEAR = (0x26 << 24)
FT800_CLEAR_COLOR_A = (0x0F << 24)
FT800_CLEAR_COLOR_RGB = (0x02 << 24)
FT800_CLEAR_STENCIL = (0x11 << 24)
FT800_CLEAR_TAG = (0x06 << 24)
FT800_COLOR_A = (0x10 << 24)
FT800_COLOR_MASK = (0x20 << 24)
FT800_COLOR_RGB = (0x04 << 24)
FT800_DISPLAY = (0)
FT800_END = (0x21 << 24)
FT800_JUMP = (0x1E << 24)
FT800_LINE_WIDTH = (0x06 << 24)
FT800_MACRO = (0x25 << 24)
FT800_POINT_SIZE = (0x0D << 24)
FT800_RESTORE_CONTEXT = (0x23 << 24)
FT800_RETURN = (0x24 << 24)
FT800_SAVE_CONTEXT = (0x22 << 24)
FT800_SCISSOR_SIZE = (0x1C << 24)
FT800_SCISSOR_XY = (0x1B << 24)
FT800_STENCIL_FUNC = (0x0A << 24)
FT800_STENCIL_MASK = (0x13 << 24)
FT800_STENCIL_OP = (0x0C << 24)
FT800_TAG = (0x03 << 24)
FT800_TAG_MASK = (0x14 << 24)
FT800_VERTEX2F = (0x01 << 30)
FT800_VERTEX2II = (0x02 << 30)

# Coprocessor opcodes
FT800_APPEND = (0xFFFFFF02)
FT800_BGCOLOR = (0xFFFFFF09)
FT800_BUTTON = (0xFFFFFF0D)
FT800_CALIBRATE = (0xFFFFFF15)
FT800_CLOCK = (0xFFFFFF14)
FT800_COLDSTART = (0xFFFFFF32)
FT800_DIAL = (0xFFFFFF2D)
FT800_DLSTART = (0xFFFFFF00)
FT800_FGCOLOR = (0xFFFFFF0A)
FT800_GAUGE = (0xFFFFFF13)
FT800_GETMATRIX = (0xFFFFFF33)
FT800_GETPTR = (0xFFFFFF23)
FT800_GRADCOLOR = (0xFFFFFF34)
FT800_GRADIENT = (0xFFFFFF0B)
FT800_INFLATE = (0xFFFFFF22)
FT800_INTERRUPT = (0xFFFFFF02)
FT800_KEYS = (0xFFFFFF0E)
FT800_LOADIDENTITY = (0xFFFFFF26)
FT800_LOADIMAGE = (0xFFFFFF24)
FT800_LOGO = (0xFFFFFF31)
FT800_MEMCPY = (0xFFFFFF1D)
FT800_MEMCRC = (0xFFFFFF18)
FT800_MEMSET = (0xFFFFFF1B)
FT800_MEMWRITE = (0xFFFFFF1A)
FT800_MEMZERO = (0xFFFFFF1C)
FT800_NUMBER = (0xFFFFFF2E)
FT800_PROGRESS = (0xFFFFFF0F)
FT800_REGREAD = (0xFFFFFF19)
FT800_ROTATE = (0xFFFFFF29)
FT800_SCALE = (0xFFFFFF28)
FT800_SCREENSAVER = (0xFFFFFF2F)
FT800_SCROLLBAR = (0xFFFFFF11)
FT800_SETMATRIX = (0xFFFFFF2A)
FT800_SKETCH = (0xFFFFFF30)
FT800_SLIDER = (0xFFFFFF10)
FT800_SNAPSHOT = (0xFFFFFF1F)
FT800_SPINNER = (0xFFFFFF16)
FT800_STOP = (0xFFFFFF17)
FT800_SWAP = (0xFFFFFF01)
FT800_TEXT = (0xFFFFFF0C)
FT800_TOGGLE = (0xFFFFFF12)
FT800_TRACK = (0xFFFFFF2C)
FT800_TRANSLATE = (0xFFFFFF27)

# Functions
FT800_FUNC_NEVER = (0)
FT800_FUNC_LESS = (1)
FT800_FUNC_LEQUAL = (2)
FT800_FUNC_GREATER = (3)
FT800_FUNC_GEQUAL = (4)
FT800_FUNC_EQUAL = (5)
FT800_FUNC_NOTEQUAL = (6)
FT800_FUNC_ALWAYS = (7)

# Primitives
FT800_BITMAPS = (1)
FT800_POINTS = (2)
FT800_LINES = (3)
FT800_LINE_STRIP = (4)
FT800_EDGE_STRIP_R = (5)
FT800_EDGE_STRIP_L = (6)
FT800_EDGE_STRIP_A = (7)
FT800_EDGE_STRIP_B = (8)
FT800_RECTS = (9)

# Formats
FT800_ARGB1555 = (0)
FT800_L1 = (1)
FT800_L4 = (2)
FT800_L8 = (3)
FT800_RGB332 = (4)
FT800_ARGB2 = (5)
FT800_ARGB4 = (6)
FT800_RGB565 = (7)
FT800_PALETTED = (8)
FT800_TEXT8X8 = (9)
FT800_TEXTVGA = (10)
FT800_BARGRAPH = (11)

# Filters
FT800_NEAREST = (0)
FT800_BILINEAR = (1)

# Wrap modes
FT800_BORDER = (0)
FT800_REPEAT = (1)

# Blend functions
FT800_BLEND_ZERO = (0)
FT800_BLEND_ONE = (1)
FT800_BLEND_SRC_ALPHA = (2)
FT800_BLEND_DST_ALPHA = (3)
FT800_BLEND_ONE_MINUS_SRC_ALPHA = (4)
FT800_BLEND_ONE_MINUS_DST_ALPHA = (5)

# Options
FT800_OPT_3D = (0)
FT800_OPT_RGB565 = (0)
FT800_OPT_MONO = (1)
FT800_OPT_NODL = (2)
FT800_OPT_FLAT = (256)
FT800_OPT_SIGNED = (256)
FT800_OPT_CENTERX = (512)
FT800_OPT_CENTERY = (1024)
FT800_OPT_CENTER = (1536)
FT800_OPT_RIGHTX = (2048)
FT800_OPT_NOBACK = (4096)
FT800_OPT_NOTICKS = (8192)
FT800_OPT_NOHM = (16384)
FT800_OPT_NOPOINTER = (16384)
FT800_OPT_NOSECS = (32768)
FT800_OPT_NOHANDS = (49152)


def enable(mikrobus_index):
    """Turn on and initialise the EVE click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to initialise the click board
    """
    ret = _LIB.eve_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("eve click enable failed")


def disable(mikrobus_index):
    """Turn off the EVE click.

    mikrobus_index: must be 0 (MIKROBUS_1) or 1 (MIKROBUS_2)

    Note: An exception is thrown if it fails to turn off the click board
    """
    ret = _LIB.eve_click_disable(mikrobus_index)
    if ret < 0:
        raise Exception("eve click disable failed")


def disable_buffering():
    """Disable buffering of graphic commands."""
    _LIB.eve_click_disable_buffering()


def enable_buffering():
    """Enable buffering of graphic commands."""
    _LIB.eve_click_disable_buffering()


def is_buffering_enabled():
    """Returns the state of the buffering of graphic commands."""
    return _LIB.eve_click_is_buffering_enabled()


def clear(r=0, g=0, b=0):
    """ Clear the screen in a specific color (default: black)

    r: Red component, must be in range 0..255

    g: Green component, must be in range 0..255

    b: Blue component, must be in range 0..255

    Note: An exception is thrown if it fails to clear the screen.
    """
    ret = _LIB.eve_click_clear(r, g, b)
    if ret < 0:
        raise Exception("eve click clear failed")


def draw(cmd, args):
    """Append a graphic command to the buffer.

    If buffering is disabled, the command is immediately send to the EVE Click.

    cmd: Opcode of the command

    args: List of arguments of the command

    Note: An exception is thrown if it fails to handle the command.
    """
    ret = _LIB.eve_click_draw(cmd, *args)
    if ret < 0:
        raise Exception("eve click draw failed")


def display():
    """Flush the buffer and display the frame on the screen.

    Note: An exception is thrown if it fails to display the frame.
    """
    ret = _LIB.eve_click_display()
    if ret < 0:
        raise Exception("eve click display failed")


def load_image(ptr, options, data):
    """Load a JPEG image in the FT800 chip memory.

    ptr: Starting address to decompress the image

    options: Can be FT800_OPT_RGB565 or FT800_OPT_MONO

    data: A list of bytes

    Note: An exception is thrown if it fails to load the image in the memory of
    the FT800 chip.
    """
    length = len(data)
    _data = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.eve_click_load_image(ptr, options, _data, length)
    if ret < 0:
        raise Exception("eve click load image failed")


def inflate(ptr, data):
    """Decompress some data in FT800 memory.

    The data must have been compressed using the DEFLATE algorithm.

    ptr: Starting address to decompress data

    data: A list of bytes.

    Note: An exception is thrown if it fails to decompress data.
    """
    length = len(data)
    _data = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.eve_click_inflate(ptr, _data, length)
    if ret < 0:
        raise Exception("eve click inflate failed")


def get_ptr():
    """Return the end address of data decompressed using inflate.

    Note: An exception is thrown if it fails to get the end address.
    """
    ptr = ctypes.c_uint32(0)
    ret = _LIB.eve_click_get_ptr(ctypes.byref(ptr))
    if ret < 0:
        raise Exception("eve click get ptr failed")
    return ptr.value


def load_identity():
    """Set the bitmap transformation matrix to identity.

    Note: An exception is thrown if it cannot set the bitmap transformation
    matrix to identity.
    """
    ret = _LIB.eve_click_load_identity()
    if ret < 0:
        raise Exception("eve click load identity failed")


def translate(tx, ty):
    """Perform a translation on the bitmap transformation matrix.

    tx: 16.16 fixed point x coordinate

    ty: 16.16 fixed point y coordinate

    Note: An exception is thrown if it fails to perform the translation on the
    bitmap transformation matrix.
    """
    ret = _LIB.eve_click_translate(tx, ty)
    if ret < 0:
        raise Exception("eve click translate failed")


def scale(sx, sy):
    """Perform a scale operation on the bitmap transformation matrix.

    sx: 16.16 fixed point x factor

    sy: 16.16 fixed point y factor

    Note: An exception is thrown if it fails to perform this operation.
    """
    ret = _LIB.eve_click_scale(sx, sy)
    if ret < 0:
        raise Exception("eve click scale failed")


def rotate(angle):
    """Perform a rotation matrix.

    angle: clockwise rotaion angle in units of 1/65536 of a circle.

    Note: An exception is thrown if it fails to perform this operation.
    """
    ret = _LIB.eve_click_rotate(angle)
    if ret < 0:
        raise Exception("eve click rotate failed")


def get_matrix():
    """Returns the bitmap transformation matrix currently in use.

    The format of the matrix is a list of 32 bits:
    [ a, b, c
      d, e, f]

    Note: An exception is thrown if it fails to retrieve the bitmap
    transformation matrix.
    """
    a = ctypes.c_int32(0)
    b = ctypes.c_int32(0)
    c = ctypes.c_int32(0)
    d = ctypes.c_int32(0)
    e = ctypes.c_int32(0)
    f = ctypes.c_int32(0)
    ret = _LIB.eve_click_get_matrix(ctypes.byref(a),
                                    ctypes.byref(b),
                                    ctypes.byref(c),
                                    ctypes.byref(d),
                                    ctypes.byref(e),
                                    ctypes.byref(f))
    if ret < 0:
        raise Exception("eve click get matrix failed")
    return [a.value, b.value, c.value,
            d.value, e.value, f.value]


def set_matrix():
    """Update the bitmap transformation matrix.

    It is necessary to call this function after performing some operations
    on the bitmap transformation matrix, otherwise the matrix will not change.

    Note: An exception is thrown if it fails to update the bitmap
    transformation matrix.
    """
    ret = _LIB.eve_click_set_matrix()
    if ret < 0:
        raise Exception("eve click set matrix failed")


def memcrc(ptr, byte_count):
    """Compute the CRC32 of a memory region of the FT800.

    ptr: Starting address of the memory region

    byte_count: Length of the memory region

    Note: An exception is thrown if it fails to compute the CRC of a memory
    region.
    """
    crc = ctypes.c_uint32(0)
    ret = _LIB.eve_click_memcrc(ptr, byte_count, ctypes.byref(crc))
    if ret < 0:
        raise Exception("eve click memcrc failed")
    return crc.value


def memset(ptr, value, byte_count):
    """Set some bytes to a specific value in the memory of the FT800.

    ptr: Starting address of the memory region

    value: 8-bit value

    byte_count: Length of the memory region

    Note: An exception is thrown if it fails to set the memory region.
    """
    ret = _LIB.eve_click_memset(ptr, value, byte_count)
    if ret < 0:
        raise Exception("eve click memset failed")


def memcpy(dest, src, byte_count):
    """Copy some bytes from one memory region to another.

    dest: Destination address to copy to.

    src: Source address to copy from.

    byte_count: Number of bytes to copy.

    Note: An exception is thrown if it fails to copy the memory region.
    """
    ret = _LIB.eve_click_memcpy(dest, src, byte_count)
    if ret < 0:
        raise Exception("eve click memcpy failed")


def memzero(ptr, byte_count):
    """Set to zero a memory region of the FT800.

    ptr: Starting address of the memory region.

    byte_count: Number of bytes to set to 0.

    Note: An exception is thrown if it fails to set to zero a memory region.
    """
    ret = _LIB.eve_click_memzero(ptr, byte_count)
    if ret < 0:
        raise Exception("eve click memzero failed")


def ftdi_logo():
    """Display the FTDI logo on the screen.

    This functions takes about 2.5 seconds to complete.

    Note: An exception is thrown if it fails to display the logo.
    """
    ret = _LIB.eve_click_ftdi_logo()
    if ret < 0:
        raise Exception("eve click ftdi logo failed")


def snapshot(ptr):
    """Take a snapshot of the screen.

    Returns the snapshot as a list of bytes of length 261120. The format is
    RGB565. This function might take up to several seconds to complete depending
    on the speed of the SPI bus.

    ptr: Address in FT800 memory to store the snapshot.

    Note: An exception is thrown if it fails to take a snapshot.
    """
    data = (ctypes.c_uint8 * 261120)()
    ret = _LIB.eve_click_snapshot(ptr, data)
    if ret < 0:
        raise Exception("eve click snapshot failed")
    return [data[i] for i in range(261120)]


def spinner(x, y, style, scale_factor):
    """Display a spinner on the screen:

    x: X screen coordinate of top left of spinner

    y: Y screen coordinate of top right of spinner

    style: Must be in range 0 to 3

    scale_factor: Scaling coefficient. 0 for no scaling, 1: half screen,
    2: full screen

    Note: An exception is thrown if it fails to display the spinner.
    """
    ret = _LIB.eve_click_spinner(x, y, style, scale_factor)
    if ret < 0:
        raise Exception("eve click spinner failed")


def stop():
    """Stop a spinner or a screensaver.

    Note: An exception is thrown if it fails to stop the spinner of the
    screensaver.
    """
    ret = _LIB.eve_click_stop()
    if ret < 0:
        raise Exception("eve click stop failed")


def coldstart():
    """Reset the coprocessor of the FT800.

    Note: An exception is thrown if it fails to reset the coprocessor.
    """
    ret = _LIB.eve_click_coldstart()
    if ret < 0:
        raise Exception("eve click coldstart failed")


def screensaver():
    """Display the screensaver on screen.

    Note: An exception is thrown if it fails to display the screensaver.
    """
    ret = _LIB.eve_click_screensaver()
    if ret < 0:
        raise Exception("eve click screensaver failed")


def set_backlight_intensity(intensity):
    """Set the intensity of the backlight.

    At initialisation, the intensity is set to the maximum (100).

    intensity: must be in range 0..100

    Note: An exception is thrown if it fails to set the intensity of the
    backlight.
    """
    ret = _LIB.eve_click_set_backlight_intensity(intensity)
    if ret < 0:
        raise Exception("eve click set backlight intensity failed")


def attach_touch_callback(callback):
    """Set the function to call whenever a touch screen conversion is complete
    (about 60 times a second).

    This callback must be able to take two 16-bit unsigned integers (the
    coordinates of the event in screen coordinates).
    """
    global _CALLBACK
    ptr = _CALLBACK_TYPE(callback)
    _LIB.eve_click_attach_touch_callback(ptr)
    _CALLBACK = ptr


def attach_touch_event_callback(callback):
    """Set the function to call when a touch event is detected.

    This callback does not take any arguments.
    """
    global _EVENT_CALLBACK
    ptr = _CALLBACK_EVENT_TYPE(callback)
    _LIB.eve_click_attach_touch_event_callback(ptr)
    _EVENT_CALLBACK = ptr


def calibrate():
    """Calibrate the touch screen.

    Note: An exception is thrown if it fails to calibrate the touch screen.
    """
    ret = _LIB.eve_click_calibrate()
    if ret < 0:
        raise Exception("eve click calibrate failed")


def get_calibration_matrix():
    """Retrieve calibration matrix.

    format:
    | a b c |
    | d e f |
    Each value of the matrix is in 16.16 fixed-point format.
    The return value is a tuple (a, b, c, d, e, f)

    Note: An exception is thrown if it fails to get the calibration matrix.
    """
    a = ctypes.c_uint32(0)
    b = ctypes.c_uint32(0)
    c = ctypes.c_uint32(0)
    d = ctypes.c_uint32(0)
    e = ctypes.c_uint32(0)
    f = ctypes.c_uint32(0)
    ret = _LIB.eve_click_get_calibration_matrix(ctypes.byref(a),
                                                ctypes.byref(b),
                                                ctypes.byref(c),
                                                ctypes.byref(d),
                                                ctypes.byref(e),
                                                ctypes.byref(f))
    if ret < 0:
        raise Exception("eve click get calibration matrix failed")
    return (a.value, b.value, c.value, d.value, e.value, f.value)


def set_calibration_matrix(a, b, c, d, e, f):
    """Set the calibration matrix.

    format:
    | a b c |
    | d e f |

    Each number must be in fixed point 16.16 format.

    Note: An exception is thrown if it fails to set the calibration matrix.
    """
    ret = _LIB.eve_click_set_calibration_matrix(a, b, c, d, e, f)
    if ret < 0:
        raise Exception("eve click set calibration matrix failed")
