# -*- coding: utf-8 -*-
"""Convertor of files pdf to jpg"""

VERSION = '0.0.1'

"""
Created on Wed Mar  3 00:18:52 2021

@author: romain
"""

import os
import tempfile
from pdf2image import convert_from_path
from glob import glob  

def find_ext(dr, ext):
    return glob(os.path.join(dr,"*.{}".format(ext)))

def main():
    for filename in find_ext('PDF', 'pdf'):
        with tempfile.TemporaryDirectory() as path:
            images_from_path = convert_from_path(filename)
            base_filename = os.path.splitext(os.path.basename(filename))[0]
            save_dir = 'JPG'
            for idx, page in enumerate(images_from_path):
                page.save(os.path.join(save_dir, base_filename + '_' + str(idx) + '.jpg'), 'JPEG')

if __name__ == '__main__':
    main()
