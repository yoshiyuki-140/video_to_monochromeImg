#coding:utf-8
# Author : Yoshiyuki Kurose

from config import *
import os
import cv2


class Converter:
    def colorToGrayscale():
        for filename in os.listdir(destDirPath):
            img = cv2.imread(os.path.join(destDirPath, filename))
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            os.makedirs(os.path.join(destDirPath, grayImgDirName), exist_ok=True)
            cv2.imwrite(os.path.join(destDirPath,), img_gray)


    def videoToFrames():
        cap = cv2.VideoCapture(videoDataPath)

        if not cap.isOpened():
            return

        os.makedirs(destDirPath, exist_ok=True)
        base_path = os.path.join(destDirPath, basename)

        digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

        n = 0

        while True:
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(f'{base_path}_{str(n).zfill(digit)}.{ext}', frame)
                n += 1
            else:
                return

