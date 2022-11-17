from moviepy.editor import *
from settings import *
import movie_chopper as mc

# TODO: Add transitions
# TODO: Count up concat file name so multiple can exist in directory
# TODO: Clip folder cleanup

def concat_clips(video_folder):
    clips = mc.get_video_files(video_folder)
    
    final_clip = concatenate_videoclips(clips, method="compose")
    final_clip.write_videofile("concat.mp4")