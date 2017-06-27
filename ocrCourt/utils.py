# -*- coding: UTF-8 -*-

import os
from PIL import Image
import numpy
import roughclassification


def isRed(color):
    if color[0] > 180:
        return True
    else:
        return False


def isBlack(color):
    if sum(color) <= 250:
        return True
    else:
        return False


def binarition(imageFile, threshold):
    Bimage = imageFile
    image = numpy.array(imageFile)
    height = len(image)
    width = len(image[0])
    for i in range(width):
        for j in range(height):
            r, g, b = roughclassification.getRGB(image[j, i])
            r = r * 1.1 + 30
            g = g * 1.1 + 30
            b = b * 1.1 + 30
            if r + g + b < threshold:
                Bimage.putpixel((i, j), (255, 255, 255))
            else:
                Bimage.putpixel((i, j), (0, 0, 0))
    return Bimage


def tohisto(imageFile, type):
    image = numpy.array(imageFile)
    height = len(image)
    width = len(image[0])
    histo = numpy.zeros(height)
    if type == 'row':
        for i in range(height):
            for j in range(width):
                if isBlack(image[i, j]):
                    histo[i] = histo[i] + 1
    elif type == 'col':
        for j in range(width):
            for i in range(height):
                if isBlack(image[i, j]):
                    histo[j] = histo[j] + 1
    return int(histo)


if __name__ == '__main__':
    filePath = r'/Users/dw8855/Desktop/SaveImage'
    file = os.listdir(filePath)[1:]
    imageName = os.listdir(filePath + '/' + file[0])
    imagePath = filePath + '/' + file[0] + '/' + imageName[0]
    imageFile = Image.open(imagePath)
    fineDocumentNum = 0
    type = 'row'
    print(tohisto(imageFile, type))
