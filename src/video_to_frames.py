# coding:utf-8
import cv2
import os
from config import *


def convert():
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


if __name__ == '__main__':
    convert()
