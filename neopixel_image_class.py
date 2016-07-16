from PIL import Image,  ImageDraw

imageSizeX=1000
imageSizeY=700
im = Image.new("RGB", (imageSizeX, imageSizeY), "black")
draw = ImageDraw.Draw(im)
imageFormat = 'PNG'
imageName = 'tstlib.png'
lastPixelX = None
lastPixelY = None
pixColor = (255, 0, 0)
pixColorLower = 4

class Axis:
    axisGap = 20
    axisSize = 256
    im = None

    def drawAxis():
        fillColor = (50, 50, 50)
        draw.line((axisGap, axisSize+axisGap, imageSizeX-axisGap, axisSize+axisGap), fill=fillColor)
        draw.line((axisGap, axisGap, axisGap, axisGap+axisSize), fill=fillColor)
        draw.line((axisGap,  axisGap-1,  imageSizeX-axisGap,   axisGap-1), fill=fillColor)
        draw.text((axisGap-19, axisGap-5), '255')
        draw.text((axisGap-8, axisSize+axisGap-5), '0')

    def __init__(self,  img):
        self.im = img
        self.drawAxis()
    

def saveImage():
    im.save(imageName,  imageFormat)

#Funtion reaclculate X cords of axis to real coord (for draw'ing)
def getRealX(x):
    return(axisGap+1+x)
#Funtion reaclculate Y cords of axis to real coord (for draw'ing)    
def getRealY(y):
    return(axisGap+axisSize-1-y)    

def putAxisPixel(x,  y):
    #if (lastPixelX is not None) and (lastPixelY is not None):
    global lastPixelX
    global lastPixelY
    if lastPixelX is not None and lastPixelY is not None:
        draw.line((getRealX(lastPixelX),  getRealY(lastPixelY),  getRealX(x),  getRealY(y)), (pixColor[0] / pixColorLower,  pixColor[1] / pixColorLower,  pixColor[2] / pixColorLower))
        im.putpixel((getRealX(lastPixelX), getRealY(lastPixelY)), pixColor)
    lastPixelX = x
    lastPixelY = y
    
    if y > (axisSize-1):
        draw.line((getRealX(x),  axisGap-2,  getRealX(x), axisGap-6))
    
    if y < 0:
        draw.line((getRealX(x),  axisSize+axisGap+2,  getRealX(x), axisSize+axisGap+6))
     
    im.putpixel((getRealX(x), getRealY(y)), pixColor)


tst = Axis(im)
saveImage()
