        #reikia padaryti palete pagal:
#https://www.shadertoy.com/view/ll2GD3#

import time
import colorsys
import math

from neopixel import *


# LED strip configuration:
LED_COUNT      = 72      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

#Grazina reiksmes atitikmeny kitoje skaleje
# in_min in_max tai skale, kurios reiksme yra paduodamas
# out_min out_max tai skale, kurios reiksme norima gauti
def map_value(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def gamma(value):
        factor = 2.8
        return int(pow((float(value)/255),factor)*255+0.5)

def getRED(RGB):
  return RGB / 65536

def getGREEN(RGB):
  return RGB % 65536 / 256

def getBLUE(RGB):
  return RGB % 256

def cos8(value):
  return int(math.cos(float(value)/128*3.14159+3.14159)*128)+128

def sin8(value):
  return int(math.sin(float(value)/128*3.14159+3.14159)*128)+128

  def SINValue(range, value):
  if range>=1:
    range = range - 1;
  return abs((int(math.sin((float(value)/float(range)-float(range)/2)*math.pi)*float(range))-range)/2)
#Is HEX kodo generuoja RGB. Grazina INT reiksme
# paduodamas hex kaip stringas. Pvz. '#00FF00'
def HEX2RGB(hex):
  tmp = [int(hex[i:i+2], 16) for i in range(1,6,2)]  #Generuoja tuplet'a (list'a)
  return RGBColor(tmp[0], tmp[1], tmp[2])

#Is RGB sugeneruoja HEX koda
def RGB2HEX(RGB):
  RGB = [getRED(RGB), getGREEN(RGB), getBLUE(RGB)]
  return "#"+"".join(["0{0:x}".format(v) if v < 16 else
            "{0:x}".format(v) for v in RGB])

#RGB spalvos modelis (Grazina INT tipo reiksme)
# Red - raudona
# Green - Zalia
# Blue - Melyna
def RGBColor(r, g, b):
        return Color(r, g, b)

#HSV spalvos modelis (Grazina INT  tipo reiksme)
#   Hue - Spalva [0-359] (0 - raudona, 42 - geltona, 85 - zalia, 128 - zydra, 171 - melyna, 213 - violetine) 
#   Saturation - spalvos intensyvumas (0 - balta, 255 - Ryskiausia spalva)
#   Value - Spalvos reksme (0 - juoda, 255 - Ryskiausia spalva)
def HSVColor(h, s, v):  #Hue - Spalva, Saturation - spalvosintensyvumas (0 - spalva isjungta, 255-ryskiausia), 
        h, s, v = float(h)/359, float(s)/255, float(v)/255
        r, g, b = colorsys.hsv_to_rgb(h, s, v)
        r, g, b = int(r*255), int(g*255), int(b*255)
        return Color(r, g, b)

        def linear_gradient(start, finish=0, steps=3, step=1, use_gamma=True):
#  print steps
#  print step
  s = (getRED(start), getGREEN(start), getBLUE(start))
  f = (getRED(finish), getGREEN(finish), getBLUE(finish))
  # Initilize a list of the output colors with the starting color
  if steps > 1:
    RGB_list = [s]
    curr_vector = [
      int(s[j] + (float(step)/(steps-1))*(f[j]-s[j]))
      for j in range(3)
    ]
  else:
    curr_vector = [
      int((f[j]+s[j])/2)
      for j in range(3)
    ]
  r, g, b = curr_vector[0], curr_vector[1], curr_vector[2]
  if use_gamma:
    r, g, b = gamma(r), gamma(g), gamma(b)
  return RGBColor(r, g, b)

  #Grazina spalva is paletes
def getColorFromPalette(num, use_gamma=True):
        myPalette = [(0, RGBColor(255,0,0)),
                     (1,RGBColor(0,255,0)),
                     (2,RGBColor(0,0,255)),
                     (3,RGBColor(0,0,0)),
                     (65, RGBColor(255,255,255)),
                     (80, RGBColor(255,0,255)),
                     (100, RGBColor(0,255,0)),
                     (127, RGBColor(0,0,0)),
                     (128, RGBColor(0,0,0)),
                     (155, RGBColor(0,255,0)),
                     (175, RGBColor(255,0,255)),
                     (190, RGBColor(255,255,255)),
                     (252,RGBColor(0,0,0)),
                     (253,RGBColor(0,0,255)),
                     (254,RGBColor(0,255,0)),
                     (255,RGBColor(255,0,0))]
        startColorIndex, startColor = 0, RGBColor(0,0,0)
        finishColorIndex, finishColor = 255,  RGBColor(0,0,0)
        for i in range(len(myPalette)):
                if myPalette[i][0]<=num:
                        startColor = myPalette[i][1]
                        startColorIndex = myPalette[i][0]
                if myPalette[i][0]>=num:
                        finishColor = myPalette[i][1]
                        finishColorIndex = myPalette[i][0]
                        break
        rezColor = linear_gradient(startColor, finishColor, finishColorIndex - startColorIndex+1, num - startColorIndex, use_gamma)
#       print "%d - %s _ is _  %d - %s ........ %d - %s" % (num, RGB2HEX(rezColor), startColorIndex, RGB2HEX(startColor), finishColorIndex, RGB2HEX(finishCol$

       return rezColor

# Main program logic follows:
if __name__ == '__main__':
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        # Intialize the library (must be called once before other functions).
        strip.begin()
        strip.setBrightness(55)
        for i in range(256):
                print sin8(i)
        print 'Press Ctrl-C to quit.'
        strip.show()
#################################################################
##### Visos paletes parodymas
#################################################################
#       for i in range(strip.numPixels()):
#               strip.setPixelColor(i,getColorFromPalette(map_value(i,0,71,0,255)))
#       strip.show()
#       time.sleep(5)
################################################################

#        for i in range(strip.numPixels()):
#               strip.setPixelColor(i,linear_gradient(RGBColor(0,0,255), RGBColor(255,0,0),72,i))
#        strip.show()
#        time.sleep(5)

#        for i in range(strip.numPixels()):
#               strip.setPixelColor(i,linear_gradient(RGBColor(0,0,255), RGBColor(255,0,0),72,SINValue(72,i)))
#        strip.show()
#        time.sleep(5)

        stp = 0
#       stp = 254
        while True:
#                stp = stp + 1
#                if stp >= 720:
#                       stp = 0
#                clr = linear_gradient(RGBColor(25,25,0), RGBColor(0,25,25),360,SINValue(360,abs(stp-360)))
#               if stp >= 511:
#                       stp = 0
#               clr = getColorFromPalette(abs(stp-255))
#               for i in range(strip.numPixels()):
#                       strip.setPixelColor(i, clr)
 #               strip.show()
                stp = stp + 1;
                for i in range(72):
                        inx = (i*3+stp+sin8(i*16))%256
#                       print inx
#                       strip.setPixelColor(i, getColorFromPalette(inx))
                        strip.setPixelColor(i, HSVColor(inx, 255, 255))

                strip.show()
#               time.sleep(0.01)
################################################################
####### Visos paletes testavimas
################################################################
#               for j in range(185):
#                       for i in range(72):
#                               strip.setPixelColor(i, getColorFromPalette(i+j))
#                       strip.show()
#               time.sleep(5)
#               for j in range(184,-1,-1):
#                       for i in range(72):
#                               strip.setPixelColor(i, getColorFromPalette(i+j))
#                       strip.show()
#               time.sleep(5)
###############################################################
###### GAMMA palyginimas
###############################################################
#               for j in range(72):
                #       strip.setPixelColor(j, RGBColor(map_value(j,0,71,0,255),0,0))
                #       strip.setPixelColor(j, linear_gradient(RGBColor(255,0,0),RGBColor(0,0,255),72,j,False))
#                       strip.setPixelColor(j, getColorFromPalette(map_value(j,0,71,0,255), False))
#               strip.show()
#               time.sleep(5)
#               for j in range(72):
                #       strip.setPixelColor(j, RGBColor(gamma(map_value(j,0,71,0,255)),0,0))
                #       strip.setPixelColor(j, linear_gradient(RGBColor(255,0,0),RGBColor(0,0,255),72,j,True))
#                       strip.setPixelColor(j, getColorFromPalette(map_value(j,0,71,0,255), True))
#               strip.show()
#               time.sleep(5)

