from PIL import Image,  ImageDraw

imageSizeX=1000
imageSizeY=700
im = Image.new("RGB", (imageSizeX, imageSizeY), "black")
draw = ImageDraw.Draw(im)
imageFormat = 'PNG'
imageName = 'tstlib.png'
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#
class Axis:
    def __init__(self, size, whereY):
        self.axisGap = 20 #Free spaces by x Axis
        self.axisPosition = whereY #Where to draw axis by y Axis
        self.axisSize = size #Sixe of axis
        
        fillColor = (50, 50, 50)
        draw.line((self.axisGap, self.axisSize+whereY, imageSizeX-self.axisGap, self.axisSize+whereY), fill=fillColor) #DownLine
        draw.line((self.axisGap, whereY, self.axisGap, whereY+self.axisSize), fill=fillColor)  #SideLine
        draw.line((self.axisGap,  whereY-1,  imageSizeX-self.axisGap,   whereY-1), fill=fillColor) #UpLine
        draw.text((self.axisGap-19, whereY-5), str(self.axisSize-1))
        draw.text((self.axisGap-8, self.axisSize+whereY-5), '0')

    def realCoordX(self, x):
        x = self.axisGap+1+x
        return(x)
    
    def realCoordY(self, y):
        y = self.axisPosition+self.axisSize-1-y
        if y < 0:
            y = 0
        return(y)
        
    def realCoords(self, coord):
        x = self.realCoordX(coord[0])
        y = self.realCoordY(coord[1])
        if y < 0:
            y = 0
        return(x, y)
    
    def drawBottomWarning(self, x):
        x = self.realCoordX(x)
        draw.line((x,  self.axisSize+self.axisPosition+2, x, self.axisSize+self.axisPosition+6))
        
    def drawTopWarning(self, x):
        x = self.realCoordX(x)
        draw.line((x,  self.axisPosition-2,  x, self.axisPosition-6))
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#
class Graph:
    def __init__(self,  axis, color):
        self.color = color
        self.lastPixelCoord = None;
        self.jointColorLower = 4
        self.axis = axis
        self.currXPos = 0

    def joinPixels(self,  coord):
        #coord = self.realCoords(coord)
        coord = self.axis.realCoords(coord)
        #lastCoord = self.realCoords(self.lastPixelCoord)
        lastCoord = self.axis.realCoords(self.lastPixelCoord)
        r = self.color[0] / self.jointColorLower
        g = self.color[1] / self.jointColorLower
        b = self.color[2] / self.jointColorLower
        draw.line((lastCoord, coord),  (r, g, b))
        im.putpixel(lastCoord, self.color)
        
    def putPixel (self,  y):
        self.putPixelCoord((self.currXPos, y))
        self.currXPos = self.currXPos + 1
        
    def putPixelCoord (self, coord ):
        realCoord = self.axis.realCoords(coord)
        
        #Adding some small lines, if coords are wrong
        if coord[1] > (self.axis.axisSize-1):
            self.axis.drawTopWarning(coord[0])
            
        if coord[1] < 0:
            self.axis.drawBottomWarning(coord[0])

        if self.lastPixelCoord is not None:
            self.joinPixels(coord)
        
        im.putpixel(realCoord, self.color)
        self.lastPixelCoord = coord
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#
def saveImage():
    im.save(imageName,  imageFormat)


