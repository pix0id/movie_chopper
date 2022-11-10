from moviepy.editor import *
import settings
import movie_chopper as mc

# TODO: Add transitions
# TODO: Count up concat file name so multiple can exist in directory
# TODO: Clip folder cleanup

def concat_clips(clips_folder):
    clips = mc.get_video_files(movie_path=settings.clip_path)
    clip_list = []

    for clip in clips:
        clip_file = VideoFileClip(f"{settings.clip_path}{clip}")
        clip_list.append(clip_file)
    
    final_clip = concatenate_videoclips(clip_list, method="compose")
    final_clip.write_videofile("concat.mp4")

# F R A N K E N M O V I E
concat_clips(clips_folder=settings.clip_path)