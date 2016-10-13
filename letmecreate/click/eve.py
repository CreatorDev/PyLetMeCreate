#!/usr/bin/env python3


import ctypes

_LIB = ctypes.CDLL('libletmecreate_click.so')
_CALLBACK_TYPE = ctypes.CFUNCTYPE(None, ctypes.c_uint16, ctypes.c_uint16)
_CALLBACK = None

# Display list opcodes
FT800_ALPHA_FUNC                = (0x09 << 24)
FT800_BEGIN                     = (0x1F << 24)
FT800_BITMAP_HANDLE             = (0x05 << 24)
FT800_BITMAP_LAYOUT             = (0x07 << 24)
FT800_BITMAP_SIZE               = (0x08 << 24)
FT800_BITMAP_SOURCE             = (0x01 << 24)
FT800_BITMAP_TRANSFORM_A        = (0x15 << 24)
FT800_BITMAP_TRANSFORM_B        = (0x16 << 24)
FT800_BITMAP_TRANSFORM_C        = (0x17 << 24)
FT800_BITMAP_TRANSFORM_D        = (0x18 << 24)
FT800_BITMAP_TRANSFORM_E        = (0x19 << 24)
FT800_BITMAP_TRANSFORM_F        = (0x1F << 24)
FT800_BLEND_FUNC                = (0x0B << 24)
FT800_CALL                      = (0x1D << 24)
FT800_CELL                      = (0x06 << 24)
FT800_CLEAR                     = (0x26 << 24)
FT800_CLEAR_COLOR_A             = (0x0F << 24)
FT800_CLEAR_COLOR_RGB           = (0x02 << 24)
FT800_CLEAR_STENCIL             = (0x11 << 24)
FT800_CLEAR_TAG                 = (0x06 << 24)
FT800_COLOR_A                   = (0x10 << 24)
FT800_COLOR_MASK                = (0x20 << 24)
FT800_COLOR_RGB                 = (0x04 << 24)
FT800_DISPLAY                   = (0)
FT800_END                       = (0x21 << 24)
FT800_JUMP                      = (0x1E << 24)
FT800_LINE_WIDTH                = (0x06 << 24)
FT800_MACRO                     = (0x25 << 24)
FT800_POINT_SIZE                = (0x0D << 24)
FT800_RESTORE_CONTEXT           = (0x23 << 24)
FT800_RETURN                    = (0x24 << 24)
FT800_SAVE_CONTEXT              = (0x22 << 24)
FT800_SCISSOR_SIZE              = (0x1C << 24)
FT800_SCISSOR_XY                = (0x1B << 24)
FT800_STENCIL_FUNC              = (0x0A << 24)
FT800_STENCIL_MASK              = (0x13 << 24)
FT800_STENCIL_OP                = (0x0C << 24)
FT800_TAG                       = (0x03 << 24)
FT800_TAG_MASK                  = (0x14 << 24)
FT800_VERTEX2F                  = (0x01 << 30)
FT800_VERTEX2II                 = (0x02 << 30)

# Coprocessor opcodes
FT800_APPEND                    = (0xFFFFFF02)
FT800_BGCOLOR                   = (0xFFFFFF09)
FT800_BUTTON                    = (0xFFFFFF0D)
FT800_CALIBRATE                 = (0xFFFFFF15)
FT800_CLOCK                     = (0xFFFFFF14)
FT800_COLDSTART                 = (0xFFFFFF32)
FT800_DIAL                      = (0xFFFFFF2D)
FT800_DLSTART                   = (0xFFFFFF00)
FT800_FGCOLOR                   = (0xFFFFFF0A)
FT800_GAUGE                     = (0xFFFFFF13)
FT800_GETMATRIX                 = (0xFFFFFF33)
FT800_GETPTR                    = (0xFFFFFF23)
FT800_GRADCOLOR                 = (0xFFFFFF34)
FT800_GRADIENT                  = (0xFFFFFF0B)
FT800_INFLATE                   = (0xFFFFFF22)
FT800_INTERRUPT                 = (0xFFFFFF02)
FT800_KEYS                      = (0xFFFFFF0E)
FT800_LOADIDENTITY              = (0xFFFFFF26)
FT800_LOADIMAGE                 = (0xFFFFFF24)
FT800_LOGO                      = (0xFFFFFF31)
FT800_MEMCPY                    = (0xFFFFFF1D)
FT800_MEMCRC                    = (0xFFFFFF18)
FT800_MEMSET                    = (0xFFFFFF1B)
FT800_MEMWRITE                  = (0xFFFFFF1A)
FT800_MEMZERO                   = (0xFFFFFF1C)
FT800_NUMBER                    = (0xFFFFFF2E)
FT800_PROGRESS                  = (0xFFFFFF0F)
FT800_REGREAD                   = (0xFFFFFF19)
FT800_ROTATE                    = (0xFFFFFF29)
FT800_SCALE                     = (0xFFFFFF28)
FT800_SCREENSAVER               = (0xFFFFFF2F)
FT800_SCROLLBAR                 = (0xFFFFFF11)
FT800_SETMATRIX                 = (0xFFFFFF2A)
FT800_SKETCH                    = (0xFFFFFF30)
FT800_SLIDER                    = (0xFFFFFF10)
FT800_SNAPSHOT                  = (0xFFFFFF1F)
FT800_SPINNER                   = (0xFFFFFF16)
FT800_STOP                      = (0xFFFFFF17)
FT800_SWAP                      = (0xFFFFFF01)
FT800_TEXT                      = (0xFFFFFF0C)
FT800_TOGGLE                    = (0xFFFFFF12)
FT800_TRACK                     = (0xFFFFFF2C)
FT800_TRANSLATE                 = (0xFFFFFF27)

