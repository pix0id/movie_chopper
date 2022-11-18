from moviepy.editor import *
from settings import *
import movie_chopper as mc

# TODO: Add transitions
# TODO: Count up concat file name so multiple can exist in directory
# TODO: Create folder for final concats.
# TODO: Clip folder cleanup

def concat_clips(video_folder):
    clips = mc.get_video_files(video_folder)
    clips_list = []

    for clip in clips:
        clips_list.append(VideoFileClip(clip))

    # Add opening and closing "transitions"
    clips_list.insert(0, VideoFileClip(OPENING_TRANSITION))
    clips_list.append(VideoFileClip(CLOSING_TRANSITION))

    final_clip = concatenate_videoclips(clips_list, transition=VideoFileClip(TRANSITION), method="compose")
    final_clip.write_videofile("concat.mp4")