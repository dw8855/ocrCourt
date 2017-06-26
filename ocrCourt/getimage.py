#-*- coding: UTF-8 -*-
from PIL import Image

def getImage(imagePath):
    imageFile = Image.open(imagePath)
    return imageFile
