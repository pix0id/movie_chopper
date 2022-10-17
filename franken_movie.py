from moviepy.editor import *
import os

clip_path = "movies/clips"

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


def concat_clips(clips_folder):
    clips = get_movies(movie_path=clip_path)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{clip_path}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list)
    final_clip.write_videofile("concat.mp4")

# F R A N K E N M O V I E
concat_clips(clips_folder=clip_path)