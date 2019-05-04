from PIL import Image
import numpy as np

def MakeGray(img):
    """Returns a grayscale copy of image in img"""

    w, h = img.size

    new = Image.new("RGB", (w,h))
    output = new.load()

    pixels = np.array(img)
    
    for x in range(w):
        for y in range(h):
            r = pixels[y, x, 0] * 0.42
            g = pixels[y, x, 1] * 0.71
            b = pixels[y, x, 2] * 0.07
            newCol = int((r + g + b) / 3)
            
            output[x, y] = (newCol, newCol, newCol)

    return new

def MakeGrayVectorized(img):
    """Returns a grayscale copy of image in img"""

    w, h = img.size

    new = Image.new("RGB", (w,h))
    output = new.load()

    pixels = np.array(img)
    
    intermidiary = np.sum(np.array(img), 2) / 3
    
    for x in range(w):
        for y in range(h):
            newCol = int(intermidiary[y, x])
            output[x,y] = (newCol, newCol, newCol)

    return new

def SimpleBlur(img, blurSize = 1):
    """Returns a blurred copy of image in img"""

    w, h = img.size
    if blurSize < 1: blurSize = 1

    new = Image.new("RGB", (w,h))
    output = new.load()
    
    pixels = np.array(img)

    for x in range(0, w):
        for y in range(0, h):
            r = 0
            g = 0
            b = 0
            p = 0
            for xx in range(-blurSize, blurSize + 1):
                for yy in range(-blurSize, blurSize + 1):
                    if x + xx < 0 or x + xx >= w or y + yy < 0 or y + yy >= h: continue
                    else:
                        #pixel = img.getpixel((x + xx, y + yy))
                        r += pixels[y + yy, x + xx, 0]#pixel[0]
                        g += pixels[y + yy, x + xx, 1]#pixel[1]
                        b += pixels[y + yy, x + xx, 2]#pixel[2]
                        p += 1

            if p == 0: p = 1
            newR = r / p
            newG = g / p
            newB = b / p
            
            output[x, y] = (int(newR), int(newG), int(newB))

    return new

def Pixelate(img, pixelSize = 1):
    """Returns a pixelated copy of image in img"""

    w, h = img.size
    if pixelSize < 1: pixelSize = 1

    new = Image.new("RGB", (w,h))
    output = new.load()
    
    widthRemainder = w % pixelSize
    heightRemainder = h % pixelSize

    pixels = np.array(img)

    for x in range(pixelSize, w + widthRemainder, pixelSize * 2):
        for y in range(pixelSize, h + heightRemainder, pixelSize * 2):
            r = 0
            g = 0
            b = 0
            neighbors = []
            for xx in range(-pixelSize, pixelSize + 1):
                for yy in range(-pixelSize, pixelSize + 1):
                    if x + xx < 0 or x + xx >= w or y + yy < 0 or y + yy >= h: continue
                    else:
                        #pixel = img.getpixel((x + xx, y + yy))
                        r += pixels[y + yy, x + xx, 0]#pixel[0]
                        g += pixels[y + yy, x + xx, 1]#pixel[1]
                        b += pixels[y + yy, x + xx, 2]#pixel[2]
                        neighbors.append((y + yy, x + xx))
            divideBy = len(neighbors)
            if divideBy == 0: divideBy = 1
            newR = r / divideBy
            newG = g / divideBy
            newB = b / divideBy

            for i in neighbors:
                output[i[1], i[0]] = (int(newR), int(newG), int(newB))

    return new

def PixelateVariant(img, pixelSize = 1):
    """Returns a pixelated copy of image in img"""

    w, h = img.size
    if pixelSize < 1: pixelSize = 1

    new = Image.new("RGB", (w,h))
    output = new.load()
    
    widthRemainder = w % pixelSize
    heightRemainder = h % pixelSize

    pixels = np.array(img)

    for x in range(pixelSize, w + widthRemainder, pixelSize * 2):
        for y in range(pixelSize, h + heightRemainder, pixelSize * 2):
            r, g, b = img.getpixel((x, y))
            neighbors = []
            for xx in range(-pixelSize, pixelSize + 1):
                for yy in range(-pixelSize, pixelSize + 1):
                    if x + xx < 0 or x + xx >= w or y + yy < 0 or y + yy >= h: continue
                    else:
                        neighbors.append((y + yy, x + xx))
            
            for i in neighbors:
                output[i[1], i[0]] = (int(r), int(g), int(b))

    return new

def RGBSwap(img):
    """Swaps R->G->B->R and returns a copy of image in img"""

    w, h = img.size

    new = Image.new("RGB", (w,h))
    output = new.load()

    pixels = np.array(img)

    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pixels[y, x]
            output[x, y] = (b, r, g)

    return new

def Negate(img):
    """Returns a negative copy of image in img"""

    w, h = img.size

    new = Image.new("RGB", (w,h))
    output = new.load()

    pixels = np.array(img)

    for x in range(0, w):
        for y in range(0, h):
            r, g, b = pixels[y, x]
            output[x, y] = (255 - r, 255 - g, 255 - b)

    return new

def EdgeDetect(img, threshHold = 0):
    """Returns the edges of the image in img"""

    w, h = img.size

    new = Image.new("RGB", (w, h))
    output = new.load()

    pixels = np.array(img)
    xMatrix = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    yMatrix = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
    
    for x in range(0, w):
        for y in range(0, h):
            neighborArr = np.sum(pixels[max(0, y - 1):min(y + 2, h), max(0, x - 1):min(x + 2, w)], 2)
                
            if neighborArr.shape != (3,3):
                neighborArr = np.resize(neighborArr, (3,3))
                    
            Gx = neighborArr * yMatrix
            Gy = neighborArr * xMatrix
                
            dG = int((abs(np.sum(Gx, None)) + abs(np.sum(Gy, None))) / 3)

            if dG > threshHold:
                output[x, y] = ((dG, dG, dG))
            else: output[x, y] = ((0, 0, 0))

    return new

