# coding:utf-8

from config import *
import cv2
import os


def color_to_grayscale():
    for filename in os.listdir(destDirPath):
        img = cv2.imread(os.path.join(destDirPath, filename))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        os.makedirs(os.path.join(destDirPath, grayImgDirName), exist_ok=True)
        cv2.imwrite(os.path.join(destDirPath,), img_gray)


if __name__ == '__main__':
    color_to_grayscale()
