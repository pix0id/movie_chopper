from moviepy.editor import *
from settings import *
import movie_chopper as mc

# TODO: Add transitions
# TODO: Count up concat file name so multiple can exist in directory
# TODO: Clip folder cleanup

def concat_clips(video_folder):
    clips = mc.get_video_files(video_folder)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{video_folder}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list, method="compose")
    final_clip.write_videofile("concat.mp4")

# F R A N K E N M O V I E
concat_clips(video_folder=CLIP_PATH)