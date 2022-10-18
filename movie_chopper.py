from moviepy.editor import *
import os
import math
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", dest="length", default="1", help="Clip duration in whole minutes")
parser.add_argument("-n", "--num", dest="number_of_clips", default="1", help="Number of clips to create")
parser.add_argument("-p", "--path", dest="movie_path", default="movies/", help="Movie Folder Path (Only have videos, no subdirectoies.")
parser.add_argument("-c", "--clips", dest="clip_path", default="movies/clips/", help="Folder for clip output")

args = parser.parse_args()

# Path variables
movie_path = args.movie_path
clip_path = args.clip_path

# Timing variables
length_in_seconds = 60*int(args.length)

# Logic variables
number_of_clips = int(args.number_of_clips)
touched_movies = []
count = 0

def get_movies(movie_path):
        # FIXME: Only return video files! Check moviepy documentation for list of file types accepted.
        # TODO: name everything more "general" can be confusing since it's being used for clips and movies.
    '''
        Generates list of videos from specified video path.
        Does not work with nested directories.
        Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
        TODO:
            - Make work with nested directories
            - specify accepted video types
    '''
    movies_list = []

    for file in os.listdir(movie_path):
        if os.path.isfile(os.path.join(movie_path, file)):
            movies_list.append(file)
    
    return movies_list


def set_clip_buffer(video_length, clip_length):
    '''
        Creates buffer space at end of video, so you cannot get a clip shorter than the specified amount.
    '''
    return video_length - clip_length


def clip_random_movie(movies):
    '''
        Chooses a random file from the list of movies
        Checks if the movie has been "touched" recently 
        (Meaning other movies haven't been "touched" recently.)
        Clips chosen movie and writes file
    '''

    global touched_movies
    global count
    current_movie_name = random.choice(movies)
    
    if current_movie_name not in touched_movies:
        count += 1
        touched_movies.append(current_movie_name)

        current_movie = VideoFileClip(f"{movie_path}{current_movie_name}")
        movie_length = math.floor(current_movie.duration)
        
        start_index = random.randint(0, set_clip_buffer(movie_length, length_in_seconds))
        
        clip = current_movie.subclip(start_index, start_index+length_in_seconds)
        clip.write_videofile(f"{clip_path}{count}.mp4",codec="libx264")

        clip.close()
    else:
        '''
        Sort lists and check if they're the same. 
        If so, empty touched_movies and start chopping again
        '''
        movies.sort()
        touched_movies.sort()

        if movies == touched_movies:
            touched_movies = []


def concat_clips(clips_folder):
    clips = get_movies(movie_path=clip_path)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{clip_path}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list, method="compose")
    final_clip.write_videofile("concat.mp4")


# Actual execution

# get movies list
movies = get_movies(movie_path=movie_path)

# Create clips
while count < number_of_clips:
    clip_random_movie(movies)

# F R A N K E N M O V I E
concat_clips(clips_folder=clip_path)