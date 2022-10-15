from moviepy.editor import *
import os
import argparse

# Directories and files
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", dest="length", default="1", help="Clip duration in minutes")
parser.add_argument("-n", "--num", dest="number_of_clips", default="1", help="Number of clips to create")
parser.add_argument("-p", "--path", dest="path", default="movies/", help="Movie Folder Path (Only have videos, no subdirectoies.")
parser.add_argument("-c", "--clips", dest="clips_folder", default="movies/clips/", help="Folder for clip output")

args = parser.args()

video_path = "movies/"
clip_path = f"movies/clips/"
movies = []

# time/name logic variables
clip_length_minutes = args.length
clip_length_seconds = 60 * clip_length_minutes
count = 1
# TODO: Clip videos at random timestamps instead of splitting up like it is now.
# TODO: Choose which video to clip randomly.
# TODO: Do not clip from same video until all other videos have been clipped from.
# TODO: Only create the number of clips specified in args.number_of_clips.
# TODO: After clipping is complete, merge all videos together into one file.
# TODO: Remove audio and replace it with ~*~V I B E S~*~

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