# Functions
FT800_FUNC_NEVER        = (0)
FT800_FUNC_LESS         = (1)
FT800_FUNC_LEQUAL       = (2)
FT800_FUNC_GREATER      = (3)
FT800_FUNC_GEQUAL       = (4)
FT800_FUNC_EQUAL        = (5)
FT800_FUNC_NOTEQUAL     = (6)
FT800_FUNC_ALWAYS       = (7)

# Primitives
FT800_BITMAPS           = (1)
FT800_POINTS            = (2)
FT800_LINES             = (3)
FT800_LINE_STRIP        = (4)
FT800_EDGE_STRIP_R      = (5)
FT800_EDGE_STRIP_L      = (6)
FT800_EDGE_STRIP_A      = (7)
FT800_EDGE_STRIP_B      = (8)
FT800_RECTS             = (9)

# Formats
FT800_ARGB1555          = (0)
FT800_L1                = (1)
FT800_L4                = (2)
FT800_L8                = (3)
FT800_RGB332            = (4)
FT800_ARGB2             = (5)
FT800_ARGB4             = (6)
FT800_RGB565            = (7)
FT800_PALETTED          = (8)
FT800_TEXT8X8           = (9)
FT800_TEXTVGA           = (10)
FT800_BARGRAPH          = (11)

# Filters
FT800_NEAREST           = (0)
FT800_BILINEAR          = (1)

# Wrap modes
FT800_BORDER            = (0)
FT800_REPEAT            = (1)

# Blend functions
FT800_BLEND_ZERO                    = (0)
FT800_BLEND_ONE                     = (1)
FT800_BLEND_SRC_ALPHA               = (2)
FT800_BLEND_DST_ALPHA               = (3)
FT800_BLEND_ONE_MINUS_SRC_ALPHA     = (4)
FT800_BLEND_ONE_MINUS_DST_ALPHA     = (5)

# Options
FT800_OPT_3D                        = (0)
FT800_OPT_RGB565                    = (0)
FT800_OPT_MONO                      = (1)
FT800_OPT_NODL                      = (2)
FT800_OPT_FLAT                      = (256)
FT800_OPT_SIGNED                    = (256)
FT800_OPT_CENTERX                   = (512)
FT800_OPT_CENTERY                   = (1024)
FT800_OPT_CENTER                    = (1536)
FT800_OPT_RIGHTX                    = (2048)
FT800_OPT_NOBACK                    = (4096)
FT800_OPT_NOTICKS                   = (8192)
FT800_OPT_NOHM                      = (16384)
FT800_OPT_NOPOINTER                 = (16384)
FT800_OPT_NOSECS                    = (32768)
FT800_OPT_NOHANDS                   = (49152)


def enable(mikrobus_index):
    ret = _LIB.eve_click_enable(mikrobus_index)
    if ret < 0:
        raise Exception("eve click enable failed")


def disable(mikrobus_index):
    ret = _LIB.eve_click_disable(mikrobus_index)
    if ret < 0:
        raise Exception("eve click disable failed")


def disable_buffering():
    _LIB.eve_click_disable_buffering()


