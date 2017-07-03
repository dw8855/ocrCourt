#-*- coding: UTF-8 -*-

from PIL import Image
import os
import platform
from ctypes import *

#只处理window以及linux系统的32位以及64位



def imagePretreatmentGuang(imagePath, saveImagePath):
    if platform.system() == 'Linux':
        if platform.machine() == 'x86_64':
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
        else:
            pass
    elif platform.system() == 'Windows':
        if platform.machine() == 'x86_64':
            pass
        else:
            pass

