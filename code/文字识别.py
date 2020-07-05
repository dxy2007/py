# coding:utf8
import os
from PIL import Image
import pytesseract

language = None
file = input('请输入图片路径:')
lang = input('请输入识别的语言 en/cn :')
if lang == 'cn':
    language = 'chi_sim'
if lang == 'en':
    language = 'eng'

if os.path.exists(file):
    image = Image.open(file)

    text = pytesseract.image_to_string(image, language)
    print(text)
else:
    print('你输入的图片路径不存在')
