#coding:utf-8
# Autor : Yoshiyuki Kurose

import unittest
from ..convert_methods import Converter
import os
from ..config import *

class ConverterTest(unittest.TestCase):
    def test_sourceFileExist(self):
        for filename in os.listdir(destDirPath):
            self.assertTrue(os.path.isfile(
                os.path.join(destDirPath, filename)))

    def test_colorToGrayScale_method():
        pass
