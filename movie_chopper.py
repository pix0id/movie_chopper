from moviepy.editor import *
import os
import math
import random
from settings import *


# Logic variables
touched_movies = []
count = 0

# TODO: combine get_file_extension and get_name_text, they do basically the same damn thing.
# TODO: Or, combine get_file extension and verify_file_extension.. Strings = True in python so it wouldn't be too far fetched..


def get_file_extension(file):
    split_name = file.split('.')
    ext = split_name[-1]
    return ext

def get_video_files(path):
    '''
        Generates list of videos from specified video path.
        Does not work with nested directories.
        Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
    '''
    paths=[]
    directories=[]

    for root, dirs, files in os.walk(path):
        for _dir in dirs:
            directories.append(_dir)

        for _file in files:
            filetype = get_file_extension(_file)
            if filetype in FILE_TYPES:
                paths.append(os.path.join(root,_file))

    return paths

def verify_extension(ext):
    '''
    Verify if file extension is in the FILE_TYPES list. Modify in settings.py
    '''
    if ext in FILE_TYPES:
        return True

    return False


def set_clip_buffer(video_length, clip_length):
    '''
        Creates buffer space at end of video, so you cannot get a clip shorter than the specified amount.
    '''
    return video_length - clip_length

def get_name_text(file):
    file_name = file.split('.')
    video_name = file_name[0].split('_')
    return video_name

def generate_title(text):
    return TextClip(txt=text, fontsize=30, color="white", stroke_color="black", stroke_width=12)

def clip_dir_check():
    '''
        If the CLIP_PATH directory does not exist, create it.
    '''
    if not os.path.isdir(CLIP_PATH):
        os.mkdir(CLIP_PATH)

def clip_random_movie(movies):
    '''
        Chooses a random file from the list of movies
        Checks if the movie has been "touched" recently 
        (Meaning other movies haven't been "touched" recently.)
        Clips chosen movie and writes file
    '''

    global touched_movies
    global count
    current_movie_file = random.choice(movies)
    movie_name = get_name_text(current_movie_file)
    
    if current_movie_file not in touched_movies:
        count += 1
        touched_movies.append(current_movie_file)

        current_movie = VideoFileClip(f"{VIDEO_PATH}{current_movie_file}")
        movie_length = math.floor(current_movie.duration)
       
        start_index = random.randint(0, set_clip_buffer(movie_length, LENGTH))
        
        clip = current_movie.subclip(start_index, start_index+LENGTH)
        clip.write_videofile(f"{CLIP_PATH}{count}_{movie_name[0]}.mp4",codec=CODEC)

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

def title_clips():
    '''
    Generate a title for the video clip.
    Title is grabbed from the file name.
    currently, the names are not trimmed or cleaned, so if it is titled
    "The_Shining.mp4" the title preview will show "The_Shining"
    '''
    clips = get_video_files(video_path=CLIP_PATH)
    
    for clip in clips:
        video = VideoFileClip(f"{CLIP_PATH}{clip}", audio=True)
        title = get_name_text(clip)
        w,h = moviesize = video.size
        clip_count = title[0]
        video_title = generate_title(title[1])

        txt_mov = video_title.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )

        final = CompositeVideoClip([video,txt_mov])
        final.subclip(0,LENGTH).write_videofile(f"{generate_title(title[1])}_titled.mp4",codec="libx264")

# remove because of frankenmovie!!
def concat_clips():
    '''
    Concatenate video clips together.
    TODO: Add transitions (As well as custom start and end clips)
    '''
    clips = get_video_files(video_path=CLIP_PATH)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{CLIP_PATH}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list, method="compose")
    final_clip.write_videofile("concat.mp4")

