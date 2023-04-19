import video_to_colorFrame


if __name__ == "__main__":

    video_path = "D:/Downloads/Touhou - Bad Apple.flv"
    dist_path = "C:/Users/moyas/Documents/programsForMe/python/apps/badapple/color_frames"

    video_to_colorFrame.save_all_frames(video_path, dist_path, "badapple")
