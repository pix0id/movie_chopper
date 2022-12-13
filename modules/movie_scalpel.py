from moviepy.editor import *
import os
import csv
from settings import *

try:
    from modules.settings import *
    from modules.utils import clip_cleanup, audio_cleanup, get_video_files
except ModuleNotFoundError:
    from settings import *
    from utils import clip_cleanup, audio_cleanup, get_video_files

class Movie_Scalpel():

    def __init__(self, csv_file: str) -> None:
        self.csv_file = csv_file
        self.line_count = 0
        self.current_video = ""
        self.clip_times = {}

    def movie_times(self):
        with open(self.csv_file, mode="r", newline="") as csvfile:
            clip_times = csv.reader(csvfile, delimiter=",")

            for row in clip_times:
                if self.line_count > 0:
                    if len(row[0]) > 0:
                        self.current_video = row[0]
                        self.clip_times[self.current_video] = []

                    self.clip_times[self.current_video].append((row[1], row[2]))

                self.line_count += 1
                    
                
        
        print(self.clip_times)


if __name__ == "__main__":
    ms = Movie_Scalpel("movies.csv")

    ms.movie_times()