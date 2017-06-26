#-*- coding: UTF-8 -*-

#import sys
import os
import getimage
import roughclassification
import fineclassifycertificate
import fineclassifydocument
import ocrabbyy
import wordsfilter



#   User: duanwei
#   Date: 2017/6/19
#   version number: 0.1


def Main(imagePath):
    roughNum = 0
    fineCertificateNum = 0
    fineDocumentNum = 0
    imageFile = getimage.getImage(imagePath)
#    imageFile = imagePretreatmentGuang(imageFile)
#    imageFile = imagePretreatment(imageFile)
#     classifiedInformation = roughclassification.roughClassification(imageFile)
    classifiedInformation = '文书'
    if (classifiedInformation == '证件'):
        deepClassifiedInformation, fineCertificateNum = fineclassifycertificate.fineClassifyCertificate(imageFile, fineCertificateNum)
    elif (classifiedInformation == '文书'):
        deepClassifiedInformation, fineDocumentNum = fineclassifydocument.fineClassifyDocument(imageFile, fineDocumentNum)
        finalClassifiedInformation = wordsfilter.wordsFilter(ocrText)
    elif (classifiedInformation == '其他'):
        print('文件分类失败，它的路径为' + imagePath)
        roughNum = roughNum + 1

if __name__ == "__main__":
    filePath = r'/Users/dw8855/Desktop/SaveImage'
    file = os.listdir(filePath)[1:]
    for fileName in file:
        imageName = os.listdir(filePath + '/' + fileName)
        for image in imageName:
            imagePath = filePath + '/' + fileName + '/' + image
            Main(imagePath)



