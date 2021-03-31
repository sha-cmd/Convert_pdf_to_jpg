# -*- coding: utf-8 -*-
"""Convertor of files pdf to jpg or jpg to pdf"""

VERSION = '0.0.1'

"""
Created on Wed Mar  3 00:18:52 2021

@author: romain
"""

SAVE_DIRECTORY = 'OUT'

import os
import tempfile
import img2pdf

from pdf2image import convert_from_path
from glob import glob

def find_ext(dr, ext):
    return glob(os.path.join(dr, "*.{}".format(ext)))

def img_to_pdf(filename):
    img_list: list = find_ext('JPG', 'jpg')
    print(img_list)
    save_dir = SAVE_DIRECTORY
    with open(os.path.join(save_dir, filename + '.pdf'), "wb") as f:
        f.write(img2pdf.convert(img_list))
        f.close()

def pdf_to_img():
    for filename in find_ext('PDF', 'pdf'):
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(filename)
            base_filename = os.path.splitext(os.path.basename(filename))[0]
            save_dir = SAVE_DIRECTORY
            for idx, page in enumerate(images_from_path):
                page.save(os.path.join(save_dir, base_filename + '_' + str(idx) + '.jpg'), 'JPEG')

def main():
    img_to_pdf('name')
    #pdf_to_img()
if __name__ == '__main__':
    main()
