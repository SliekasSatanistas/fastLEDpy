from PIL import Image,  ImageDraw

imageSizeX=1000
imageSizeY=700
im = Image.new("RGB", (imageSizeX, imageSizeY), "black")
draw = ImageDraw.Draw(im)
imageFormat = 'bmp'
imageName = 'tstlib.bmp'
axisGap = 20
axisSize = 256
lastPixelX = None
lastPixelY = None

def saveImage():
    im.save(imageName,  imageFormat)

def drawAxis():
    fillColor = (50, 50, 50)
    draw.line((axisGap, axisSize+axisGap, imageSizeX-axisGap, axisSize+axisGap), fill=fillColor)
    draw.line((axisGap, axisGap, axisGap, axisGap+axisSize), fill=fillColor)
    draw.line((axisGap,  axisGap-1,  imageSizeX-axisGap,   axisGap-1), fill=fillColor)
    draw.text((axisGap-19, axisGap-5), '255')
    draw.text((axisGap-8, axisSize+axisGap-5), '0')
    
def putAxisPixel(x,  y):
    #if (lastPixelX is not None) and (lastPixelY is not None):
    #if lastPixelX is not None:
    #    draw.line((lastPixelX,  pastPixelY,  x,  y),  (50, 0, 0))
    lastPixelX = x
    lastPixelY = y
    
    if y > (axisSize-1):
        draw.line((axisGap+1+x,  axisGap-2,  axisGap+1+x, axisGap-6))
    
    if y < 0:
        draw.line((axisGap+1+x,  axisSize+axisGap+2,  axisGap+1+x, axisSize+axisGap+6))
     
    im.putpixel((axisGap+1+x, axisGap+axisSize-1-y), (255,  0, 0))
  #   im.putpixel((20, 20), (0,  255, 0))
  #  im.putpixel((30, 40), (0,  0, 255))
