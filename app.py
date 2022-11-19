import os
import movie_chopper as mc
import franken_movie as fm
from settings import *

# TODO: Project wide - look into type safety and add types to all scripts.
# TODO: Project wide - try/except blocks and error handling, lol.
# TODO: Project wide - Add timing functinality to output the time it takes to make the videos.
# TODO: Project wide - OOP?
# TODO: Project wide - Multithreading/Multiprocessing???
# TODO: Ask for concat name before clipping starts.

count = 0

# get movies list
movies = mc.get_video_files(path=VIDEO_PATH)

mc.clip_dir_check()

# Create clips
while count <= NUMBER_OF_CLIPS:
    count += 1
    mc.clip_random_movie(movies)
    
#TODO: Set default name OR name given above.
# F R A N K E N M O V I E
fm.concat_clips(video_folder=CLIP_PATH)