from moviepy.editor import *
import os
import csv
from movie_chopper import Movie_chopper
try:
    from modules.settings import *
    from modules.utils import dir_check, file_name_text
except ModuleNotFoundError:
    from settings import *
    from utils import dir_check, file_name_text

class Movie_Scalpel():

    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file
        self.line_count = 0
        self.current_video = ""
        self.clip_times = {}

    def video_times(self):
        with open(self.csv_file, mode="r", newline="") as csvfile:
            clips = csv.reader(csvfile, delimiter=",")

            for row in clips:
                if self.line_count > 0:
                    if len(row[0]) > 0:
                        self.current_video = row[0]
                        self.clip_times[self.current_video] = []

                    self.clip_times[self.current_video].append((row[1], row[2]))

                self.line_count += 1

    def get_video_times(self) -> dict:
        return self.clip_times


if __name__ == "__main__":
    scalpel = Movie_Scalpel(f"{root_dir}/movies.csv")
    mc = Movie_chopper(video_path)

    scalpel.video_times()
    times = scalpel.get_video_times()

    for video, timestamps in times.items():
        print(f"VIDEO: {video}")
        curr_video = VideoFileClip(f"{video_path}{video}")
        dir_check(f"{clip_path}{file_name_text(video)[0]}")

        for timestamp in timestamps:
            mc.custom_clip(video_file=curr_video,timestamp=timestamp)
        
        curr_video.close()
