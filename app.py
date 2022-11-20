import os
import movie_chopper as mc
import franken_movie as fm
from settings import *
from utils import dir_check

count = 0
movies = mc.get_video_files(path=VIDEO_PATH)

print("Creating required directories....")
dir_check(CLIP_PATH)
dir_check(CONCAT_PATH)

while count <= NUMBER_OF_CLIPS:
    count += 1
    mc.clip_random_movie(movies)

fm.concat_clips(video_folder=CLIP_PATH)