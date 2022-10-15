from moviepy.editor import *
import os
import argparse
import random

# Directories and files
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", dest="length", default="1", help="Clip duration in minutes")
parser.add_argument("-n", "--num", dest="number_of_clips", default="1", help="Number of clips to create")
parser.add_argument("-p", "--path", dest="path", default="movies/", help="Movie Folder Path (Only have videos, no subdirectoies.")
parser.add_argument("-c", "--clips", dest="clips_folder", default="movies/clips/", help="Folder for clip output")

args = parser.args()

class MovieChop:
    def __init__(self, length, number_of_clips, video_path, clip_path,):
        self.length = int(length)
        self.number_of_clips = int(number_of_clips)
        self.video_path = video_path
        self.clip_path = clip_path
        self.length_in_seconds = int(60*length)
        self.movies = []
        self.touched_movies = []
        self.count = 0

    def get_movies(self):
        '''
            Generates list of videos from specified video path.
            Does not work with nested directories.
            Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
            TODO:
                - Make work with nested directories
                - specify accepted video types
        '''
        for file in os.listdir(self.video_path):
            if os.path.isfile(os.path.join(self.video_path, file)):
                self.movies.append(video)

    def set_clip_buffer(self, video_length, clip_length):
        '''
            Creates buffer space at end of video, so you cannot get a clip shorter than the specified amount.
        '''
        return video_length - clip_length

    def clip_random_movie(self):
        '''
            Chooses a random file from the list of movies
            Checks if the movie has been "touched" recently 
            (Meaning other movies haven't been "touched" recently.)
            Clips chosen movie and writes file
        '''
        current_movie_name = random.choice(self.movies)
        movie_length = current_movie.duration
        clip_buffer = self.set_clip_buffer(movie_length, self.length_in_seconds)

        if current_movie not in self.touched_movies:
            self.count += 1
            current_movie = VideoFileClip(f"{self.video_path}{current_movie_name}")
            start_index = random.randint(0, clip_buffer)

            clip = video.subclip(start_index, self.length_in_seconds)
            clip.write_videofile(f"{self.clip_path}{self.count + 1}.mp4",codec="libx264")

            clip.close()
        else:
            """Sort lists and check if they're the same. If so, empty touched_movies and start chopping again"""
            self.movies.sort()
            self.touched_movies.sort()

            if self.movies == self.touched_movies:
                self.touched_movies = []



# video_path = "movies/"
# clip_path = f"movies/clips/"
# movies = []

# # time/name logic variables
# clip_length_minutes = args.length
# clip_length_seconds = 60 * clip_length_minutes
# count = 1
# # TODO: Refactor.

# # TODO: Only create the number of clips specified in args.number_of_clips.
# # TODO: After clipping is complete, merge all videos together into one file.
# # TODO: Remove audio and replace it with ~*~V I B E S~*~

# # # get all files listed in /movies/
# # for video in os.listdir(video_path):
# #     if os.path.isfile(os.path.join(video_path, video)):
# #         movies.append(video)
        
# # Loop through all the movies in the movies folder
# for index, movie in enumerate(movies):
#     video = VideoFileClip(f"{video_path}{movie}")
#     time_tracker = 0
#     movie_length = video.duration

#     print(f"Now chopping {movie} ({index + 1}/{len(movies)})")

#     while time_tracker < movie_length:
#         remaining_time = movie_length - time_tracker
#         # If statement here to prevent errors if clip will be shorter than the remaining time in the movie.
#         # Won't matter really since 99% of the time this will prevent one clip that is 100% credits.
#         # Marvel post-credit scene fans in shambles.
#         if remaining_time > clip_length_seconds:
#             clip = video.subclip(time_tracker, clip_length_seconds*count)
#             clip.write_videofile(f"{clip_path}{count}.mp4",codec="libx264")
#             clip.close()

#         count += 1
#         time_tracker += clip_length_seconds