def enable_buffering():
    _LIB.eve_click_disable_buffering()


def is_buffering_enabled():
    ret = _LIB.eve_click_is_buffering_enabled()
    if ret < 0:
        raise Exception("eve click is buffering enabled failed")
    return ret


def clear(r = 0, g = 0, b = 0):
    ret = _LIB.eve_click_clear(r, g, b)
    if ret < 0:
        raise Exception("eve click clear failed")


def draw(cmd, args):
    ret = _LIB.eve_click_draw(cmd, *args)
    if ret < 0:
        raise Exception("eve click draw failed")


def display():
    ret = _LIB.eve_click_display()
    if ret < 0:
        raise Exception("eve click display failed")


def load_image(ptr, options, data, count):
    length = len(data)
    _data = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.eve_click_load_image(ptr, options, _data, count)
    if ret < 0:
        raise Exception("eve click load image failed")


def inflate(ptr, data, count):
    length = len(data)
    _data = (ctypes.c_uint8 * length)(*data)
    ret = _LIB.eve_click_inflate(ptr, _data, count)
    if ret < 0:
        raise Exception("eve click inflate failed")


def get_ptr():
    ptr = ctypes.c_uint32(0)
    ret = _LIB.eve_click_get_ptr(ctypes.byref(ptr))
    if ret < 0:
        raise Exception("eve click get ptr failed")
    return ptr.value


def load_identity():
    ret = _LIB.eve_click_load_identity()
    if ret < 0:
        raise Exception("eve click load identity failed")


def translate(tx, ty):
    ret = _LIB.eve_click_translate(tx, ty)
    if ret < 0:
        raise Exception("eve click translate failed")


def scale(sx, sy):
    ret = _LIB.eve_click_scale(sx, sy)
    if ret < 0:
        raise Exception("eve click scale failed")


def rotate(angle):
    ret = _LIB.eve_click_rotate(angle)
    if ret < 0:
        raise Exception("eve click rotate failed")


def get_matrix():
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
    ret = _LIB.eve_click_set_matrix()
    if ret < 0:
        raise Exception("eve click set matrix failed")


def memcrc(ptr, byte_count):
    crc = ctypes.c_uint32(0)
    ret = _LIB.eve_click_memcrc(ptr, byte_count, ctypes.byref(crc))
    if ret < 0:
        raise Exception("eve click memcrc failed")
    return crc.value


def memset(ptr, value, byte_count):
    ret = _LIB.eve_click_memset(ptr, value, byte_count)
    if ret < 0:
        raise Exception("eve click memset failed")


def memcpy(dest, src, byte_count):
    ret = _LIB.eve_click_memcpy(dest, src, byte_count)
    if ret < 0:
        raise Exception("eve click memcpy failed")


def memzero(ptr, byte_count):
    ret = _LIB.eve_click_memzero(ptr, byte_count)
    if ret < 0:
        raise Exception("eve click memzero failed")


def ftdi_logo():
    ret = _LIB.eve_click_ftdi_logo()
    if ret < 0:
        raise Exception("eve click ftdi logo failed")


def snapshot(ptr):
    data = (ctypes.c_uint8 * 261120)()
    ret = _LIB.eve_click_snapshot(ptr, data);
    if ret < 0:
        raise Exception("eve click ftdi logo failed")
    return [data[i] for i in range(261120)]


def spinner(x, y, style, scale):
    ret = _LIB.eve_click_spinner(x, y, style, scale)
    if ret < 0:
        raise Exception("eve click spinner failed")


def stop():
    ret = _LIB.eve_click_stop()
    if ret < 0:
        raise Exception("eve click stop failed")


def coldstart():
    ret = _LIB.eve_click_coldstart()
    if ret < 0:
        raise Exception("eve click coldstart failed")


def screensaver():
    ret = _LIB.eve_click_screensaver()
    if ret < 0:
        raise Exception("eve click screensaver failed")


def set_backlight_intensity(intensity):
    ret = _LIB.eve_click_set_backlight_intensity(intensity)
    if ret < 0:
        raise Exception("eve click set backlight intensity failed")


def attach_touch_callback(callback):
    ptr = _CALLBACK_TYPE(callback)
    _LIB.eve_click_attach_touch_callback(ptr)
    _CALLBACK = callback


def calibrate():
    ret = _LIB.eve_click_calibrate()
    if ret < 0:
        raise Exception("eve click calibrate failed")
