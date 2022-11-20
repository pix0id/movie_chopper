import os
import movie_chopper as mc
import franken_movie as fm
from settings import *

count = 0

# get movies list
movies = mc.get_video_files(path=VIDEO_PATH)

mc.clip_dir_check()

# Create clips
while count <= NUMBER_OF_CLIPS:
    count += 1
    mc.clip_random_movie(movies)
    
# F R A N K E N M O V I E
fm.concat_clips(video_folder=CLIP_PATH)