# -*- coding: UTF-8 -*-

from PIL import Image
import os
import platform
from ctypes import *
import subprocess


# 只处理window以及linux系统的32位以及64位



def imagePretreatmentGuang(imagePath, saveImagePath):
    if platform.system() == 'Linux':
        ocr = cdll.LoadLibrary('./libgrgPageAnalysisV3.so')
        pageAnalysis = ocr.grgPageAnalysis
        arg0 = imagePath
        arg1 = saveImagePath + '/' + imagePath.split('/')[-1]
        arg2 = '123'
        pageAnalysis(arg0, arg1, arg2)
        imageFile = Image.open(arg1)
        return imageFile
        ''' 
            直接调用.so文件比用几次io接口好很多


            arg0 = imagePath
            arg1 = saveImagePath + '/' +imagePath.split('/')[-1]
            arg2 = 123
            os.system('./pageAnalysis ' + arg0 + ' ' + arg1 + ' ' + arg2)
            imageFile = Image.open(arg1)
            return imageFile
        '''
    elif platform.system() == 'Windows':
        arg0 = imagePath
        arg1 = saveImagePath + os.path.sep + imagePath.split(os.path.sep)[-1]
        arg2 = '123'
        exePath = os.path.join('D:', os.sep, 'release')
        exePath = os.path.join(exePath, 'pageAnalysis.exe')
        subprocess.call([exePath, arg0, arg1, arg2])
        # pageAnalysis = r'C:/Users/Administrator/Desktop/release/pageAnalysis.exe ' + arg0 + ' ' + arg1 + ' ' + arg2
        # key = os.system('C:/Users/Administrator/Desktop/release/pageAnalysis.exe ' + arg0 + ' ' + arg1 + ' ' + arg2)
        imageFile = Image.open(arg1)
        return imageFile


if __name__ == '__main__':
    a = platform.system()
    imagePath = os.path.join(os.path.join('D:', os.path.sep), 'page_1.jpg')
    saveImagePath = os.path.join(os.path.join('D:', os.path.sep), 'down')
    image = imagePretreatmentGuang(imagePath, saveImagePath)
    # print(image)