from ctypes import *

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
    if t > 255: t = 255;
    return t;

# Add one byte to another, saturating at 0x7F
# @param i - first byte to add
# @param j - second byte to add
# @returns the sum of i & j, capped at 0xFF
#LIB8STATIC_ALWAYS_INLINE int8_t qadd7( int8_t i, int8_t j)
def qadd7(i, j):
    t = i + j;
    if t > 127: t = 127;
    return t;

# Subtract one byte from another, saturating at 0x00
# @returns i - j with a floor of 0
#LIB8STATIC_ALWAYS_INLINE uint8_t qsub8( uint8_t i, uint8_t j)
def qsub8(i,  j):
    t = i - j;
    if t < 0: t = 0;
    return t;

# add one byte to another, with one byte result
#LIB8STATIC_ALWAYS_INLINE uint8_t add8( uint8_t i, uint8_t j)
def add8(i,  j):
    t = (i + j) & 0xFF;
    return t;
    
# subtract one byte from another, 8-bit result
#LIB8STATIC_ALWAYS_INLINE uint8_t sub8( uint8_t i, uint8_t j)
def sub8(i,  j):
    t = (i-j) & 0xFF;
    return t;
    
# Calculate an integer average of two unsigned
# 8-bit integer values (uint8_t).
# Fractional results are rounded down, e.g. avg8(20,41) = 30
#LIB8STATIC_ALWAYS_INLINE uint8_t avg8( uint8_t i, uint8_t j)   
def avg8(i,  j):
    t = ((i+j)& 0xFF) >> 1;
    return t;

# Calculate an integer average of two unsigned
# 16-bit integer values (uint16_t).
# Fractional results are rounded down, e.g. avg16(20,41) = 30
#LIB8STATIC_ALWAYS_INLINE uint16_t avg16( uint16_t i, uint16_t j)
def avg16(i,  j):
    return (((i & 0xFFFF) + (j & 0xFFFF))& 0xFFFF) >> 1;

# Calculate an integer average of two signed 7-bit
# integers (int8_t)
# If the first argument is even, result is rounded down.
# If the first argument is odd, result is result up.
#LIB8STATIC_ALWAYS_INLINE int8_t avg7( int8_t i, int8_t j)
def avg7(i,  j):
   t = ((i + j) >> 1) + (i & 0x1);
   return t & 0xFF;
   
# Calculate an integer average of two signed 15-bit
# integers (int16_t)
# If the first argument is even, result is rounded down.
# If the first argument is odd, result is result up.
#LIB8STATIC_ALWAYS_INLINE int16_t avg15( int16_t i, int16_t j)  
def avg15(i,  j):
    t = ((((i & 0xFFFF) + (j & 0xFFFF))& 0xFFFF) >> 1)  + (i & 0x1);
    return t & 0xFFFF;

#///       Calculate the remainder of one unsigned 8-bit
#///       value divided by anoter, aka A % M.
#///       Implemented by repeated subtraction, which is
#///       very compact, and very fast if A is 'probably'
#///       less than M.  If A is a large multiple of M,
#///       the loop has to execute multiple times.  However,
#///       even in that case, the loop is only two
#///       instructions long on AVR, i.e., quick.
#LIB8STATIC_ALWAYS_INLINE uint8_t mod8( uint8_t a, uint8_t m)
def mod8(a,  m):
    while a >=m:
        a -= m;
    return a;

#///          Add two numbers, and calculate the modulo
#///          of the sum and a third number, M.
#///          In other words, it returns (A+B) % M.
#///          It is designed as a compact mechanism for
#///          incrementing a 'mode' switch and wrapping
#///          around back to 'mode 0' when the switch
#///          goes past the end of the available range.
#///          e.g. if you have seven modes, this switches
#///          to the next one and wraps around if needed:
#///            mode = addmod8( mode, 1, 7);
#LIB8STATIC_ALWAYS_INLINESee 'mod8' for notes on performance.
#LIB8STATIC uint8_t addmod8( uint8_t a, uint8_t b, uint8_t m)
def addmod8(a,  b,  m):    
    a += b;
    while a >= m:
        a -= m;
    return a;
    
#/// 8x8 bit multiplication, with 8 bit result
#LIB8STATIC_ALWAYS_INLINE uint8_t mul8( uint8_t i, uint8_t j)   
def mul8(i,  j):
    return (i * j) & 0xFF;

#/// saturating 8x8 bit multiplication, with 8 bit result
#/// @returns the product of i * j, capping at 0xFF
#LIB8STATIC_ALWAYS_INLINE uint8_t qmul8( uint8_t i, uint8_t j)
def qmul8(i,  j):
    p = i + j;
    if p > 255: p=255;
    return p;

#/// take abs() of a signed 8-bit uint8_t
#LIB8STATIC_ALWAYS_INLINE int8_t abs8( int8_t i)
def abs8(i):
    if i < 0: i = -i;
    return i;
    
#///         square root for 16-bit integers
#///         About three times faster and five times smaller
#///         than Arduino's general sqrt on AVR.
#LIB8STATIC uint8_t sqrt16(uint16_t x)
def sqrt16(x):
    if x <= 1: return x;

    low = 1; # lower bound
    hi, mid = 0, 0;

    if x > 7904:  hi = 255;
    else:  hi = (x >> 5) + 8; #// initial estimate for upper bound
    

    while True:
        mid = (low + hi) >> 1;
        if mid * mid > x:
            hi = mid - 1;
        else:
            if mid == 255: return 255;
            low = mid + 1;
        if hi >= low: break;    
    return low - 1;  
    
print (qadd8(255, 5));
i = c_ushort(-3);
print (i);
print(sub8(255, 255))
print(c_uint8(255-255));
print(avg8(300, 400));
print(avg16(300, 400));
print(sqrt16(123123));
