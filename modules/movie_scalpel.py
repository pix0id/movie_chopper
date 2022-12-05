from moviepy.editor import *
import os
import csv
from modules.settings import *
from modules.utils import get_video_files, dir_check, get_file_extension

class Movie_Scalpel():
    def __init__(self, csv_file) -> None:
        self.csv_file = csv_file

    def open_csv(self):
        with open(self.csv_file, "r", newline=",") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
