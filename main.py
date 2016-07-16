from ctypes import *

import neopixel_image

#bool_ 	Boolean (True or False) stored as a byte
#int_ 	Default integer type (same as C long; normally either int64 or int32)
#intc 	Identical to C int (normally int32 or int64)
#intp 	Integer used for indexing (same as C ssize_t; normally either int32 or int64)
#int8 	Byte (-128 to 127)
#int16 	Integer (-32768 to 32767)
#int32 	Integer (-2147483648 to 2147483647)
#int64 	Integer (-9223372036854775808 to 9223372036854775807)
#uint8 	Unsigned integer (0 to 255)
#uint16 	Unsigned integer (0 to 65535)
#uint32 	Unsigned integer (0 to 4294967295)
#uint64 	Unsigned integer (0 to 18446744073709551615)
#import numpy as np



#lib8tion/math8.h

##Is http://slideplayer.com/slide/3426254/
#int8_t   -128 <= x <= 127
#int16_t  -32768 <= x <= 32767
#uint8_t  0 <= x <= 255
#uint16_t 0 <= x <= 65535

# add one byte to another, saturating at 0xFF
# @param i - first byte to add
# @param j - second byte to add
# @returns the sum of i & j, capped at 0xFF
#LIB8STATIC_ALWAYS_INLINE uint8_t qadd8( uint8_t i, uint8_t j)
def qadd8(i, j):
    t = i + j;
    if t > 255:
        t = 255;
    return t;


# Add one byte to another, saturating at 0x7F
# @param i - first byte to add
# @param j - second byte to add
# @returns the sum of i & j, capped at 0xFF
#LIB8STATIC_ALWAYS_INLINE int8_t qadd7( int8_t i, int8_t j)
def qadd7(i, j):
    t = i + j;
    if t > 127:
        t = 127;
    return t;

print (qadd8(255, 5));
i = c_ushort(-3);
print (i);


ax = neopixel_image.Axis(256, 40)

pixR = neopixel_image.Pixels(ax, (255, 0, 0))
pixR.putPixel((0, 0))
pixR.putPixel((20, -2))
pixR.putPixel((40, 50))
pixR.putPixel((60, 60))
pixR.putPixel((80, 257))
pixR.putPixel((100, 110))
pixR.putPixel((120, 130))

pixG = neopixel_image.Pixels(ax, (255, 255, 0))
pixG.putPixel((0, 0))
pixG.putPixel((10, 40))
pixG.putPixel((30, 20))
pixG.putPixel((40, 50))
pixG.putPixel((50, 30))
pixG.putPixel((60, -1))
pixG.putPixel((70, 20))
pixG.putPixel((80, 60))
pixG.putPixel((90, 256))
pixG.putPixel((100, 200))
pixG.putPixel((110, 200))

pixB = neopixel_image.Pixels(ax, (0, 0, 255))
pixB.putPixel((100, 0))
pixB.putPixel((110, 40))
pixB.putPixel((130, 20))
pixB.putPixel((140, 50))
pixB.putPixel((150, 30))
pixB.putPixel((160, -1))
pixB.putPixel((170, 20))

neopixel_image.saveImage()
