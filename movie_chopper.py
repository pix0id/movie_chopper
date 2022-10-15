# FIXME: refactor args. File was removed and added to app. Set function arguments if needed.


from moviepy.editor import *
import os
import random


def get_movies(movies):
        # FIXME: Only return video files! Check moviepy documentation for list of file types.
    '''
        Generates list of videos from specified video path.
        Does not work with nested directories.
        Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
        TODO:
            - Make work with nested directories
            - specify accepted video types
    '''
    movies_list = []

    for file in os.listdir(movies):
        if os.path.isfile(os.path.join(movies, file)):
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
    current_movie_name = random.choice(movies)
    
    if current_movie_name not in touched_movies:
        count += 1

        current_movie = VideoFileClip(f"{args.video_path}{current_movie_name}")
        movie_length = current_movie.duration
        start_index = random.randint(0, set_clip_buffer(movie_length, length_in_seconds))

        clip = current_movie.subclip(start_index, length_in_seconds)
        clip.write_videofile(f"{args.clip_path}{count + 1}.mp4",codec="libx264")

        clip.close()
    else:
        """Sort lists and check if they're the same. If so, empty touched_movies and start chopping again"""
        movies.sort()
        touched_movies.sort()

        if movies == touched_movies:
            touched_movies = []
