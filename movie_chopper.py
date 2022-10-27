from moviepy.editor import *
import os
import math
import random
import settings



# Logic variables
touched_movies = []
count = 0

def get_file_extension(file):
    split_name = file.split('.')
    ext = split_name[-1]
    return ext

def verify_extension(ext):
    if ext == "avi" or ext == "mp4" or ext == "mkv":
        return True
    else:
        return False

def get_clip_count():
    clip_count = 0

    for file in os.scandir(settings.clip_path):
        if os.path.isfile(os.path.join(settings.clip_path, file)):
            clip_count += 1
    return clip_count

def get_video_files(video_path):
    '''
        Generates list of videos from specified video path.
        Does not work with nested directories.
        Make sure the videos are the ONLY thing in the directory. ALL FILES are added to the list currently.
        TODO:
            - Make work with nested directories
    '''
    movies_list = []

    for file in os.listdir(settings.video_path):
        
        if verify_extension(get_file_extension(file)):
            if os.path.isfile(os.path.join(settings.video_path, file)):
                movies_list.append(file)
    
    return movies_list


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

        current_movie = VideoFileClip(f"{settings['video_path']}{current_movie_file}")
        movie_length = math.floor(current_movie.duration)
       
        start_index = random.randint(0, set_clip_buffer(movie_length, settings["length"]))
        
        clip = current_movie.subclip(start_index, start_index+settings["length"])
        clip.write_videofile(f"{settings['clip_path']}{count}_{movie_name[0]}.mp4",codec="libx264")

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
    clips = get_video_files(video_path=settings.clip_path)
    
    for clip in clips:
        video = VideoFileClip(f"{settings.clip_path}{clip}", audio=True)
        title = get_name_text(clip)
        w,h = moviesize = video.size
        clip_count = title[0]
        video_title = generate_title(title[1])

        txt_mov = video_title.set_pos( lambda t: (max(w/30,int(w-0.5*w*t)),max(5*h/6,int(100*t))) )

        final = CompositeVideoClip([video,txt_mov])
        final.subclip(0,settings["length"]).write_videofile(f"{generate_title(title[1])}_titled.mp4",codec="libx264")

def concat_clips():
    clips = get_video_files(video_path=settings.clip_path)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{settings.clip_path}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list, method="compose")
    final_clip.write_videofile("concat.mp4")


# Actual execution

# get movies list
# movies = get_video_files(video_path=settings.video_path)


# Create clips
# while count < settings.number_of_clips:
#     clip_random_movie(movies)

# add titles to clips
# title_clips()

# F R A N K E N M O V I E
# concat_clips(clips_folder=settings.clip_path)