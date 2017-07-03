# -*- coding: UTF-8 -*-

# import sys
import os
import roughclassification
import fineclassifycertificate
import fineclassifydocument
import platform
import imagePretreatmentGuang

#   User: duanwei
#   Date: 2017/6/19
#   version number: 0.1


def Main(imagePath, saveImagePath, type):
    roughNum = 0
    fineCertificateNum = 0
    fineDocumentNum = 0
    imageFile = imagePretreatmentGuang.imagePretreatmentGuang(imagePath, saveImagePath)
    #    imageFile = imagePretreatment(imageFile)
    #     classifiedInformation = roughclassification.roughClassification(imageFile)
    classifiedInformation = '文书'
    if classifiedInformation == '证件':
        deepClassifiedInformation = fineclassifycertificate.fineClassifyCertificate(imageFile)
        if deepClassifiedInformation:
            fineCertificateNum = fineCertificateNum + 1
        if classifiedInformation == '其它':
            print('文件分类失败，它的路径为' + imagePath)
            roughNum = roughNum + 1
    elif classifiedInformation == '文书':
        deepClassifiedInformation = fineclassifydocument.fineClassifyDocument(imageFile, type)
        if deepClassifiedInformation:
            fineDocumentNum = fineDocumentNum + 1
        if classifiedInformation == '其它':
            print('文件分类失败，它的路径为' + imagePath)
            roughNum = roughNum + 1
    print(fineCertificateNum, fineDocumentNum, roughNum)


if __name__ == "__main__":
    filePath = r'/Users/dw8855/Desktop/SaveImage'
    saveImagePath = r'/Users/dw8855/Desktop/SaveImage!'
    file = os.listdir(filePath)[1:]
    type = 'Tessesract'
    for fileName in file:
        imageName = os.listdir(filePath + '/' + fileName)
        for image in imageName:
            imagePath = filePath + '/' + fileName + '/' + image
            Main(imagePath, saveImagePath, type)
