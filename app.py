import os
import movie_chopper as mc
import franken_movie as fm
import settings

count = 0

# get movies list
movies = mc.get_video_files(video_path=settings.video_path)


# Create clips
while count < settings.number_of_clips:
    mc.clip_random_movie(movies)


# F R A N K E N M O V I E
fm.concat_clips(clips_folder=settings.clip_path)