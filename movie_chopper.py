from moviepy.editor import *
import os

# Directories and files
video_path = "movies/"
clip_path = "movies/clips/"
movies = []

# time/name logic variables
# TODO: make clip length flexible with script flags
minute = 60
clip_length = 5 #length of clip in minutes
clip_length_seconds = minute * clip_length
count = 1

# get all files listed in /movies/
for video in os.listdir(video_path):
    if os.path.isfile(os.path.join(video_path, video)):
        movies.append(video)
        
# Loop through all the movies in the movies folder
for index, movie in enumerate(movies):
    video = VideoFileClip(f"{video_path}{movie}")
    time_tracker = 0
    movie_length = video.duration

    print(f"Now chopping {movie} ({index + 1}/{len(movies)})")

    while time_tracker < movie_length:
        remaining_time = movie_length - time_tracker
        # If statement here to prevent errors if clip will be shorter than the remaining time in the movie.
        # Won't matter really since 99% of the time this will prevent one clip that is 100% credits.
        # Marvel post-credit scene fans in shambles.
        if remaining_time > clip_length_seconds:
            clip = video.subclip(time_tracker, clip_length_seconds*count)
            clip.write_videofile(f"{clip_path}{count}.mp4",codec="libx264")

        count += 1
        time_tracker += clip_length_seconds

    clip.close()
