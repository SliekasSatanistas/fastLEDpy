from ctypes import *

import neopixel_image
import math

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


def cos8(value):
  return int(math.cos(float(value)/128*math.pi+math.pi)*128)+128
#return int(math.cos(float(value)/128))

def sin8(value):
  return int(math.sin(float(value)/128*math.pi+math.pi)*128)+128

ax = neopixel_image.Axis(256, 40)

pixR = neopixel_image.Graph(ax, (255, 0, 0))
pixR.putPixelCoord((0, 0))
pixR.putPixelCoord((20, -2))
pixR.putPixelCoord((40, 50))
pixR.putPixelCoord((60, 60))
pixR.putPixelCoord((80, 257))
pixR.putPixelCoord((100, 110))
pixR.putPixelCoord((120, 130))

pixG = neopixel_image.Graph(ax, (255, 255, 0))
pixG.putPixelCoord((0, 0))
pixG.putPixelCoord((10, 40))
pixG.putPixelCoord((30, 20))
pixG.putPixelCoord((40, 50))
pixG.putPixelCoord((50, 30))
pixG.putPixelCoord((60, -1))
pixG.putPixelCoord((70, 20))
pixG.putPixelCoord((80, 60))
pixG.putPixelCoord((90, 256))
pixG.putPixelCoord((100, 200))
pixG.putPixelCoord((110, 200))

pixB = neopixel_image.Graph(ax, (0, 0, 255))
pixB.putPixelCoord((100, 0))
pixB.putPixelCoord((110, 40))
pixB.putPixelCoord((130, 20))
pixB.putPixelCoord((140, 50))
pixB.putPixelCoord((150, 30))
pixB.putPixelCoord((160, -1))
pixB.putPixelCoord((170, 20))

pixG = neopixel_image.Graph(ax, (0, 255, 0))
for i in range(600):
                pixG.putPixel(cos8(i))


#pixZ = neopixel_image.Graph(ax, (0, 255, 255))
#for i in range(600):
#                pixZ.putPixel(sin8(i))

neopixel_image.saveImage()

