# -*- coding: UTF-8 -*-
import pytesseract
from PIL import Image


def Ocr(imageFile, type):
    if type == 'Abbyy':
        pass
    elif type == 'Tesseract':
        try:
            txt = pytesseract.image_to_string(imageFile)
        except():
            tessdata_dir_config = '--tessdata-dir "<replace_with_your_tessdata_dir_path>"'
            pytesseract.image_to_string(imageFile, lang='chi_sim', config=tessdata_dir_config)
        return txt

