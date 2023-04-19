from config import *
# import video_to_colorFrame as vtc

def save_all_frames(video_file_path, distDir_path, basename, ext='jpg'):
    import os
    import cv2
    cap = cv2.VideoCapture(video_file_path)

    if not cap.isOpened():
        return

    os.makedirs(distDir_path, exist_ok=True)
    base_path = os.path.join(distDir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'{base_path}_{str(n).zfill(digit)}.{ext}', frame)
            n += 1
        else:
            return

if __name__ == "__main__":
    basename = "badapple"
    save_all_frames(videoDataPath, destDirPath, basename)
